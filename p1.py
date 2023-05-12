def maxMul(a, b):
    if(b == 0):
        return 0;
    a = a - 1
    return a - (a % b) 

def sumMul(a, b):
    c = maxMul(a, b) // b
    return (c + 1) * c // 2 * b

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    print(sumMul(args.value, 3) + sumMul(args.value,5) - sumMul(args.value, 15))