from ws import(
    get_all_prime
)

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=10, type=int, help='''value''')
    args = parser.parse_args()
    q = args.value
    primes = get_all_prime(int(q ** 0.5))
    index = 0
    while index < len(primes):
        p = primes[index]
        index = index + 1
        if(q % p != 0):
            if((p ** 2) > q):
                break;
            continue;
        q = q // p
        while(q % p == 0):
            q = q // p
        if(q < p):
            q = p;
            break;
        if((p ** 2) > q):
            break;

    print(q)
        