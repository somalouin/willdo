#!/usr/bin/env python3

import sys
import os
from features import list

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "list":
      list()
  else:
    print("[*] Missing argument \n")
    sys.exit(1)

if __name__ == "__main__":
  main()
