import os

def ls():
  files = os.listdir('.')
  for file in files:
    print(f"- {file}")

def cat(path):
    try:
        with open(path, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f'File not found: {path}')
    except PermissionError:
        print(f'Permission denied: {path}')
    except IsADirectoryError:
        print(f'{path} is a directory')

def cd(new_dir):
    try:
        os.chdir(new_dir)
    except FileNotFoundError:
        print(f'Directory not found: {new_dir}')
    except NotADirectoryError:
        print(f'Not a directory: {new_dir}')
    except PermissionError:
        print(f'Permission denied: {new_dir}')