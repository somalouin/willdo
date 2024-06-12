import os

def ls():
  files = os.listdir('.')
  for file in files:
    print(f"- {file}")

def cat(file):
  with open(file, 'r') as f:
    print(f.read())

def cd(new_dir):
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print(f'Directory not found: {new_dir}')
    except NotADirectoryError:
        print(f'Not a directory: {new_dir}')
    except PermissionError:
        print(f'Permission denied: {new_dir}')