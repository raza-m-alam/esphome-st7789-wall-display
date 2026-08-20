# Validation details

This document records the hardware observations behind version 0.1.0. The
current source is also validated and compiled by GitHub Actions; automated
compilation does not replace physical testing.

## ESP32-S3 N16R8

Tested profile: `install/st7789-wall-display-s3.yaml`

- 16 MB flash and 8 MB octal PSRAM detected
- 170x320 ST7789V initialized at 10 MHz
- full 108,800-byte framebuffer allocated in PSRAM
- GPIO12 clock, GPIO11 MOSI, GPIO10 CS, GPIO9 DC, GPIO13 reset, GPIO14 backlight
- BGR color order and display inversion enabled
- correct RGBW static output
- eight-position animation and timed rotation
- immediate Home Assistant mode changes
- encrypted Native API connection
- device-specific OTA password and successful wireless update
- local Remote JPEG reached `Loaded` and displayed successfully
- BLE Start disabled the backlight before enabling BLE
- BLE Stop disabled BLE and restored the previous display state
- no visible flicker while the primary profile's BLE backlight guard was active

## Classic ESP32-WROOM-32D

Tested profile: `wall-display-esp32-classic.yaml`

- 170x320 ST7789V initialized at 5 MHz
- GPIO18 clock, GPIO23 MOSI, GPIO22 CS, GPIO16 DC, GPIO17 reset, GPIO4 backlight
- correct RGB output and deterministic SVG test image
- 12.5% / 13,600-byte segmented framebuffer
- stable Wi-Fi and encrypted API operation
- BLE operation without image corruption, watchdog reset, or boot loop
- manual BLE stop and backlight restoration

A full framebuffer was rejected for the classic board because it created severe
resource pressure with Wi-Fi and BLE enabled together. The classic profile uses
a simpler backlight-off mitigation; its exposed Backlight entity is not locked
while BLE is active.

## Development profile

`wall-display.yaml` remains a separate `0.2.0-dev` media experiment. It compiles
in CI but is not the primary installation profile and does not carry all of the
primary S3 profile's runtime safeguards.

See `TESTING.md` for the concise release record and CI link.
