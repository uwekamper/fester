#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

setup (
    cmdclass = {'build_ext': build_ext } ,
    ext_modules = [Extension ("fester.integrate", ["fester/integrate.pyx"]),
])