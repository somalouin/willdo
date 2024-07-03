import os

ROOT_DIR = os.path.abspath(os.curdir)

def search_file(file_path=None):
    todo_comments = {}
    if not file_path:
        for root, dirs, files in os.walk(ROOT_DIR):
            for file in files:
                file_path = os.path.join(root, file)
                try:
                    todo_comments.update(extract_todo_comments(file_path))
                except Exception as e:
                    print(f"Error processing file {file_path}: {str(e)}")
    else:
        todo_comments = extract_todo_comments(file_path)
    return todo_comments
  
def extract_todo_comments(file_path, todo_comments={}):
    if ".git" not in file_path and ".vscode" not in file_path and ".gitignore" not in file_path and "README.md" not in file_path:
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                for line_number, line in enumerate(file, start=1):
                    if "# TODO:" in line:
                        if file_path not in todo_comments:
                            todo_comments[file_path] = []
                        todo_comments[file_path].append((line_number, line.strip()))
        except UnicodeDecodeError:
            try:
                with open(file_path, 'r', encoding='iso-8859-1') as file:
                    for line_number, line in enumerate(file, start=1):
                        if "# TODO:" in line:
                            if file_path not in todo_comments:
                                todo_comments[file_path] = []
                            todo_comments[file_path].append((line_number, line.strip()))
            except UnicodeDecodeError:
                print(f"Unable to read file: {file_path}")
    return todo_comments

def display_todo_comments(todo_comments):
  for file_path, comments in todo_comments.items():
    print(f"File: {file_path}")
    for line_number, comment in comments:
      print(f"-> {comment.split('TODO:')[1].strip()} (line {line_number})")

def export_to_markdown(todo_comments):
  with open("TODO.md", "w") as file:
    for file_path, comments in todo_comments.items():
      file.write(f"## File: {file_path}\n")
      for line_number, comment in comments:
        file.write(f"- [ ] {comment.split('TODO:')[1].strip()} (line {line_number})\n")
      file.write("\n")
      
