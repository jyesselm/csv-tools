#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

readme = open('README.rst').read()
doclink = """
Documentation
-------------

The full documentation is at http://csv-tools.rtfd.org."""
history = open('HISTORY.rst').read().replace('.. :changelog:', '')

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='csv-tools',
    version='0.1.0',
    description='a simple wrapper of pandas to do common csv tasks ',
    long_description=readme + '\n\n' + doclink + '\n\n' + history,
    author='Joe Yesselman',
    author_email='jyesselm@unl.edu',
    url='https://github.com/jyesselm/csv-tools',
    packages=[
        'csv_tools',
    ],
    py_modules=[
        'csv_tools/csv_tools'
    ],
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='csv-tools',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
    entry_points = {
        'console_scripts' : [
            'csv_tools = csv_tools.csv_tools:main'
        ]
    }
)
