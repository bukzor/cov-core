import setuptools
import sys
import os

from python_lib import python_lib

# The name of the path file must appear after easy-install.pth so that
# cov_core has been added to the sys.path and cov_core_init can be
# imported.
PTH_FILE_NAME = 'init_cov_core.pth'

setuptools.setup(name='cov-core',
                 version='1.15.0',
                 description='plugin core for use by pytest-cov, '
                 'nose-cov and nose2-cov',
                 long_description=open('README.rst').read().strip(),
                 author='Marc Schlaich',
                 author_email='marc.schlaich@gmail.com',
                 url='https://github.com/schlamar/cov-core',
                 py_modules=['cov_core',
                             'cov_core_init'],
                 data_files=[(python_lib, [PTH_FILE_NAME])],
                 install_requires=['coverage>=3.6'],
                 license='MIT License',
                 zip_safe=False,
                 keywords='cover coverage',
                 classifiers=['Development Status :: 4 - Beta',
                              'Intended Audience :: Developers',
                              'License :: OSI Approved :: MIT License',
                              'Operating System :: OS Independent',
                              'Programming Language :: Python',
                              'Programming Language :: Python :: 2.4',
                              'Programming Language :: Python :: 2.5',
                              'Programming Language :: Python :: 2.6',
                              'Programming Language :: Python :: 2.7',
                              'Programming Language :: Python :: 3.0',
                              'Programming Language :: Python :: 3.1',
                              'Topic :: Software Development :: Testing'])
