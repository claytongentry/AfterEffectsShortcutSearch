import sys
import tty
tty.setcbreak(sys.stdin) # Sets linebreak
while True:
    print ord(sys.stdin.read(1))
