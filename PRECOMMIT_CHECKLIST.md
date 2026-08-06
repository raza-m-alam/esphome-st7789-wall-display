# Pre-merge checklist

Run this checklist before every release pull request is merged.

## Privacy and security

- [x] No real SSID, password, API key, OTA password, or token
- [x] No private IP address, MAC address, BSSID, or router detail
- [x] No family name, household name, private entity ID, or personal media
- [x] No raw ESPHome, serial, or installer logs
- [x] No local paths containing a personal account name
- [x] `secrets.yaml` and local override files remain ignored
- [x] Demo media contains no creator, device, location, or identifying metadata
- [x] Public demo assets are original project test graphics
- [x] The classic SVG test card has an exact-byte SHA-256 sidecar

## Configuration quality

- [x] Device Builder creates device-specific Wi-Fi, API, and OTA secret references locally
- [x] The primary install configuration contains no real credentials or private identifiers
- [x] Board profiles and physical pin mappings match the tested hardware
- [x] BLE tracker and Bluetooth proxy components are absent
- [x] The S3 profile uses the tested 8 MB octal PSRAM and full framebuffer
- [x] The classic ESP32 profile stays within the tested 13,600-byte buffer limit
- [x] The primary S3 hostname is stable and does not append a MAC suffix
- [x] Remote JPEG failures have explicit status and display feedback
- [x] BLE setup forces the backlight off before enabling BLE

## Automated validation

- [x] All GitHub Actions validation jobs pass on the final release commit
- [x] All GitHub Actions compile jobs pass on the final release commit
- [x] ESPHome version used for CI matches the final validated release version

## Physical validation — ESP32-S3 N16R8

- [x] Fixed hostname is tracked correctly by Device Builder
- [x] Wi-Fi connects and encrypted Native API authenticates
- [x] Device-specific OTA password is configured and wireless installation succeeds
- [x] Static RGBW output has correct geometry and colors
- [x] Eight-frame animation renders and demo rotation works
- [x] Display-mode changes respond immediately
- [x] Remote JPEG changes from `Downloading` to `Loaded` and displays successfully
- [x] BLE Start turns the backlight off before enabling BLE
- [x] BLE Stop disables BLE and restores the prior display state
- [x] No visible flicker occurs while protected BLE setup is active

## Physical validation — classic ESP32-WROOM-32D

- [x] RGB output and deterministic sample image render correctly
- [x] Wi-Fi and encrypted API remain stable with the reduced framebuffer
- [x] BLE setup completes without image corruption, watchdog reset, or boot loop
- [x] Manual BLE stop disables BLE immediately
- [x] Backlight-off mitigation prevents normal users from seeing BLE-induced flicker

## Licensing and provenance

- [x] MIT license selected for original repository content
- [x] Copyright holder recorded as `Raza M Alam`
- [x] Third-party licensing boundaries documented
- [x] No third-party photographs, logos, firmware blobs, or copied source files are bundled
- [x] Optional Pillow, FFmpeg, ESPHome, and icon references are documented
- [x] Source-first release avoids presenting generated firmware as an MIT-only artifact

## Release controls

- [x] Repository remains private until explicitly approved
- [x] No public tag or release is created without approval
- [x] Rollback path remains available in private development history
- [ ] Stale development branches and visible workflow history are cleaned or intentionally retained
- [ ] Pull requests are archived or intentionally left public before visibility changes
- [ ] Final squash merge is complete
- [ ] One post-merge privacy scan passes
- [ ] Explicit approval is received before changing repository visibility
