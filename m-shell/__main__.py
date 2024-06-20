#!/usr/bin/env python3

import sys
from todo import *

def main():
  if len(sys.argv) > 1:
      name = sys.argv[1]
  else:
      name = "World"
  print(f"Hello, {name}!")
  comments = extract_todo_comments("test/test_todo.py")
  display_todo_comments(comments)

if __name__ == "__main__":
  main()
