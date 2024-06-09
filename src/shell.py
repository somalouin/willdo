from prompt_toolkit import PromptSession
from prompt_toolkit.styles import Style
from prompt_toolkit.shortcuts import set_title

# Define your custom style
style = Style.from_dict({
    'prompt': 'ansigreen bold',
    'input': 'ansiblue',
    'output': 'ansiyellow italic'
})

# Create a PromptSession
session = PromptSession()

def main():
    set_title("My Custom Shell")  # Set the terminal title
    while True:
        try:
            # Use your custom style for the prompt
            text = session.prompt('MyShell> ', style=style)
            if text == 'exit':
                break
            print(f'You entered: {text}')
        except KeyboardInterrupt:
            continue  # Ctrl+C pressed, continue to the next prompt
        except EOFError:
            break  # Ctrl+D pressed, exit the shell
    print('Goodbye!')

if __name__ == '__main__':
    main()
