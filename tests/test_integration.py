"""
Integration / End to End test for the st2credentials command.

The only mocked component is the `aws sts` command.
"""
# pylint: disable=line-too-long, missing-function-docstring
import os
import subprocess
import pytest
from .test_sts2credentials import STS_ASSUME_ROLE_OUTPUT

EXPECTED_CREDENTIALS = """[sts]
aws_access_key_id = XYZ12XYZ12XYZ12XYZ12
aws_secret_access_key = wXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWn
aws_session_token = FwoGZXIvYXdzEOH//////////wEaDDJGG9XfRY6aIe/6KSK0AZtHj0Jl/SZcMNY1EIqLGPeUPGP0bgl1kxRm2n+R6fg9f34wN07h9doFpjMaFtCJ3uN5SipXzP5SsRgiFi6pCR2MYNku3gnhA0hATCMo0zpWBN2mh4FZlBkm+UwZAoTTdldYzKCNrxH8gYRz8wYkMZ4tyLXdmTkLk0e0X6EhEFhwSBnNWzmu1Dd2EJwN5+C5S6+K/kma8Jrdt+Gt3AThiy2cd+JCnL0o/sUEMdlGkWOSqaopliibitH2BTItcpQXidjuyFcATZnBAV6eBI6YdhmsagKlqJK5FDulH4rK1mt+JBQ7A9P51dkj
"""  # noqa: E501

EXPECTED_CREDENTIALS_CUSTOM_PROFILE_NAME = (
    "[dummy-profile-name]" + EXPECTED_CREDENTIALS[5:]
)


@pytest.mark.parametrize(
    "cmd, expected",
    [
        (["sts2credentials"], EXPECTED_CREDENTIALS),
        (
            ["sts2credentials", "--profile-name", "dummy-profile-name"],
            EXPECTED_CREDENTIALS_CUSTOM_PROFILE_NAME,
        ),
    ],
)
def test_integration(cmd, expected, tmp_path):
    tmp_cred_file = tmp_path / "credentials"
    env = os.environ.copy()
    env["AWS_SHARED_CREDENTIALS_FILE"] = str(tmp_cred_file)
    subprocess.check_output(  # pylint: disable=unexpected-keyword-arg
        cmd, input=STS_ASSUME_ROLE_OUTPUT, env=env
    )
    # Assert credentials file is correctly written
    with tmp_cred_file.open() as f:
        credentials = f.read()
    print(credentials)
    assert credentials == expected
