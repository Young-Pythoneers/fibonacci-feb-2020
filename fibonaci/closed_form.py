import math
from functools import lru_cache
import time


def fibonacci_closed(n: int):
    phi = (1 + math.sqrt(5)) / 2
    return int(round((phi**n)/math.sqrt(5)))

def fibonacci_loop(n:int):
    if n <=1:
        return [0,1][n]
    else:
        min2 = 0
        min1 = 1
        for i in range(n-1):
            min1, min2 = min1+min2, min1
        return min1

def fibonacci_loop_n(n:int):
    fib = [0,1]
    if n < 2:
        return fib[0:n+1]
    else:
        for i in range(n-1):
            fib.append(fib[-1]+fib[-2])
        return fib

def fibonaci_loop_max(n:int):
    fib = [0,1]
    if n < 1:
        return fib[0:1]
    else:
        while True:
            num = fib[-1]+fib[-2]
            if num > n:
                break
            else:
                fib.append(num)
        return fib

@lru_cache(maxsize=4000000)
def fibonacci_recursive(n:int):
    '''https://codereview.stackexchange.com/questions/183231/python-3-fibonacci-implementation'''
    if n < 3:
        return [0,1,1][n]
    elif n % 2 == 0:
        m = n // 2
        return (fibonacci_recursive(m - 1) + fibonacci_recursive(m + 1)) * fibonacci_recursive(m)
    else:
        m = (n + 1) // 2
        return fibonacci_recursive(m) ** 2 + fibonacci_recursive(m-1) ** 2

#n = 200
for n in range(1000000,5000000,1000000):
    #print(fibonacci_closed(n))
    timer_start: float = time.time()
    fib_loop = fibonacci_loop(n)
    print(fib_loop)
    timer_stop = time.time()
    loop_time = timer_stop-timer_start
    print("fibonacci_loop(" + str(n) + ") took " + str(loop_time)+ " seconds.")

    timer_start = time.time()
    fib_rec = fibonacci_recursive(n)
    print(fib_rec)
    timer_stop = time.time()
    rec_time = timer_stop-timer_start
    print("fibonacci_recursive(" + str(n) + ") took " + str(rec_time)+ " seconds.")
    if fib_loop != fib_rec:
        print("aaaaaaaargh!")
        print(n)
        break