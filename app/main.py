import sys
import os
import shutil
import subprocess as subp
import shlex

# System and Quoting
def handle_system(cmdlst):
    cmd = cmdlst[0]

    if cmd == "exit":
        return "exit"

    elif cmd == "echo":
        print(" ".join(cmdlst[1:]))
        return True

    elif cmd == "type":
        if len(cmdlst) < 2:
            return True

        target = cmdlst[1]
        builtins = ("echo", "exit", "type", "pwd", "cd")

        if target in builtins:
            print(f"{target} is a shell builtin")
        else:
            path = shutil.which(target)
            if path:
                print(f"{target} is {path}")
            else:
                print(f"{target}: not found")

        return True

    return False


# Navigation Commands
def handle_navigation(cmdlst):
    cmd = cmdlst[0]

    if cmd == "pwd":
        print(os.getcwd())
        return True

    elif cmd == "cd":
        if len(cmdlst) < 2:
            return True

        path = cmdlst[1]

        if path == "~":
            path = os.path.expanduser("~")

        try:
            os.chdir(path)
        except (FileNotFoundError, NotADirectoryError):
            print(f"cd: {path}: No such file or directory")

        return True

    return False


def main():
    while True:
        sys.stdout.write("$ ")

        command = input()
        cmdlst = shlex.split(command)

        if not cmdlst:
            continue

        # system layer
        result = handle_system(cmdlst)
        if result == "exit":
            break
        if result:
            continue

        # navigation layer
        if handle_navigation(cmdlst):
            continue

        # external commands
        try:
            subp.run(cmdlst)
        except FileNotFoundError:
            print(f"{cmdlst[0]}: command not found")


if __name__ == "__main__":
    main()