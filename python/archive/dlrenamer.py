import sys
import time
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler

path = sys.argv[1] if len(sys.argv) > 1 else '.'

observer = Observer()
observer.start()

observer.schedule(lambda: print('lol'), path, recursive=True)

for i in range()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
