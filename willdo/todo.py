import os

ROOT_DIR = os.path.abspath(os.curdir)

def extract_todo_comments():
  todo_comments = {}
  for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
      file_path = os.path.join(root, file)
      if ".git" not in file_path and ".vscode" not in file_path and ".gitignore" not in file_path:
        with open(file_path, 'r') as file:
          print(f"[*] Reading file: {file_path}")
          for line_number, line in enumerate(file, start=1):
            if 'TODO' in line:
              if file_path not in todo_comments:
                todo_comments[file_path] = []
              todo_comments[file_path].append((line_number, line.strip()))
  return todo_comments

def display_todo_comments(todo_comments):
  for file_path, comments in todo_comments.items():
    print(f"File: {file_path}")
    for line_number, comment in comments:
      print(f"Line {line_number}: {comment}")