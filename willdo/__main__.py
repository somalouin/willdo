#!/usr/bin/env python3

import sys
import pyfiglet
from features import list, export
from utils.input import handle_params

def main():
  if len(sys.argv) > 1:
    print(pyfiglet.figlet_format("willdo"))
    if sys.argv[1] == "list": handle_params(sys.argv, list)
    elif sys.argv[1] == "export": handle_params(sys.argv, export)
  else:
    print("[*] Missing argument \n")
    sys.exit(1)

if __name__ == "__main__":
  main()
