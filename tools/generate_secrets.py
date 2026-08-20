#!/usr/bin/env python3
"""Generate local ESPHome secret values without exposing them online."""

from __future__ import annotations

import argparse
import base64
import os
import secrets
import sys
from pathlib import Path

DEFAULT_OUTPUT = Path("secrets.generated.local.yaml")


def build_content() -> str:
    """Return an ESPHome secrets template with random device secrets."""
    api_key = base64.b64encode(secrets.token_bytes(32)).decode("ascii")
    fallback_password = secrets.token_urlsafe(18)
    ota_password = secrets.token_urlsafe(32)

    return (
        "# Generated locally. Replace the Wi-Fi placeholders, then merge these\n"
        "# values into ESPHome's active secrets.yaml. Do not commit this file.\n\n"
        'wifi_ssid: "REPLACE_WITH_WIFI_SSID"\n'
        'wifi_password: "REPLACE_WITH_WIFI_PASSWORD"\n'
        f'fallback_ap_password: "{fallback_password}"\n'
        f'ota_password: "{ota_password}"\n'
        f'api_encryption_key: "{api_key}"\n'
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Generate random ESPHome API, OTA, and fallback-AP secrets."
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"output path (default: {DEFAULT_OUTPUT})",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="replace an existing output file",
    )
    return parser.parse_args()


def write_secure_file(output: Path, content: str, force: bool) -> None:
    """Write a new local file with owner-only permissions where supported."""
    output.parent.mkdir(parents=True, exist_ok=True)
    flags = os.O_WRONLY | os.O_CREAT | (os.O_TRUNC if force else os.O_EXCL)

    try:
        descriptor = os.open(output, flags, 0o600)
    except FileExistsError as exc:
        raise FileExistsError(
            f"Refusing to overwrite existing file: {output}. "
            "Use --force to replace it."
        ) from exc

    with os.fdopen(descriptor, "w", encoding="utf-8", newline="\n") as file:
        file.write(content)


def main() -> int:
    args = parse_args()
    output = args.output.expanduser()

    try:
        write_secure_file(output, build_content(), args.force)
    except FileExistsError as exc:
        print(exc, file=sys.stderr)
        return 1

    print(f"Created {output}")
    print("Replace the Wi-Fi placeholders and keep the file out of Git.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
