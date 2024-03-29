#!/bin/bash

# this script takes the current clipboard contents (assumed to be a java file) and formats 
# it for easy pasting into weblab

xclip -selection c -o | sed 's/^package.*/package weblab;/' | sed '/^.*System.out.println(/d' | sed 's/    /  /g'| xclip -selection c

notify-send "ready to paste"
