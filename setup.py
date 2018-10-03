#!/usr/bin/env python3
from setuptools import setup, find_packages
setup(
        name='automirror',
        version='0.0.1',
        description='aptly-automirror',
        author='Sam Wallinga',
        author_email='samwallinga@gmail.com',
        packages=find_packages(),
        install_requires=[
            'hvac',
        ],
)
