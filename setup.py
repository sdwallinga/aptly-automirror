#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
        name='automirror',
        version='0.0.1',
        description='5C AutoMirror',
        author='Sam Wallinga',
        author_email='sam@5thcolumn.net',
        packages=find_packages(),
        install_requires=[
            'hvac',
        ],
)
