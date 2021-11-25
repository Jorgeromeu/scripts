import os

for filename in os.listdir():
    name, ext = filename.split('.')

    if ext == 'wiki':
        os.rename(filename, f'{name}.md')
