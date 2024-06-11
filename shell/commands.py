import os

def ls():
  files = os.listdir('.')
  for file in files:
    print(f"- {file}")

def cat(file):
  with open(file, 'r') as f:
    print(f.read())