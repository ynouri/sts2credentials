"""
sts2credentials: AWS STS output saved to ~/.aws/credentials file.

This is the Python public API.
"""
import json
import subprocess


def configure_credentials(creds_dict, profile_name="sts"):
    """Configure credentials using `aws configure` command."""
    keys_2_configure = [
        ("aws_access_key_id", "AccessKeyId"),
        ("aws_secret_access_key", "SecretAccessKey"),
        ("aws_session_token", "SessionToken"),
    ]
    for keys in keys_2_configure:
        _aws_configure(keys[0], creds_dict[keys[1]], profile_name)


def _aws_configure(key_name, value, profile_name):
    """Configure a single property using `aws configure` command."""
    base_cmd = ["aws", "configure", "set", key_name, value]
    profile_opt = [f"--profile={profile_name}"]
    cmd = base_cmd + profile_opt
    output = subprocess.check_output(cmd)
    return output


def parse_credentials(sts_output):
    """Parse the credentials contained in the output of `aws sts` commands."""
    sts_output_dict = json.loads(sts_output)
    creds_dict = sts_output_dict["Credentials"]
    expected_keys = [
        "AccessKeyId",
        "SecretAccessKey",
        "SessionToken",
        "Expiration",
    ]
    for key in expected_keys:
        assert key in creds_dict
    return creds_dict
