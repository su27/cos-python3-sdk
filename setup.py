#!/usr/bin/env python

from setuptools import setup
import sys

if sys.version_info[0] != 3 or sys.version_info[1] < 5:
    sys.exit('Sorry, only python 3.5 and above is supported.')

setup(
    name='qcloud_cos3',
    version='0.1.0',
    description='an unofficial sdk for qcloud cos',
    author='su27',
    author_email='damn.su@gmail.com',
    url='https://github.com/su27/cos-python3-sdk',
    packages=['qcloud_cos3'],
    include_package_data=True,
    install_requires=['requests>=2.0'],
    license='MIT License',
    zip_safe=False,
)
