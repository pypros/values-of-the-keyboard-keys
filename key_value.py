#linux
import sys
import tty
import termios

def get_key_value(data_buffer_sieze=3):
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        key_value = sys.stdin.read(data_buffer_sieze)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return key_value

def get():
    while True:
        key_value = get_key_value()
        if key_value:
            break
    return key_value.encode()

def main():
    for i in range(4):
        print(get())

if __name__=='__main__':
        main()
