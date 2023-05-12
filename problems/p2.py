def handle(max):
    p1 = 1
    p2 = 2
    sum = 2
    current = 0
    while True:
        current = p1 + p2 
        p1 = p2 
        p2 = current
        if(current > max):
            break;
        if(current % 2 == 0):
            sum = sum + current
    return sum

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    print(handle(args.value))