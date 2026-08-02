# First-commit validation gate

Do not publish or tag a release until every applicable item passes.

## Preserve rollback first

- Preserve the installed working YAML under its original filename.
- Preserve the exact working image and GIF assets.
- Record the current project version.
- Do not add the old private files to this repository.
- Confirm that the original rollback configuration still compiles.

## Static checks

- `secrets.yaml` is absent from Git.
- No household names, entity IDs, IP addresses, MAC addresses, SSIDs, or
  credentials appear in tracked files.
- `tools/prepare_media.py` successfully processes a static image.
- The tool successfully processes an animated GIF.
- MP4/MOV conversion succeeds when FFmpeg is available.
- Generated media reopens as 170x320.
- GIF frame count, duration, and looping are reported.

## ESPHome checks

1. Validate YAML.
2. Compile successfully.
3. Review warnings.
4. Record firmware size.
5. Do not confuse compilation with installation.

## Physical checks

- Backlight turns on.
- Orientation is portrait.
- All four corners are visible.
- No horizontal offset or clipping is present.
- Demo static image has correct colors.
- Demo animation has correct colors and timing.
- Mode changes work through Home Assistant.
- Remote JPEG downloads and refreshes.
- Remote JPEG calibration colors are correct.
- Wi-Fi reconnects after restart.
- BLE setup recovery remains disabled after Wi-Fi connects.
- Fallback AP appears only after normal Wi-Fi failure.
- OTA update succeeds.
- Encrypted API reconnects.
- Original firmware can be restored.

## Commit rule

The first Git commit is created only after the candidate passes static,
compilation, and physical checks. No public repository or release should
contain the old personalized source tree.
