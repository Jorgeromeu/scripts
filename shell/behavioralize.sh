#!/bin/bash

# takes a truth table in pla format and uses espresso to optimize it.
# the output is formatted into behavioral VHDL. 
# ---
# requres "espresso" which can be downloaded from the AUR as "espresso-logic"

# $1 input file

espresso -o eqntott $1 | sed 's/!/not /g;s/!/not /g;s/&/ and /g;s/|/or/g;s/\=/<=/g' #| sed 's/\s*//g'
