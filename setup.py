#!/usr/bin/env python3
# vim:fileencoding=utf-8

from setuptools import setup, find_packages
import nvchecker

setup(
  name = 'nvchecker',
  version = nvchecker.__version__,
  packages = find_packages(),
  install_requires = ['tornado'],
  entry_points = {
    'console_scripts': [
      'nvchecker = nvchecker.main:main',
      'nvtake = nvchecker.tools:take',
    ],
  },

  author = 'lilydjwg',
  author_email = 'lilydjwg@gmail.com',
  description = 'New version checker for software',
  license = 'MIT',
  keywords = 'new version build check',
  url = 'https://github.com/lilydjwg/nvchecker',
)
