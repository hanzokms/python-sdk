# coding: utf-8

"""
    Hanzo KMS SDK

    Official Hanzo KMS Python SDK for secrets management, KMS, and dynamic secrets.
"""  # noqa: E501

from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "hanzo-kms"
VERSION = "1.0.1"
PYTHON_REQUIRES = ">=3.8"
REQUIRES = [
    "python-dateutil",
    "aenum",
    "requests~=2.32",
    "boto3~=1.35",
    "botocore~=1.35",
]

setup(
    name=NAME,
    version=VERSION,
    description="Official Hanzo KMS Python SDK",
    author="Hanzo AI, Inc.",
    author_email="support@hanzo.ai",
    url="https://github.com/hanzokms/python-sdk",
    license="BSD-3-Clause",
    keywords=["Hanzo", "KMS", "Hanzo KMS", "SDK", "Secrets Management"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    The official Hanzo KMS Python SDK.
    Documentation can be found at https://github.com/hanzokms/python-sdk
    """,  # noqa: E501
    package_data={"hanzo_kms": ["py.typed"]},
)
