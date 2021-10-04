#!/bin/bash

# calls dmenu on ps to get the pid of a process and cipies i to clipboard

ps -eo pid,cmd | tail -n +2 | dmenu | awk '{print $1}' | tr -d '\n' | xclip -selection clipboard


