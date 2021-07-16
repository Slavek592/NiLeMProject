#!/usr/bin/python3
import os
from Definitions import Runner
from Definitions import Scripter

print("Welcome, User!")
print("NiLeSh 'compiler' greets You!")
while True:
    command = str(input("Do you want to run a script from file, write a file, or to write it here?\n"
                        "file/here/write "))
    if command in ["f", "F", "file", "File", "h", "H", "here", "Here", "w", "W", "write", "Write"]:
        break
    else:
        print("Unknown command.")
if command in ["f", "F", "file", "File"]:
    while True:
        command = str(input("Input the name of Your file:\nname/exit "))
        if command in ["break", "Break", "stop", "Stop", "exit", "Exit", "quit", "Quit", "escape", "Escape"]:
            print("OK")
            break
        else:
            if os.path.isfile(command):
                Runner.run_from_file(command)
            elif os.path.isfile(command + ".nls"):
                Runner.run_from_file(command + ".nls")
            elif os.path.isfile(command + ".nilesh"):
                Runner.run_from_file(command + ".nilesh")
            elif os.path.isfile("NileshScripts/" + command):
                Runner.run_from_file("NileshScripts/" + command)
            elif os.path.isfile("NileshScripts/" + command + ".nls"):
                Runner.run_from_file("NileshScripts/" + command + ".nls")
            elif os.path.isfile("NileshScripts/" + command + ".nilesh"):
                Runner.run_from_file("NileshScripts/" + command + ".nilesh")
            else:
                print("It does not exist, I am sorry.")
elif command in ["w", "W", "write", "Write"]:
    Scripter.run_ide()
else:
    Runner.run_from_console()
print("Thank You for using NiLeSh and NiLeM!")
print("Goodbye!")
