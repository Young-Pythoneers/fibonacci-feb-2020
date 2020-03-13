import time
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from fibonaci import fibonacci_closed, fibonacci_loop, fibonacci_recursive


def timed_iterator(func):
    """Function that times each given Fibonacci function
     for every given index using the wrapper function defined inside this function below.

    Args:
      func (function): Function that calculates a Fibonacci number based on given index.

    Returns:
      wrapper: Contains a list per Fibonaci function with execution time for each index.
    """

    def wrapper(n):
        speed_list = []
        for i in range(n):
            start = time.time()
            func(i)
            stop = time.time()
            speed_list.append(stop - start)
        return speed_list

    return wrapper


def speed(n, file_path, func_list):
    """Function that uses the timed_iterator function to calculate the execution
    time for every given Fibonacci number index and then creates a Dataframe.

    Args:
      n (int): number which indicates up to which Fibonacci index all functions are timed.
      file_path (path): Store generated CSV file on the following path.
      func_list (list): List that contains all the Fibonacci functions that you want to test.

    Returns:
      True: If every functions is timed and CSV file is created
       return True.
    """

    speed_df = pd.DataFrame({})
    for func in func_list:
        timed_func = timed_iterator(func)
        speed_df[func.__name__] = timed_func(n)
    speed_df.to_csv(file_path, index=False)
    return True


def plot_results(df):
    """Function that plots the difference in execution speed
    for three different methods to calculate a Fibonacci number.

    Args:
      df (CSV file): A  CSV file that contains the execution speed in seconds for
       each method per index number (up to and including 200).

    Returns:
      A seaborn lineplot.
    """

    ax = sns.lineplot(data=df)
    ax.set(xlabel="Fibonacci index", ylabel="Time(sec)")

    return plt.show()


if __name__ == "__main__":
    file_path = Path("./speed_data.csv")
    speed(
        200, file_path, [fibonacci_closed, fibonacci_loop, fibonacci_recursive,],
    )
    df = pd.read_csv(file_path)
    plot_results(df)
