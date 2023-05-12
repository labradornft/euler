import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    q = args.value
    s = 0
    p = 0
    d = 0 
    n = 1
    while(n <= q):
        s = s + n
        d = d + n + n - 1
        p = p + d
        n = n + 1
    s = s ** 2
    print(s, p, s - p)
    