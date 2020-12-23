#!/usr/bin/python3
"""0. Start a scrip"""
from sys import argv, stderr, exit
from os import path

if __name__ == "__main__":
    if len(argv) <= 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        exit(1)

    if not path.exists(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        exit(1)
    exit(0)
