#!/bin/bash

# lists all of the files in the $PATH variable, that is, all of the commands on the system

echo $PATH | tr ':' '\n' | xargs -n 1 ls -1 2> /dev/null
