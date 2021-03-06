# -*- coding: utf-8 -*-
# Copyright (c) 2011, 2012, Sebastian Wiesner <lunaryorn@gmail.com>
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:

# 1. Redistributions of source code must retain the above copyright notice,
#    this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

import sys
import os
import re
if sys.version_info[0] < 3:
    from codecs import open

from setuptools import setup, find_packages


with open('README.rst', encoding='utf-8') as stream:
    long_desc = stream.read()


VERSION_PATTERN = re.compile(r"__version__ = '([^']+)'")


def read_version_number():
    with open(os.path.join('src', 'sphinxcontrib', 'programoutput.py')) as stream:
        for line in stream:
            match = VERSION_PATTERN.search(line)
            if match:
                return match.group(1)
        else:
            raise ValueError('Could not extract version number')


setup(
    name='nti.sphinxcontrib-programoutput',
    version=read_version_number(),
    url='http://sphinxcontrib-programoutput.readthedocs.org/',
    download_url='http://pypi.python.org/pypi/sphinxcontrib-programoutput',
    license='BSD',
    author='Sebastian Wiesner',
    author_email='lunaryorn@gmail.com',
    description='Sphinx extension to include program output',
    long_description=long_desc,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Documentation',
        'Topic :: Utilities',
    ],
    platforms='any',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=['Sphinx>=1.1'],
    namespace_packages=['sphinxcontrib'],
)
