#!/bin/bash

# lists all of the available commands on a UNIX based system

echo $PATH | tr ':' '\n' | xargs -n 1 ls -1 | fzf
