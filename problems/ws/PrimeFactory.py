Max = 1000000

def get_all_prime(max):
    if(max > Max):
        return None
    result = [1 for i in range(max + 1)]
    half = int(max ** 0.5)    
    start = 2
    r = []
    while start <= half:
        c = start
        start = start + 1
        if(result[c] == 0):
            continue;
        r.append(c)
        n = c + c
        while n <= max:
            result[n] = 0
            n = n + c
    while start <= max:
        if(result[start] == 1):
            r.append(start)
        start = start + 1
    return r
     
    

    