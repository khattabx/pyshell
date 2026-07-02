import sys
import shutil


def main():
    while True:
        sys.stdout.write("$ ")

        command = input()

        if command == "exit":
            break

        elif command.startswith("echo "):
            print(command[5:])

        elif command.startswith("type "):
            cmd = command[5:]

            if cmd in ("echo", "exit", "type"):
                print(f"{cmd} is a shell builtin")
            else:
                path = shutil.which(cmd)

                if path:
                    print(f"{cmd} is {path}")
                else:
                    print(f"{cmd}: not found")

        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()