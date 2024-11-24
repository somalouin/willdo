from willdo.todo import *

ROOT_DIR = os.path.abspath(os.curdir)

def list(path=None):
  if path:
    display_todos(process_files(path))
  else:
    display_todos(process_files(ROOT_DIR))
  
def markdown(path=None):
  if path:
    export_to_markdown(process_files(path))
  else:
    export_to_markdown(process_files(ROOT_DIR))

def notion(path=None):
  if path:
    export_to_notion(process_files(path))
  else:
    export_to_notion(process_files(ROOT_DIR))