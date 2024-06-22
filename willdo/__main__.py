#!/usr/bin/env python3

import sys
from todo import *

def main():
  if len(sys.argv) > 1:
      name = sys.argv[1]
      print(f"Reading file: {name}")
  else:
      print("No file name provided")
  
  comments = extract_todo_comments("test/test_todo.py")
  display_todo_comments(comments)

if __name__ == "__main__":
  main()
