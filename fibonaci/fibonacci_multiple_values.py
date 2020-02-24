def fibonacci_range(index : int):

    """

    This function is used to calculate the fibonacci range up to and including the given index

    Args:
        index (int): The index is used for calculating the fibonacci range up to and including that index

    Returns: A fibonacci range given the index

    """


    fibonacci_start = [0, 1]

    if index == 0:
        return [0]
    elif index == 1:
        return [0, 1]

    else:
        for single_number in range(index):
            fibonacci_start.extend([fibonacci_start[-1] + fibonacci_start[-2]])
        return fibonacci_start[:-1]

fib = fibonacci_range(20)
print(fib)
