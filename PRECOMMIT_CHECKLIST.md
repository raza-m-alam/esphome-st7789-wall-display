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

- [ ] Secret references use the generalized names in `secrets.example.yaml`
- [ ] YAML sections follow the core, network, hardware, entity, automation order
- [ ] Board profile and physical pin mapping match
- [ ] BLE tracker/proxy components are absent unless explicitly required
- [ ] Classic ESP32 framebuffer remains within the tested memory limit

## Validation

- [ ] All GitHub Actions validation jobs pass
- [ ] All GitHub Actions compile jobs pass
- [x] Physical RGB display output remains stable
- [x] Deterministic sample image displays correctly on the classic ESP32 profile
- [ ] BLE setup window is tested without flicker, scrambling, or rebooting
- [ ] Wi-Fi reconnect disables BLE as designed
- [ ] Rollback path is preserved

## Release controls

- [ ] Repository remains private until explicitly approved
- [ ] No release or public tag is created without approval
- [ ] License is selected before public release
