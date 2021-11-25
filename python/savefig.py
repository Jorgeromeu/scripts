#!/usr/bin/env python3

import sys
import shutil
import uuid

# copy render into a directory and give it a uuid as name
# i use this to keep backups of all renders

# targetdir = sys.argv[1]
targetdir = '/home/jorge/renders'
rendername = f'{uuid.uuid4()}.png'
dst = f'{targetdir}/{rendername}'

shutil.copyfile('./render.png', dst)
