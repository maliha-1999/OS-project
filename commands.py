import os
import subprocess
import sys

def execute_command(command):
    parts = command.split()
    cmd = parts[0]
    args = parts[1:]

    if cmd == "exit":
        print("Exiting shell...")
        sys.exit(0)
    elif cmd == "cd":
        change_directory(args)
    elif cmd == "pwd":
        print(os.getcwd())
    elif cmd == "ls":
        list_directory(args)
    else:
        run_system_command(command)

def change_directory(args):
    if len(args) == 0:
        os.chdir(os.path.expanduser("~"))
    else:
        try:
            os.chdir(args[0])
        except FileNotFoundError:
            print(f"cd: no such file or directory: {args[0]}")
        except PermissionError:
            print(f"cd: permission denied: {args[0]}")
        except Exception as e:
            print(f"cd: {e}")

def list_directory(args):
    path = args[0] if len(args) > 0 else "."
    try:
        for entry in os.listdir(path):
            print(entry)
    except FileNotFoundError:
        print(f"ls: cannot access '{path}': No such file or directory")
    except PermissionError:
        print(f"ls: permission denied: '{path}'")
    except Exception as e:
        print(f"ls: {e}")

def run_system_command(command):
    try:
        result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        print(result.stdout.decode('utf-8'))
    except subprocess.CalledProcessError as e:
        print(e.stderr.decode('utf-8'))
    except Exception as e:
        print(f"Error executing command '{command}': {e}")
