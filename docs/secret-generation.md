# Local secret generation

Use `tools/generate_secrets.py` to create random ESPHome values without
sending credentials to a website or third-party service.

```powershell
py .\tools\generate_secrets.py
```

The script creates `secrets.generated.local.yaml`, which is ignored by Git.
It generates:

- a 32-byte Base64 API encryption key;
- a long OTA password;
- a fallback access-point password.

It intentionally leaves Wi-Fi values as placeholders so the real SSID and
password are never passed on the command line or stored in shell history.
Replace those placeholders locally and merge the values into ESPHome's active
`secrets.yaml`.

The script refuses to overwrite an existing output file unless `--force` is
specified.
