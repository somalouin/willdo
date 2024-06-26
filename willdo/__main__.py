#!/usr/bin/env python3

import sys
import os
from features import execute

def main():
  if len(sys.argv) > 1:
    parameter = sys.argv[1]
    path = sys.argv[2]
    # check for parameter
    if parameter != "-t":
      print("> Invalid parameter")
      sys.exit(1)
    # check for file
    if not os.path.isfile(path):
      print(f"Error: {path} is not a valid file")
      sys.exit(1)
  else:
    print("> No file name provided \n")
    sys.exit(1)
  execute(parameter, path)

if __name__ == "__main__":
  main()
