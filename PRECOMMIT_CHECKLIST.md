# Pre-merge checklist

Run this checklist before every pull request is merged.

## Privacy and security

- [ ] No real SSID, password, API key, OTA password, or token
- [ ] No private IP address, MAC address, BSSID, hostname, or router detail
- [ ] No family name, household name, private entity ID, or personal media
- [ ] No raw ESPHome, serial, or installer logs
- [ ] No local paths containing a personal Windows username
- [ ] `secrets.yaml` and local override files remain ignored
- [ ] Demo media metadata contains no private or identifying fields
- [ ] Repository visuals contain no C2PA, SynthID, or other AI provenance marker unless explicitly approved
- [ ] Public test visuals have an exact-byte SHA-256 sidecar when appropriate

## Configuration quality

- [x] Secret references use the generalized names in `secrets.example.yaml`
- [x] YAML sections follow the core, network, hardware, entity, automation order
- [x] Board profile and physical pin mapping match
- [x] BLE tracker/proxy components are absent unless explicitly required
- [x] Classic ESP32 framebuffer remains within the tested memory limit

## Validation

- [ ] All GitHub Actions validation jobs pass on the final commit
- [ ] All GitHub Actions compile jobs pass on the final commit
- [x] Physical RGB display output remains stable
- [x] Deterministic sample image displays correctly on the classic ESP32 profile
- [x] BLE setup completes without image corruption, watchdog reset, or boot loop
- [x] Backlight is disabled during BLE setup and can be restored afterward
- [x] Manual BLE stop disables BLE immediately
- [ ] Wi-Fi reconnect disables BLE as designed
- [x] Rollback path is preserved in Git history

## Release controls

- [x] Repository remains private until explicitly approved
- [x] No release or public tag is created without approval
- [ ] License is selected before public release
