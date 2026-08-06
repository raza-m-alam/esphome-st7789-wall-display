# Changelog

All notable project changes are recorded here.

## 0.1.0 — 2026-08-05

### Added

- Primary ESP32-S3 N16R8 installation profile for a 170x320 ST7789V display
- Advanced reduced-memory ESP32-WROOM-32D profile
- Home Assistant controls for display mode, backlight, restart, and diagnostics
- RGBW static test and eight-position animation
- Local Remote JPEG URL, refresh control, and explicit load status
- Encrypted Native API and password-protected OTA onboarding through Device Builder
- Guarded BLE provisioning with automatic backlight suppression
- Deterministic public display-test assets
- Optional media-preparation and local secret-generation tools
- GitHub Actions validation and firmware compilation for all tracked profiles
- MIT license and third-party notices

### Validated

- USB installation and subsequent OTA update
- S3 full framebuffer in 8 MB octal PSRAM
- Classic ESP32 13,600-byte segmented framebuffer
- Correct display geometry, offsets, color order, and inversion
- Static output, animation, mode changes, and Remote JPEG
- BLE Start/Stop behavior without visible flicker under the protected backlight flow

### Known limitations

- Hardware profiles are specific to the documented board and pin mappings
- Remote JPEG requires a baseline JPEG reachable by the ESPHome device
- BLE can cause visible backlight interference if the panel is manually driven outside the protected flow
- The compiled-media development profile is not the primary end-user installation path
