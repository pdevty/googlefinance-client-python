# coding: utf-8

try:
    import setuptools
    from setuptools import setup, find_packages
except ImportError:
    print("Please install setuptools.")

import os
long_description = 'googlefinance.client is a python client library for google finance api.'
if os.path.exists('README.txt'):
    long_description = open('README.txt').read()

setup(
    name  = 'googlefinance.client',
    version = '1.1.2',
    description = 'googlefinance.client is a python client library for google finance api.',
    long_description = long_description,
    license = 'MIT',
    author = 'pdevty',
    author_email = 'p.dev.ty@gmail.com',
    url = 'https://github.com/pdevty/googlefinance-client-python',
    keywords = 'googlefinance',
    packages = find_packages(),
    install_requires = ['datetime', 'requests', 'pandas'],
    classifiers = [
      'Programming Language :: Python :: 3.6',
      'Intended Audience :: Financial and Insurance Industry',
      'License :: OSI Approved :: MIT License'
    ]
)