#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  2015 giulio <giulioungaretti@me.com>

"""Usage: prof.py -f FILE FIELD

Convert cProfile file into sorted text
Options:
  -h --help
  -f FILE      specify output file [default: ./prof]
"""
from docopt import docopt
import pstats

def Convert(name="./prof", field="cumulative"):
    pstats.Stats(name).strip_dirs().sort_stats(field).print_stats()

if __name__ == '__main__':
    arguments = docopt(__doc__)
    print(arguments)
    _file = arguments.get("-f",None)
    _field = arguments.get("FIELD", None)
    if _file is not None:
        Convert(_file)
    if _field is not None:
        Convert(field=_field)
    else:
        Convert(_file,_field)
