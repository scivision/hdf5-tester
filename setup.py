#!/usr/bin/env python
from setuptools import setup

install_requires = ['h5py']
tests_require = ['pytest', 'coveralls', 'flake8', 'mypy']

# %% install
setup(name='HDF5tester',
      description='Test HDF5 files with Python and h5py',
      author='Michael Hirsch, Ph.D.',
      url='https://github.com/scivision/hdf5-tester',
      version='0.9.0',
      long_description=open("README.md").read(),
      long_description_content_type="text/markdown",
      install_requires=install_requires,
      tests_require=tests_require,
      extras_require={'tests': tests_require},
      python_requires='>=3.6',
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Intended Audience :: End Users/Desktop',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7', ]
      )
