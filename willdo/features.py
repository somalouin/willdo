from willdo.todolist import *

def list():
  todo_comments = search_file()
  display_todo_comments(todo_comments)

def export():
  todo_comments = search_file()
  export_to_markdown(todo_comments)