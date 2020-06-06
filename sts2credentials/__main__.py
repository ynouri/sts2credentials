"""
sts2credentials: AWS STS output saved to ~/.aws/credentials file.

This is the CLI entry point.
"""
import sys
import json
from sts2credentials import parse_credentials, configure_credentials


def sts2credentials():
    """Read stdin, parse aws sts output and configure credentials."""
    sts_output = sys.stdin.read()
    try:
        creds_dict = parse_credentials(sts_output)
        configure_credentials(creds_dict)
    except json.decoder.JSONDecodeError:
        print(sts_output)


if __name__ == "__main__":
    sts2credentials()
