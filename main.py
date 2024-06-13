from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import set_title
import os

style = Style.from_dict({
  'prompt': 'ansigreen bold',
  'input': 'ansiblue',
  'output': 'ansiyellow italic'
})

session = PromptSession()

def main():
  set_title("m-shell") 
  while True:
    try:
      text = session.prompt(f'{os.getcwd()} > ', style=style)
      if text == 'exit': # exit
          break
    except KeyboardInterrupt: # ctrl+c
      continue  
    except EOFError: # ctrl+d
      break

if __name__ == '__main__':
  main()
