#!/bin/bash

# Takes a screenshot of the current window and adds a dropshadow to it
# Adapted from https://stefanscherer.github.io/how-to-take-screenshots-with-drop-shadow/

gnome-screenshot -w -f "$HOME/window.png"
convert "$HOME/window.png" -trim \( +clone -background grey25 -shadow 80x40+5+30 \) +swap -background transparent -layers merge +repage "$HOME/window.png"



