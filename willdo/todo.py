import re
import os

def extract_todos(file_path):
  todos = []
  with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, 1):
      if re.search(r'#\s*TODO', line, re.IGNORECASE):
        todos.append((line_number, line.strip(), file_path))
  return todos

def process_files(path):
  all_todos = []
  if os.path.isfile(path):
    all_todos.extend(extract_todos(path))
  elif os.path.isdir(path):
    for root, _, files in os.walk(path):
      for file in files:
        if file.endswith('.py'):
          file_path = os.path.join(root, file)
          all_todos.extend(extract_todos(file_path))
  return all_todos

def display_todos(todos):
  for line_number, todo, file_path in todos:
    print(f"-> {todo.split('TODO:')[1].strip()} (line {line_number}) in {file_path.split('/')[-1]}")
  print()

def export_to_markdown(todos):
  with open("todolist.md", "w") as file:
    file.write("# TODO List\n")
    for line_number, todo, file_path in todos:
      file.write(f"- [ ] {todo.split('TODO:')[1].strip()} (line {line_number}) in {file_path.split('/')[-1]}\n")
    file.write("\n")
      
