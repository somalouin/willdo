#!/usr/bin/env python3

import sys

def extract_todo_comments(file_path):
  todo_comments = []
  with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
      if 'TODO' in line:
        todo_comments.append((line_number, line.strip()))
  return todo_comments

def display_todo_comments(todo_comments):
  if not todo_comments:
    print("No TODO comments found.")
    return
  print("TODO comments found:")
  for line_number, comment in todo_comments:
    print(f"Line {line_number}: {comment}")

def main():
  if len(sys.argv) > 1:
      name = sys.argv[1]
  else:
      name = "World"
  print(f"Hello, {name}!")
  comments = extract_todo_comments("m-shell/__main__.py")
  display_todo_comments(comments)

if __name__ == "__main__":
  main()
