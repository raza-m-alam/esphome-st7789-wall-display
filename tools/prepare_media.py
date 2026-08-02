"""Prepare still images, GIFs, MP4s, or MOVs for the tested 170x320 panel.

The tested panel requires all source RGB channels to be fully inverted
before ESPHome embeds the media. This script performs that compensation,
resizes/crops the input, writes the expected output filename, and reopens
the result for validation.

Video input requires ffmpeg on PATH.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageOps, ImageSequence

WIDTH = 170
HEIGHT = 320
VIDEO_EXTENSIONS = {".mp4", ".mov", ".m4v", ".avi", ".mkv", ".webm"}
ANIMATED_EXTENSIONS = {".gif", ".webp"}

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_IMAGE_OUTPUT = REPO_ROOT / "assets" / "user" / "background_panel.png"
DEFAULT_ANIMATION_OUTPUT = REPO_ROOT / "assets" / "user" / "animation_panel.gif"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Prepare media for the tested ESPHome ST7789 wall display."
    )
    parser.add_argument("input", type=Path, help="Input image, GIF, MP4, or MOV")
    parser.add_argument(
        "--output",
        type=Path,
        help="Output path. Defaults to assets/user/background_panel.png "
             "or assets/user/animation_panel.gif.",
    )
    parser.add_argument(
        "--fit",
        choices=("crop", "contain"),
        default="crop",
        help="crop fills 170x320; contain letterboxes without cropping.",
    )
    parser.add_argument(
        "--fps",
        type=float,
        default=6.0,
        help="Frame rate used when extracting video. Default: 6.",
    )
    parser.add_argument(
        "--max-seconds",
        type=float,
        default=10.0,
        help="Maximum video duration to convert. Default: 10.",
    )
    parser.add_argument(
        "--no-invert",
        action="store_true",
        help="Do not fully invert RGB. Use only for a panel proven not to "
             "need the tested panel's compensation.",
    )
    return parser.parse_args()


def fit_frame(image: Image.Image, mode: str) -> Image.Image:
    rgb = image.convert("RGB")
    if mode == "crop":
        return ImageOps.fit(
            rgb,
            (WIDTH, HEIGHT),
            method=Image.Resampling.LANCZOS,
            centering=(0.5, 0.5),
        )
    return ImageOps.pad(
        rgb,
        (WIDTH, HEIGHT),
        method=Image.Resampling.LANCZOS,
        color=(0, 0, 0),
        centering=(0.5, 0.5),
    )


def compensate(image: Image.Image, invert: bool) -> Image.Image:
    fitted = image.convert("RGB")
    return ImageOps.invert(fitted) if invert else fitted


def prepare_frame(image: Image.Image, fit: str, invert: bool) -> Image.Image:
    return compensate(fit_frame(image, fit), invert)


def save_static(
    source: Path,
    output: Path,
    fit: str,
    invert: bool,
) -> None:
    with Image.open(source) as image:
        prepared = prepare_frame(image, fit, invert)
        output.parent.mkdir(parents=True, exist_ok=True)
        prepared.save(output, format="PNG", optimize=True)


def save_animated_frames(
    frames: list[Image.Image],
    durations: list[int],
    output: Path,
) -> None:
    if not frames:
        raise ValueError("No animation frames were generated.")
    output.parent.mkdir(parents=True, exist_ok=True)
    frames[0].save(
        output,
        format="GIF",
        save_all=True,
        append_images=frames[1:],
        duration=durations,
        loop=0,
        disposal=2,
        optimize=False,
    )


def save_gif(
    source: Path,
    output: Path,
    fit: str,
    invert: bool,
) -> None:
    frames: list[Image.Image] = []
    durations: list[int] = []

    with Image.open(source) as image:
        default_duration = int(image.info.get("duration", 167) or 167)
        for frame in ImageSequence.Iterator(image):
            frames.append(prepare_frame(frame, fit, invert))
            duration = int(frame.info.get("duration", default_duration) or default_duration)
            durations.append(max(20, duration))

    save_animated_frames(frames, durations, output)


def extract_video_frames(
    source: Path,
    fps: float,
    max_seconds: float,
    directory: Path,
) -> list[Path]:
    ffmpeg = shutil.which("ffmpeg")
    if not ffmpeg:
        raise RuntimeError(
            "Video conversion requires ffmpeg on PATH. "
            "Install or expose ffmpeg, then retry."
        )

    frame_pattern = directory / "frame_%05d.png"
    command = [
        ffmpeg,
        "-hide_banner",
        "-loglevel",
        "error",
        "-y",
        "-i",
        str(source),
        "-t",
        str(max_seconds),
        "-vf",
        f"fps={fps}",
        str(frame_pattern),
    ]
    subprocess.run(command, check=True)
    return sorted(directory.glob("frame_*.png"))


def save_video(
    source: Path,
    output: Path,
    fit: str,
    invert: bool,
    fps: float,
    max_seconds: float,
) -> None:
    if fps <= 0:
        raise ValueError("--fps must be greater than zero.")
    if max_seconds <= 0:
        raise ValueError("--max-seconds must be greater than zero.")

    with tempfile.TemporaryDirectory(prefix="wall_display_frames_") as temp:
        frame_paths = extract_video_frames(
            source, fps, max_seconds, Path(temp)
        )
        if not frame_paths:
            raise RuntimeError("ffmpeg did not produce any frames.")

        frames: list[Image.Image] = []
        for frame_path in frame_paths:
            with Image.open(frame_path) as image:
                frames.append(prepare_frame(image, fit, invert))

        duration_ms = max(20, round(1000.0 / fps))
        durations = [duration_ms] * len(frames)
        save_animated_frames(frames, durations, output)


def verify_output(output: Path) -> str:
    with Image.open(output) as image:
        if image.size != (WIDTH, HEIGHT):
            raise RuntimeError(
                f"Output is {image.size}, expected {(WIDTH, HEIGHT)}."
            )

        frame_count = getattr(image, "n_frames", 1)
        if frame_count > 1:
            durations = []
            for frame in ImageSequence.Iterator(image):
                durations.append(int(frame.info.get("duration", 0) or 0))
            loop = image.info.get("loop")
            return (
                f"{output} | {WIDTH}x{HEIGHT} | {frame_count} frames | "
                f"durations={durations} ms | loop={loop}"
            )

        return f"{output} | {WIDTH}x{HEIGHT} | static PNG"


def main() -> int:
    args = parse_args()
    source = args.input.expanduser().resolve()

    if not source.is_file():
        print(f"Input file does not exist: {source}", file=sys.stderr)
        return 2

    extension = source.suffix.lower()
    is_video = extension in VIDEO_EXTENSIONS

    is_animated_image = False
    if not is_video:
        try:
            with Image.open(source) as image:
                is_animated_image = bool(
                    getattr(image, "is_animated", False)
                    and getattr(image, "n_frames", 1) > 1
                )
        except Exception as exc:
            print(f"Cannot open input media: {exc}", file=sys.stderr)
            return 2

    animated = is_video or is_animated_image
    output = (
        args.output.expanduser()
        if args.output
        else (DEFAULT_ANIMATION_OUTPUT if animated else DEFAULT_IMAGE_OUTPUT)
    ).resolve()

    invert = not args.no_invert

    try:
        if is_video:
            save_video(
                source,
                output,
                args.fit,
                invert,
                args.fps,
                args.max_seconds,
            )
        elif is_animated_image:
            save_gif(source, output, args.fit, invert)
        else:
            save_static(source, output, args.fit, invert)

        print(verify_output(output))
        print(
            "RGB compensation: "
            + ("full channel inversion applied" if invert else "not applied")
        )
        return 0
    except subprocess.CalledProcessError as exc:
        print(f"ffmpeg failed with exit code {exc.returncode}.", file=sys.stderr)
        return exc.returncode or 1
    except Exception as exc:
        print(f"Media preparation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
