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
    counth = 0
    countl = 0
    listing = []
    with open(argv[1], "r") as r:
        with open(argv[2], "w+") as w:
            for line in r.readlines():
                for char in line:
                    if char == "#": counth += 1

                if line[0] == "#":
                    w.write("<h"+str(counth)+">"+ line[counth+1:-1] +"</h"+str(counth)+">\n")
                if line[0] == "-":
                    listing.append(line[2:-1])
                    countl = 1
                counth = 0
    if(countl): 
        list(listing)


def list(listing):
    with open(argv[1], "r") as r:
        with open(argv[2], "a") as w:
            for line in r.readlines():
                if line[0] == "-":
                    w.write("<ul>\n")
                    for l in listing:
                        w.write("<li>"+ l +"</li>\n")
                    w.write("</ul>\n")
                    break

if __name__ == "__main__":
    if checker():
        exit(1)
    converter()
    exit(0)
