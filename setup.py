#!/usr/bin/env python
#
# Copyright (c) Bo Peng and the University of Texas MD Anderson Cancer Center
# Distributed under the terms of the 3-clause BSD License.

from setuptools import find_packages, setup

# obtain version of SoS
with open('src/sos_python/_version.py') as version:
    for line in version:
        if line.startswith('__version__'):
            __version__ = eval(line.split('=')[1])
            break

setup(
    name="sos-python",
    version=__version__,
    description='SoS Notebook extension for languages Python 2 and Python 3',
    author='Bo Peng',
    url='https://github.com/vatlab/SOS',
    author_email='bBo.Peng@bcm.edu',
    maintainer='Bo Peng',
    maintainer_email='bBo.Peng@bcm.edu',
    license='3-clause BSD',
    include_package_data=True,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: Implementation :: CPython',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=[
        'sos>=0.19.8',
        'sos-notebook>=0.19.4',
    ],
    entry_points='''
[sos_languages]
Python2 = sos_python.kernel:sos_Python
Python3 = sos_python.kernel:sos_Python
''')
