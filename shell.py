import os
import subprocess
import sys
from commands import execute_command

def main():
    while True:
        try:
            current_directory = os.getcwd()
            command = input(f"{current_directory} $ ")
            if command.strip():
                execute_command(command.strip())
        except KeyboardInterrupt:
            print("\nUse 'exit' to quit the shell.")
        except EOFError:
            break

if __name__ == "__main__":
    main()
