#!/usr/bin/python3
"""0. Start a scrip"""
from sys import argv, stderr, exit
from os import path


def checker():
    if len(argv) <= 2:
        stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        return(1)

    if not path.exists(argv[1]):
        stderr.write("Missing {}\n".format(argv[1]))
        return(1)
    return(0)


def converter():
    count=0
    with open(argv[1], "r") as r:
        with open(argv[2], "w") as w:

            for line in r.readlines():
                for char in line:
                    if char == "#": count+=1
                    
                if line[0] == "#":
                    w.write("<h"+str(count)+">"+ line[count+1:-1] +"</h"+str(count)+">\n")
                count=0
    
    """count = 0
    with open(argv[1], "r") as r:
        with open(argv[2], "w") as w:
            for line in r.readlines():
                for x in line:
                    if x == "#":
                        count += 1
                if (count != 0):
                    w.write(
                        " <h{}> Heading level {}</h{}>\n".format(count, count, count))
                count = 0
"""

if __name__ == "__main__":
    if checker():
        exit(1)
    converter()
    exit(0)
