import base64
import os
from pathlib import Path

from tools import generate_secrets


def _value(content: str, key: str) -> str:
    prefix = f'{key}: "'
    line = next(line for line in content.splitlines() if line.startswith(prefix))
    return line[len(prefix) : -1]


def test_generated_api_key_is_32_random_bytes() -> None:
    first = generate_secrets.build_content()
    second = generate_secrets.build_content()

    first_key = _value(first, "api_encryption_key")
    second_key = _value(second, "api_encryption_key")

    assert len(base64.b64decode(first_key)) == 32
    assert first_key != second_key


def test_secure_writer_refuses_overwrite_and_uses_owner_mode(tmp_path: Path) -> None:
    output = tmp_path / "secrets.generated.local.yaml"
    generate_secrets.write_secure_file(output, "test\n", force=False)

    if os.name == "posix":
        assert output.stat().st_mode & 0o777 == 0o600

    try:
        generate_secrets.write_secure_file(output, "changed\n", force=False)
    except FileExistsError:
        pass
    else:
        raise AssertionError("existing file was overwritten without --force")
