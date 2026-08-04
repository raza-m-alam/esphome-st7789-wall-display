#!/usr/bin/env python3
"""Generate safe ESPHome secret values without exposing them online."""

from __future__ import annotations

import argparse
import base64
from pathlib import Path
import secrets
import sys

DEFAULT_OUTPUT = Path("secrets.generated.local.yaml")


def build_content() -> str:
    """Return a local ESPHome secrets template with random device secrets."""
    api_key = base64.b64encode(secrets.token_bytes(32)).decode("ascii")
    fallback_password = secrets.token_urlsafe(18)
    ota_password = secrets.token_urlsafe(32)

    return (
        "# Generated locally. Replace the Wi-Fi placeholders, then merge these\n"
        "# values into ESPHome's active secrets.yaml. Never commit this file.\n\n"
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


def main() -> int:
    args = parse_args()
    output: Path = args.output

    if output.exists() and not args.force:
        print(
            f"Refusing to overwrite existing file: {output}. Use --force to replace it.",
            file=sys.stderr,
        )
        return 1

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_content(), encoding="utf-8", newline="\n")
    print(f"Created {output}")
    print("Replace the Wi-Fi placeholders and keep the file out of Git.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
