#!/usr/bin/env python3

import sys
import os
from todo import *

def main():
  
  if len(sys.argv) > 1:
    path = sys.argv[1]
    if not os.path.isfile(path):
      print(f"Error: {path} is not a valid file")
      sys.exit(1)
  else:
    print("> No file name provided \n")
    sys.exit(1)
    
  print(f"Reading file: {path}") 
  comments = extract_todo_comments(path)
  display_todo_comments(comments)

if __name__ == "__main__":
  main()
