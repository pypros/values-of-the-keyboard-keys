#linux
import sys
import tty

def get_key_value():
    DATA_BUFFER_BUFFER = 3
    fd = sys.stdin.fileno()
    tty.setcbreak(fd)
    key = sys.stdin.read(DATA_BUFFER_BUFFER)
    return key

def get():
    while True:
        key_value = get_key_value()
        if key_value:
            break
    return key_value.encode()

def main():
    for i in range(0,4):
        print(get())

if __name__=='__main__':
        main()
