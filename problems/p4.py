def isPa(n):
    if(n < 0):
        return False
    elif(n < 10):
        return True
    elif(n < 100):
        return (n // 10) == (n % 10)
    elif(n < 1000):
        return (n // 100) == (n % 10)
    elif(n < 10000):
        a = n // 100
        b = n % 100
        c = b // 10
        d = b % 10
        return a == (d * 10 + c)
    elif(n < 100000):
        a = n // 1000
        b = n % 100
        c = b // 10
        d = b % 10
        return a == (d * 10 + c)      
    elif(n < 1000000):
        a = n // 1000
        b = n % 1000
        c = b // 100
        d = (b % 100) // 10
        e = b % 10
        return a == (e * 100 + d * 10 + c)     
    else:
        return False

def get_max(p):
    s = p ** 2 // 10 * 9
    max = 1
    c = p - 1
    n = s // c
    while(n <= c):
        t = s // n
        if(t < n):
            t = n
        while(t <= c):
            v = n * t
            if(isPa(v) and (v > max)):
                max = v
            t = t + 1
        n = n + 1
    return max 

import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter) 
    parser.add_argument('-v', dest='value', default=2, type=int, help='''value 2/3''')
    args = parser.parse_args()
    q = args.value
    if(q == 2 or q == 3):
        print(get_max(10 ** q))