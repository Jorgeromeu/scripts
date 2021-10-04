#!/bin/bash

# Takes an absolute path to a desktop file:
# eg: /usr/share/applications/firefox.desktop

localpath=~/.local/share/applications/$(basename $1)

cp $1 $localpath
echo "NoDisplay=true" >> $localpath
