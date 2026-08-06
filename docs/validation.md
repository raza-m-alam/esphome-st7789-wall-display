# Release validation

This document records the release-level checks for version 0.1.0.

## Automated checks

GitHub Actions must validate and compile:

- `install/st7789-wall-display-s3.yaml`
- `wall-display-esp32-classic.yaml`
- `wall-display.yaml`

The workflow uses non-secret CI placeholders. Compilation confirms that the
configuration can produce firmware; it does not replace physical testing.

## Privacy and security checks

- `secrets.yaml` is absent from Git.
- No real SSID, password, API key, OTA password, token, IP address, MAC address,
  BSSID, or household-specific entity ID is tracked.
- Personal media and raw diagnostic logs are ignored.
- Device Builder creates the S3 user's Wi-Fi, API, and OTA secret references
  locally.
- The public demo assets contain no creator, device, location, or personal
  metadata.

## ESP32-S3 N16R8 results

Tested profile: `install/st7789-wall-display-s3.yaml`

- ESP32-S3 N16R8 detected
- 16 MB flash and 8 MB octal PSRAM available
- 170x320 ST7789V initialized at 10 MHz
- Full 108,800-byte framebuffer allocated in PSRAM
- GPIO12 clock, GPIO11 MOSI, GPIO10 CS, GPIO9 DC, GPIO13 reset, GPIO14 backlight
- BGR color order and display inversion enabled
- Correct RGBW static output
- Eight-position animation and timed rotation
- Immediate Home Assistant mode changes
- Encrypted Native API connection
- Device-specific OTA password and successful wireless update
- Local Remote JPEG changed from `Downloading` to `Loaded` and displayed
- BLE Start disabled the backlight before enabling BLE
- BLE Stop disabled BLE and restored the prior display state
- No visible flicker during the protected BLE flow

## Classic ESP32-WROOM-32D results

Tested profile: `wall-display-esp32-classic.yaml`

- 170x320 ST7789V initialized at 5 MHz
- GPIO18 clock, GPIO23 MOSI, GPIO22 CS, GPIO16 DC, GPIO17 reset, GPIO4 backlight
- Correct RGB output and deterministic SVG test image
- 12.5% / 13,600-byte segmented framebuffer
- Stable Wi-Fi and encrypted API operation
- BLE operation without image corruption, watchdog reset, or boot loop
- Manual BLE stop and backlight restoration

A full 108,800-byte framebuffer was rejected for the classic board because it
created severe resource pressure when Wi-Fi and BLE were enabled together.

## Release gate

Before publishing:

1. Add the MIT license and third-party notices.
2. Run CI on the final release commit.
3. Complete a final repository-wide privacy scan.
4. Squash-merge the release pull request.
5. Archive or intentionally retain development pull requests and workflow
   history.
6. Perform a post-merge privacy scan.
7. Create tag `v0.1.0` only after the tagged files match the validated tree.
8. Change repository visibility only after explicit approval.
