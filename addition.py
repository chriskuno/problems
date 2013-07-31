#!/usr/bin/env python

import sys


def add(a, b):
  # Computing the sum
  mysum = int(a) * int(b)
  print mysum

if __name__ == "__main__":
  add(sys.argv[1], sys.argv[2])
