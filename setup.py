"""Setup.py"""
from setuptools import setup, find_packages

INSTALL_REQUIRES = []

EXTRAS_REQUIRE = {
    "test": [
        "pytest",
        "pytest-clarity",
        "black",
        "flake8",
        "pylint",
        "awscli",
    ],
    "dev": ["tox"],
}

EXTRAS_REQUIRE["dev"] += EXTRAS_REQUIRE["test"]

ENTRY_POINT = "sts2credentials=sts2credentials.__main__:sts2credentials"

setup(
    name="sts2credentials",
    version="0.0.3",
    description="AWS STS output saved to ~/.aws/credentials file",
    author="Yacine Nouri",
    author_email="yacine@nouri.io",
    url="https://github.com/ynouri/sts2credentials/",
    include_package_data=True,
    install_requires=INSTALL_REQUIRES,
    setup_requires=[],
    python_requires=">=3.6",
    extras_require=EXTRAS_REQUIRE,
    py_modules=["sts2credentials"],
    entry_points={"console_scripts": [ENTRY_POINT]},
    zip_safe=False,
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
