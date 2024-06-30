from willdo.todolist import *

def list():
  todo_comments = search_file()
  display_todo_comments(todo_comments)