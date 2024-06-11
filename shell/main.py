from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import set_title
from commands import *

style = Style.from_dict({
  'prompt': 'ansigreen bold',
  'input': 'ansiblue',
  'output': 'ansiyellow italic'
})

# Create a PromptSession
session = PromptSession()

def main():
  set_title("m-shell") 
  while True:
    try:
      text = session.prompt('[*] > ', style=style)
      if text == 'exit': # exit
          break
      if text == 'ls':  # ls
          list_files()
          continue
      print(f'You entered: {text}')
    except KeyboardInterrupt: # ctrl+c
      continue  
    except EOFError: # ctrl+d
      break

if __name__ == '__main__':
  main()
