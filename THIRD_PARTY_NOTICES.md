# Third-party notices

The original YAML configurations, Python utilities, documentation, and demo
assets in this repository are licensed under the MIT License in `LICENSE`.
The following upstream projects remain subject to their own licenses.

## ESPHome

The configurations in this repository are inputs to ESPHome. No ESPHome source
code is copied into this repository.

ESPHome uses a combined license: its Python code and other non-runtime material
are MIT licensed, while its C/C++ runtime is licensed under GPL-3.0. Firmware
compiled from these configurations incorporates ESPHome runtime code and is
therefore not governed solely by this repository's MIT License.

Anyone distributing compiled firmware is responsible for complying with all
applicable upstream licenses, including providing the corresponding source and
license notices when required. The initial release of this repository is
source-first; it does not treat a firmware binary as an MIT-only artifact.

- Project: ESPHome
- Source: https://github.com/esphome/esphome
- License: https://github.com/esphome/esphome/blob/dev/LICENSE

## Pillow

`tools/prepare_media.py` uses Pillow when the optional media-preparation tools
are installed. Pillow is not vendored in this repository.

- Project: Pillow
- Source: https://github.com/python-pillow/Pillow
- License: MIT-CMU

## FFmpeg

FFmpeg is an optional external executable used only when converting video.
It is not bundled, linked, or redistributed by this repository. FFmpeg is
normally LGPL-2.1-or-later, but builds that enable optional GPL components are
subject to GPL-2.0-or-later.

- Project: FFmpeg
- Source: https://ffmpeg.org/
- License information: https://ffmpeg.org/legal.html

## Material Design Icons

The ESPHome configurations reference `mdi:` icon names that Home Assistant
renders from its own installed resources. No Material Design Icons files are
bundled here. Material Design Icons are distributed under Apache-2.0, with
separate terms applying to certain brand marks.

- Project: Material Design Icons by Pictogrammers
- License information: https://pictogrammers.com/docs/general/license/

## Generated firmware dependencies

A compiled ESPHome firmware image can also contain ESP-IDF and other platform
components selected by ESPHome. Those components retain their upstream
licenses. Review the generated build notices and dependency manifests before
redistributing firmware binaries.

## Trademarks

ESPHome, Home Assistant, ESP32, ST7789, and other product or project names are
used only to identify compatibility. All trademarks remain the property of
their respective owners. This independent project is not represented as an
official, affiliated, sponsored, or endorsed product of those owners.
