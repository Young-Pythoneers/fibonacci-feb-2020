fibonacci_start = [0, 1]

def fibonaci_range(index):

    if index == 0:
        return 0
    elif index == 1:
        return 1

    else:
        for single_number in range(index-1):
            fibonacci_start.extend([fibonacci_start[-1] + fibonacci_start[-2]])
        return fibonacci_start[:-1]

fib = fibonaci_range(100)
print(fib)
