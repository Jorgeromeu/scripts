import sys

valid_commands = ['step', 'break', 'next', 'quit', 'watch', 'help', 'info', 'run', 'indo']

input_cmd = sys.argv[1]

matches = filter(lambda cmd: cmd.startswith(input_cmd), valid_commands)

print(list(matches))
