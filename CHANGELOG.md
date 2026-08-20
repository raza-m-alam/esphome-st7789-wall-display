# Changelog

All notable project changes are recorded here.

## Unreleased

### Changed

- Simplified public documentation and replaced the release-audit checklist with
  a concise testing record
- Clarified that BLE setup is time-limited but unauthenticated on the tested
  hardware
- Documented the fixed-hostname requirement for multiple displays and the
  trusted-LAN assumption for runtime JPEGs
- Added the same minimum ESPHome version to all tracked profiles
- Pinned the tested Pillow version and added Ruff and Pytest tooling

### Fixed

- Removed the duplicate Remote JPEG refresh path in the primary S3 profile
- Removed redundant state publication from the optimistic Remote JPEG URL text
  entity
- Reused the project version substitution in startup logging
- Rejected media output filenames whose suffix does not match the generated
  PNG or GIF format
- Created generated secret files with owner-only permissions where supported

## 0.1.0 — 2026-08-05

### Added

- Primary ESP32-S3 N16R8 installation profile for a 170x320 ST7789V display
- Advanced reduced-memory ESP32-WROOM-32D profile
- Home Assistant controls for display mode, backlight, restart, and diagnostics
- RGBW static test and eight-position animation
- Local Remote JPEG URL, refresh control, and explicit load status
- Encrypted Native API and password-protected OTA onboarding through Device
  Builder
- Time-limited BLE setup with backlight suppression on the primary S3 profile
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
- BLE Start/Stop behavior without visible flicker under the primary profile's
  backlight guard

### Known limitations

- Hardware profiles are specific to the documented board and pin mappings
- Remote JPEG requires a baseline JPEG reachable by the ESPHome device
- BLE provisioning has no separate physical authorization input
- The compiled-media development profile is not the primary installation path
