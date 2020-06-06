# sts2credentials

[![Python package](https://github.com/ynouri/sts2credentials/workflows/Python%20package/badge.svg)](https://github.com/ynouri/sts2credentials/actions) [![PyPI package](https://badge.fury.io/py/sts2credentials.svg)](https://pypi.org/project/sts2credentials/)

AWS STS output saved to ~/.aws/credentials file

## Pre-requisites

- MacOS / Linux
- Python 3.6+
- AWS CLI

## How to install

`pip install sts2credentials`

## How to use

```
aws sts assume-role \
    --role-arn arn:aws:iam::123456789012:role/RoleYouWantToAssume \
    --role-session-name SomeSessionName \
    | sts2credentials
```

By default, `sts2credentials` will write the credentials output by the `aws sts` command in your `~/.aws/credentials` file, under a profile named `sts`.

Behind the scene, `sts2credentials` runs `aws configure` commands to set the configuration.

## References

This tool has been inspired by this Stack Overflow answer: https://stackoverflow.com/a/57430760/1489984
