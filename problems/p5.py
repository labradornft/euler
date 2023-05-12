from ws import(
    get_all_prime
)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    q = args.value
    primes = get_all_prime(q)
    v = 1
    index = 0
    while index < len(primes):
        n = primes[index]
        s = n
        while(s <= q):
            s = s * n
        v = v * s // n
        index = index + 1
    print(v)
    