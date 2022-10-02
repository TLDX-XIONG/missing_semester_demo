import sys

def rose():
    print('ROSE')

def default():
    print('hello')

def main():
    if sys.argv[1] == 'rose':
        rose()
    else:
        default()

if __name__ == '__main__':
    main()

