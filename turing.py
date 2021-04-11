#!/usr/bin/env python

from os import system, name
from colorama import Fore
import sys
import keyboard

def print_tape(s, pos):
    print(' ', end='')
    for (i, item) in enumerate(s):
        if (i == pos):
            print(Fore.BLUE + item, end=' ')
        else:
            print(Fore.RESET + item, end=' ')
    print(Fore.RESET)


tape = sys.argv[1:]
pos = 0

while True:

    system('clear')
    print_tape(tape, pos)
    op = input(" : ")

    if (op == 'r'):
        pos += 1
        if (pos > len(tape) - 1):
            tape.append('_')

    elif (op == 'l'):
        pos -= 1
        if (pos < 0):
            pos = 0

    else:
        tape[pos] = op
