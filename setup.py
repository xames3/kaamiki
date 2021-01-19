# Copyright (c) 2021 Kaamiki Development Team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Author(s):
#           xames3 <xames3.kaamiki@gmail.com>

"""
Kaamiki

A Python based implementation of kaamiki.

Kaamiki is a simple cross-platform automation framework for data
science and machine learning tasks. It is an operating system agnostic
Artificial Intelligence development package which provides high-level
and flexible python abstractions for running simple machine learning
applications.
Kaamiki also offers python based nifty tools such as logger, file I/O
related functions, etc. which provides an extension to the developers
existing work.
"""

import sys

from setuptools import find_packages, setup

from kaamiki.config import constants

# Raise early exceptions if the host system is not properly configured
# for installing the framework.
# See https://github.com/kaamiki/kaamiki for more help.
if sys.version_info < (3, ):
    sys.exit('Python 2 has officially reached end-of-life and is no longer '
             'supported by Kaamiki. Please upgrade your python interpreter '
             'to minimum Python 3.6.9 or above')

if sys.version_info < (3, 6, 9):
    sys.exit('Kaamiki supports minimum python 3.6.9 and above. Kindly '
             'upgrade your python interpreter to a suitable version')

if constants._OS == 'win32' and sys.maxsize.bit_length() == 31:
    sys.exit('32-bit Python runtime is not supported.  Please switch to '
             '64-bit Python interpreter')

skip_pkgs = []

with open('requirements.txt', 'r') as requirements:
    if constants._OS == 'win32':
        pkgs = requirements.readlines()
    elif constants._OS == 'linux' or constants._OS == 'darwin':
        pkgs = [pkg for pkg in requirements if pkg.rstrip() not in skip_pkgs]
    else:
        raise RuntimeError('Current platform is not supported by Kaamiki')

setup(
    name=constants._NAME,
    version=constants.__VERSION,
    author=constants.__AUTHOR,
    author_email=constants.__AUTHOR_EMAIL,
    maintainer=constants.__MAINTAINER,
    maintainer_email=constants.__MAINTAINER_EMAIL,
    url=constants.__URL,
    license=constants.__LICENSE,
    description=constants.__DESCRIPTION,
    long_description=open('README.md', encoding=constants.ENCODING).read(),
    long_description_content_type='text/markdown',
    install_requires=pkgs,
    packages=find_packages(),
    # You can find the complete list here:
    # https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ],
)

