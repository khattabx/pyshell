import sys
import os
import shutil
import subprocess as subp

def main():
    while True:
        sys.stdout.write("$ ")

        command = input()
        cmdlst = command.split()

        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            cmd = command[5:]
            bltincmd =  ("echo", "exit", "type", "pwd", "cd")
            if cmd in bltincmd:
                print(f"{cmd} is a shell builtin")
            else:
                path = shutil.which(cmd)

                if path:
                    print(f"{cmd} is {path}")
                else:
                    print(f"{cmd}: not found")

        elif command == "pwd":
            print(os.getcwd())

        elif cmdlst[0] == "cd":
            cdpath = cmdlst[1]
            truepath = os.path.exists(cdpath)
            if truepath == True :
                os.chdir(cdpath)
            else:
                print(f"cd: {cdpath}: No such file or directory")

        else:
            try:
                subp.run(cmdlst)
            except FileNotFoundError:
                print(f"{command}: command not found")


if __name__ == "__main__":
    main()