import os
import re
import argparse

# basic argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('dir')
args = parser.parse_args()

files = [os.path.join(dp, f) for dp, dn, fn in os.walk(os.path.expanduser(args.dir)) for f in fn]

for filename in files:
    # read the file
    og_txt = open(filename, 'r').read()

    # replace the text
    # fixed_txt = og_txt.replace('$$', '$')
    # fixed_txt = og_txt.replace('/assets/img/', 'jekyll-imgs/')
    fixed_txt = re.sub(r'^\$', '$$', og_txt)
    print(filename)

    # write
    open(filename, 'w').write(fixed_txt)



