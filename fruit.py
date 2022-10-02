import sys

def banana():
    print("eating banana")

def lemon():
    print("love and memory")

def peach():
    print("missing peach")

def default():
    print('fruit')

def main():
    if sys.argv[1] == 'banana':
        banana()
    elif sys.argv[1] == 'lemon':
        lemon();
    elif sys.argv[1] == 'peach':
        peach()
    else:
        default()

if __name__ == '__main__':
    main()
        
