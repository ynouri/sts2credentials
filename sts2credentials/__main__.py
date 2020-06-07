"""
sts2credentials: AWS STS output saved to ~/.aws/credentials file.

This is the CLI entry point.
"""
import sys
import json
import argparse
from sts2credentials import parse_credentials, configure_credentials


def parse_args():
    """Parse CLI args, in particular --profile-name"""
    parser = argparse.ArgumentParser(
        description="Save AWS STS output to ~/.aws/credentials file."
    )
    parser.add_argument(
        "--profile-name",
        type=str,
        default="sts",
        help="The profile name to use in ~/.aws/credentials",
    )
    return parser.parse_args()


def sts2credentials(args):
    """Read stdin, parse aws sts output and configure credentials."""
    sts_output = sys.stdin.read()
    try:
        creds_dict = parse_credentials(sts_output)
        configure_credentials(creds_dict, profile_name=args.profile_name)
    except json.decoder.JSONDecodeError:
        print(sts_output)


def main():
    """
    Main function, used as the CLI console_scripts entry point defined in
    setupy.py
    """
    args = parse_args()
    sts2credentials(args)


if __name__ == "__main__":
    main()
