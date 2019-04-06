#!/usr/bin/python

from distutils.core import setup


dist = setup(
    name='uptime',
    version='3.0.1',
    description='Linux uptime library',
    long_description='''\
This module provides a way to retrieve system uptime and boot time.''',
    author='Koen Crolla',
    url='https://github.com/leofiore/uptime-lite',
    package_dir={'uptime': 'src'},
    packages=['uptime'],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Intended Audience :: System Administrators',
                 'License :: OSI Approved :: BSD License',
                 'Operating System :: POSIX :: Linux',
                 'Programming Language :: Python',
                 'Programming Language :: Python :: 2',
                 'Programming Language :: Python :: 3',
                 'Topic :: System']
)
