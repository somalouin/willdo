def extract_todo_comments(file_path):
  todo_comments = []
  with open(file_path, 'r') as file:
    for line_number, line in enumerate(file, start=1):
      if 'TODO' in line:
        todo_comments.append((line_number, line.strip()))
  return todo_comments

def display_todo_comments(todo_comments):
  if not todo_comments:
    print("> No TODO in file")
    return
  print("> TODO comments found:")
  for line_number, comment in todo_comments:
    print(f"Line {line_number}: {comment}")