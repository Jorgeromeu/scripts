#!/bin/bash

# the script I use to start tmux autoatically when I open a terminal
# The script checks if a session called "main" exists. If so attach to it, else create it and then attach
# To automatically run the script you can launch the terminal emulator with the script by using:

# alacritty -e tstart

# where alacritty can be replaced with the name of the terminal emulator you use

session="main"

# check if the session exists
tmux has-session -t $session 2>/dev/null

# if the previous command's exit status was not zero (success) 
# create a new session called main
if [ $? != 0 ]; then
    tmux new -s $session
fi

# attach to main
tmux attach -t $session
