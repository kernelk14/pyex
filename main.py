#!/usr/bin/env python3

# PyEx: Make executables for Python3 files using bash scripts.
""" The goal is to get rid of using commands to execute files. We are able to execute Python files like an ordinary binary."""

import os
import sys
import subprocess

if __name__ == '__main__':
    path = os.path.abspath(".")
    ps = path.split("/")
    target_directory = "ps[len(ps)-1]"
    print(f"This is the directory right now: {len(ps)} => {ps}")
    print(f"And This is our target directory: {target_directory}")
    with open("session.c", "w") as f:
        f.write("#include <stdio.h>\n")
        f.write("int main() {\n")
        f.write(f"int session = system(\"python3 main.py\");\n")
        f.write("}\n")
    os.system("gcc -o " + target_directory + ".1 session.c")
