from willdo.todo import *

def list(path=None):
  if path and os.path.isfile(path):
    display_todos(process_files(path))
  else:
    display_todos(process_files())
  

def export(path=None):
  if path and os.path.isfile(path):
    export_to_markdown(process_files(path))
  else:
    export_to_markdown(process_files())