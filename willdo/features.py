from todo import *

def execute(parameter, path):
  if parameter == "-t":
    todo_comments = extract_todo_comments(path)
    display_todo_comments(todo_comments)