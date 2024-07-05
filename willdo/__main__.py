#!/usr/bin/env python3

import sys
from features import list, export

def main():
  if len(sys.argv) > 1:
    if sys.argv[1] == "list":
      if len(sys.argv) > 2 and sys.argv[2].endswith('.py'):
        list(sys.argv[2])
      else:
        list()
    elif sys.argv[1] == "export":
      export()
  else:
    print("[*] Missing argument \n")
    sys.exit(1)

if __name__ == "__main__":
  main()
