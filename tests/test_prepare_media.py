from pathlib import Path

import pytest
from PIL import Image

from tools import prepare_media


def test_static_output_is_png_at_panel_dimensions(tmp_path: Path) -> None:
    source = tmp_path / "source.jpg"
    output = tmp_path / "panel.png"
    Image.new("RGB", (40, 60), (10, 20, 30)).save(source)

    prepare_media.save_static(source, output, "contain", invert=False)

    with Image.open(output) as image:
        assert image.format == "PNG"
        assert image.size == (170, 320)


def test_animated_output_is_gif_at_panel_dimensions(tmp_path: Path) -> None:
    source = tmp_path / "source.gif"
    output = tmp_path / "panel.gif"
    first = Image.new("RGB", (30, 30), (255, 0, 0))
    second = Image.new("RGB", (30, 30), (0, 255, 0))
    first.save(
        source,
        format="GIF",
        save_all=True,
        append_images=[second],
        duration=[100, 120],
        loop=0,
    )

    prepare_media.save_gif(source, output, "crop", invert=False)

    with Image.open(output) as image:
        assert image.format == "GIF"
        assert image.size == (170, 320)
        assert image.n_frames == 2


def test_output_suffix_must_match_generated_format() -> None:
    with pytest.raises(ValueError, match="Static output must use .png"):
        prepare_media.validate_output_suffix(Path("panel.jpg"), animated=False)

    with pytest.raises(ValueError, match="Animated output must use .gif"):
        prepare_media.validate_output_suffix(Path("panel.png"), animated=True)
