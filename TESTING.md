# Testing

This file summarizes the evidence behind the supported profiles. Automated
compilation confirms that current configuration files build; it does not
replace physical hardware testing.

## Automated checks

The [ESPHome validation workflow](https://github.com/raza-m-alam/esphome-st7789-wall-display/actions/workflows/esphome.yml)
performs:

- ESPHome validation and firmware compilation for all three profiles;
- Ruff linting for the Python utilities and tests;
- Pytest coverage for generated static media, animated media, output suffix
  validation, secret generation, overwrite protection, and local file mode.

## Physical release record

| Recorded | Configuration | Hardware | ESPHome | Result |
|---|---|---|---|---|
| 2026-08-05 | `install/st7789-wall-display-s3.yaml` | ESP32-S3 N16R8, ST7789V 170x320 | 2026.7.4 | USB install, OTA, RGBW output, animation, mode changes, local JPEG, and BLE Start/Stop passed |
| 2026-08-05 | `wall-display-esp32-classic.yaml` | ESP32-WROOM-32D, ST7789V 170x320 | 2026.7.4 | Reduced-buffer rendering, Wi-Fi/API, sample image, and time-limited BLE passed |

Detailed hardware settings and observations are in `docs/validation.md`.
Changes that alter runtime hardware behavior should be physically re-tested on
the affected profile before a release claim is updated.
