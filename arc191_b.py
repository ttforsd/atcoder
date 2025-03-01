


def solver(x, k): 
    bits = [] 
    maxi = 1
    while  x > 0: 
        val = x & 1 
        if val  == 0: 
            maxi *= 2 
        bits.append(val)
        x >>= 1 
    if maxi < k: 
        return -1
    i = 0 
    k -= 1
    while k > 0: 
        while bits[i] != 0: 
            i += 1 
        
        bits[i] = k & 1 
        k >>= 1 
        i += 1
    res = 0 
    p = 1
    for bit in bits: 
        res += bit * p
        p *= 2 
    return res 
        
print(solver(99999, 9999999))

n = int(input())
for _ in range(n): 
    a, b = input().split(" ")
    a, b = int(a), int(b) 
    print(solver(a, b))