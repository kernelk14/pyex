#!/usr/bin/env python3

# PyEx: Make executables for Python3 files using bash scripts.
""" The goal is to get rid of using commands to execute files. We are able to execute Python files like an ordinary binary."""

import os
import sys
import subprocess

if __name__ == '__main__':
    path = os.path.abspath(".")
    ps = path.split("/")
    target_directory = ps[len(ps)-1]
    tg = ps[len(ps)-1]
    filepath = "$PREFIX/lib/pyex/"+tg
    print(filepath)
    print(tg)
    print(f"This is the directory right now: {len(ps)} => {ps}")
    print(f"And This is our target directory: {target_directory}")
    subprocess.run("echo $PREFIX", shell=True)
    if os.path.exists(filepath):
        print(f"You have the `{tg}` directory already.")
    else:
        subprocess.run("mkdir $PREFIX/lib/pyex/"+tg, shell=True)
    subprocess.run("cp main.py $PREFIX/lib/pyex/"+tg, shell=True)

