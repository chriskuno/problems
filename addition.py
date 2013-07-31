#!/usr/bin/env python

import sys


def add(a, b):
  print int(a) + int(b)

if __name__ == "__main__":
  add(sys.argv[1], sys.argv[2])
