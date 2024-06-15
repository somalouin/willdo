import time
from blessed import Terminal

term = Terminal()

def display_custom_message():
    with term.cbreak(), term.hidden_cursor():
        print(term.clear)
        print(term.yellow('=================='))
        print(term.bold_red_on_black('welcome to m-shell'))
        print(term.yellow('=================='))
        for i in range(5, 0, -1):
            print(term.move_xy(0, 4) + term.cyan(f'{i}'), end='', flush=True)
            time.sleep(1)
        print(term.move_xy(0, 4) + term.clear_eol)
        print(term.magenta('bye bye'))

def main():
  display_custom_message()

if __name__ == '__main__':
  main()