"""
Unit tests for the sts2credentials package.
"""
# pylint: disable=line-too-long, missing-function-docstring
from unittest.mock import patch, call
from sts2credentials.__main__ import (
    aws_configure,
    configure_credentials,
    parse_credentials,
)

STS_ASSUME_ROLE_OUTPUT = b"""{
    "Credentials": {
        "AccessKeyId": "XYZ12XYZ12XYZ12XYZ12",
        "SecretAccessKey": "wXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWn",
        "SessionToken": "FwoGZXIvYXdzEOH//////////wEaDDJGG9XfRY6aIe/6KSK0AZtHj0Jl/SZcMNY1EIqLGPeUPGP0bgl1kxRm2n+R6fg9f34wN07h9doFpjMaFtCJ3uN5SipXzP5SsRgiFi6pCR2MYNku3gnhA0hATCMo0zpWBN2mh4FZlBkm+UwZAoTTdldYzKCNrxH8gYRz8wYkMZ4tyLXdmTkLk0e0X6EhEFhwSBnNWzmu1Dd2EJwN5+C5S6+K/kma8Jrdt+Gt3AThiy2cd+JCnL0o/sUEMdlGkWOSqaopliibitH2BTItcpQXidjuyFcATZnBAV6eBI6YdhmsagKlqJK5FDulH4rK1mt+JBQ7A9P51dkj",
        "Expiration": "2020-06-01T01:00:27Z"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "ABC1234ABC1234ABC1234:MyDummyRole",
        "Arn": "arn:aws:sts::123456789012:assumed-role/MyDummyRole/MyDummySessionName"
    }
}
"""  # noqa: E501

EXPECTED_CREDS_DICT = {
    "AccessKeyId": "XYZ12XYZ12XYZ12XYZ12",
    "SecretAccessKey": "wXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWn",
    "SessionToken": "FwoGZXIvYXdzEOH//////////wEaDDJGG9XfRY6aIe/6KSK0AZtHj0Jl/SZcMNY1EIqLGPeUPGP0bgl1kxRm2n+R6fg9f34wN07h9doFpjMaFtCJ3uN5SipXzP5SsRgiFi6pCR2MYNku3gnhA0hATCMo0zpWBN2mh4FZlBkm+UwZAoTTdldYzKCNrxH8gYRz8wYkMZ4tyLXdmTkLk0e0X6EhEFhwSBnNWzmu1Dd2EJwN5+C5S6+K/kma8Jrdt+Gt3AThiy2cd+JCnL0o/sUEMdlGkWOSqaopliibitH2BTItcpQXidjuyFcATZnBAV6eBI6YdhmsagKlqJK5FDulH4rK1mt+JBQ7A9P51dkj",  # noqa: E501
    "Expiration": "2020-06-01T01:00:27Z",
}


def test_parse_credentials():
    creds_dict = parse_credentials(STS_ASSUME_ROLE_OUTPUT)
    assert creds_dict == EXPECTED_CREDS_DICT


@patch("sts2credentials.__main__.subprocess.check_output")
def test_aws_configure(mock_check_output):
    aws_configure("dummy_key", "dummy_value", "dummy_profile")
    expected_cmd = [
        "aws",
        "configure",
        "set",
        "dummy_key",
        "dummy_value",
        "--profile=dummy_profile",
    ]
    # aws configure set aws_access_key_id dummy_value --profile=dummy_profile
    mock_check_output.assert_called_once_with(expected_cmd)


@patch("sts2credentials.__main__.aws_configure")
def test_configure_credentials(mock_aws_configure):
    configure_credentials(EXPECTED_CREDS_DICT, profile_name="dummy_profile")
    expected_calls = [
        call("aws_access_key_id", "XYZ12XYZ12XYZ12XYZ12", "dummy_profile"),
        call(
            "aws_secret_access_key",
            "wXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWnwXRWn",
            "dummy_profile",
        ),
        call(
            "aws_session_token",
            "FwoGZXIvYXdzEOH//////////wEaDDJGG9XfRY6aIe/6KSK0AZtHj0Jl/SZcMNY1EIqLGPeUPGP0bgl1kxRm2n+R6fg9f34wN07h9doFpjMaFtCJ3uN5SipXzP5SsRgiFi6pCR2MYNku3gnhA0hATCMo0zpWBN2mh4FZlBkm+UwZAoTTdldYzKCNrxH8gYRz8wYkMZ4tyLXdmTkLk0e0X6EhEFhwSBnNWzmu1Dd2EJwN5+C5S6+K/kma8Jrdt+Gt3AThiy2cd+JCnL0o/sUEMdlGkWOSqaopliibitH2BTItcpQXidjuyFcATZnBAV6eBI6YdhmsagKlqJK5FDulH4rK1mt+JBQ7A9P51dkj",  # noqa: E501
            "dummy_profile",
        ),
    ]
    mock_aws_configure.assert_has_calls(expected_calls)
