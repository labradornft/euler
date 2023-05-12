from ws import(
    get_all_prime
)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    q = args.value
    primes = get_all_prime(q * 11)
    print(len(primes))
    print(primes[q - 1])