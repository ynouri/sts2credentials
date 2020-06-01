"""
Tests for the sts2credentials package
"""

from sts2credentials.__main__ import configure_credentials


def test_configure_credentials():
    """Test the configuration step"""
    configure_credentials()
