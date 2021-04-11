#!/usr/bin/env python

from os import system, name
import sys
import time

def print_stack(s):
    print(' ', end='')
    for item in s:
        print(item, end=' ')

        
stack = sys.argv[1:]

while True:
    system('clear')
    print_stack(stack)
    op = input(" : ")

    if (op == ''):
        if (stack):
            stack.pop()
    else:
        stack.append(op)
