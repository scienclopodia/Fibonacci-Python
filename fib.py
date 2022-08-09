def fibonacci(len, singleNum=False):
    fib = []
    i = -1
    
    for x in range(len):
        if x == 0:
            fib.append(1)
        elif x == 1:
            fib.append(1)
        elif x == 2:
            fib.append(2)
        else:
            fib.append(fib[i] + fib[i - 1])
        i += 1
    
    if not singleNum:
        return fib
    else:
        return fib[i]

print(fibonacci(1000, True))
