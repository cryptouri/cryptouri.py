#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="cryptouri",
    version="0.0.0",
    description="URI-based format for encoding cryptographic objects (keys, signatures, etc) using bech32 encoding/checksums",
    long_description="""
        CryptoURI is a URN-like namespace for encoding various cryptographic objects,
        including keys, signatures, and fingerprints/digests. It leverages the bech32
        serialization format to provide a human-friendly encoding and checksums.
    """,
    author="Tony Arcieri",
    author_email="bascule@gmail.com",
    url="https://github.com/cryptouri/cryptouri-py/",
    packages=["cryptouri"],
    include_package_data=True,
    install_requires=[],
    license="Apache-2.0",
    zip_safe=False,
    keywords=["cryptography", "security", "serialization"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
    ],
    test_suite="tests",
    tests_require=[]
)
