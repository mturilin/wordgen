# !/usr/bin/env python

__author__ = 'mikhailturilin'

from distutils.core import setup

setup(
    name='wordgen',
    version='0.1',
    packages=['wordgen'],
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    description="Generate names for the mock objects in Python.",
    long_description=open('README.md').read(),
    install_requires=['functools32', 'path.py'],
    maintainer='Michael Turilin',
    maintainer_email='mturilin@gmail.com',
    package_data={
        'wordgen': ['*.txt']
    }
)

