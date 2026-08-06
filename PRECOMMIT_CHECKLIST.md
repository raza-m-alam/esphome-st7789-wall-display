# Pre-merge checklist

Run this checklist before every pull request is merged.

## Privacy and security

- [x] No real SSID, password, API key, OTA password, or token
- [x] No private IP address, MAC address, BSSID, hostname, or router detail
- [x] No family name, household name, private entity ID, or personal media
- [x] No raw ESPHome, serial, or installer logs
- [x] No local paths containing a personal Windows username
- [x] `secrets.yaml` and local override files remain ignored
- [x] Demo media metadata contains no private or identifying fields
- [x] Repository visuals contain no C2PA, SynthID, or other AI provenance marker unless explicitly approved
- [x] Public test visuals have an exact-byte SHA-256 sidecar when appropriate

## Configuration quality

- [x] Device Builder can create device-specific Wi-Fi, API-encryption, and OTA secret references locally
- [x] Published install configuration contains no real credentials or private network identifiers
- [x] Board profile and physical pin mapping match the tested hardware
- [x] BLE tracker/proxy components are absent unless explicitly required
- [x] S3 profile uses the tested 8 MB octal PSRAM and full 108,800-byte framebuffer
- [x] Classic ESP32 profile remains within the tested 13,600-byte framebuffer limit

## Automated validation

- [x] All GitHub Actions validation jobs pass on the final test commit
- [x] All GitHub Actions compile jobs pass on the final test commit

## Physical validation — ESP32-S3 N16R8

- [x] Fixed hostname is tracked correctly by Device Builder
- [x] Wi-Fi connects and encrypted Native API authenticates
- [x] Device-specific OTA password is configured and wireless installation succeeds
- [x] Static RGBW test renders with correct geometry and colors
- [x] Eight-frame animation renders and demo rotation works
- [x] Display-mode changes respond immediately
- [x] Remote JPEG changes from `Downloading` to `Loaded` and displays successfully
- [x] BLE Start turns the backlight off before enabling BLE
- [x] BLE Stop disables BLE and restores the prior display state
- [x] No visible BLE flicker while the protected backlight behavior is active

## Physical validation — classic ESP32-WROOM-32D

- [x] RGB output and deterministic sample image render correctly
- [x] Wi-Fi and encrypted API remain stable with the reduced framebuffer
- [x] BLE setup completes without image corruption, watchdog reset, or boot loop
- [x] Manual BLE stop disables BLE immediately
- [x] Backlight-off mitigation prevents normal users from seeing BLE-induced flicker

## Release controls

- [x] Repository remains private until explicitly approved
- [x] No release or public tag is created without approval
- [x] Rollback path is preserved in Git history
- [ ] License decision recorded, or repository intentionally published without a reuse license
- [ ] Final squash merge completed
- [ ] Explicit approval received before changing repository visibility
