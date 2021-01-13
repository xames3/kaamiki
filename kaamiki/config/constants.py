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

"""Collection of all the constants traversing through implementation"""

import getpass
import pathlib
import sys

# Implementation identity.
_NAME = 'kaamiki'
_CODENAME = 'miroslava'

# The implementation adheres to Semantic Versioning Specification
# (SemVer) starting with version 0.0.1.
# You can read about it here: https://semver.org/spec/v2.0.0.html
_VERSION = '0.0.2'

# Implementation authors and project details.
_AUTHOR = 'Kaamiki Development Team'
_MAINTAINER = 'xames3'
_AUTHOR_EMAIL = _MAINTAINER_EMAIL = 'xames3.kaamiki@gmail.com'
_URL = 'https://github.com/kaamiki/kaamiki'
_LICENSE = 'Apache Software License 2.0'
_DESCRIPTION = (
    'Kaamiki is a simple cross-platform automation framework for data '
    'science and machine learning tasks.'
)

# Current operating system and session user.
_OS = sys.platform  # darwin, linux and win32
_SESSION = getpass.getuser()

# Encoding for all StringIO and FileIO operations.
ENCODING = 'utf-8'

# Separator for string substitution.
SUB_STR_SEP = '_'

# File system separator.
_PATH_SEP = pathlib.os.sep

# Default canonical and sub directories for the implementation
ROOT_DIR = pathlib.Path().home() / _NAME
LOGS_DIR = ROOT_DIR / _SESSION / 'logs'
