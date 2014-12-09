#!/usr/bin/env python
from distutils.sysconfig import get_python_lib
import os, sys

python_lib = os.path.relpath(get_python_lib(), sys.prefix)

if __name__ == '__main__':
    print(python_lib)
