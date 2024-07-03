#!/usr/bin/env python3

import sys
from features import list, export

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "list":
      list()
    elif sys.argv[1] == "export":
      export()
  else:
    print("[*] Missing argument \n")
    sys.exit(1)

if __name__ == "__main__":
  main()
