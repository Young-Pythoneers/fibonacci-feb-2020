import pandas as pd
import time
import closed_form
import matplotlib.pyplot as plt
import seaborn as sns

def timed_iterator(func):
    def wrapper(n):
        speed_list = []
        for i in range(n):
            start = time.time()
            func(i)
            stop = time.time()
            speed_list.append(stop-start)
        return speed_list
    return wrapper

def speed(n, file_path, func_list):
    speed_df = pd.DataFrame({})
    for func in func_list:
        timed_func = timed_iterator(func)
        speed_df[func.__name__] = timed_func(n)
    speed_df.to_csv(file_path, index=False)

def plot_results(df):
    ax = sns.lineplot(data=df)
    plt.show()

if __name__ == '__main__':
    file_path = './speed_data.csv'
    speed(2000, file_path, [closed_form.fibonacci_closed,closed_form.fibonacci_loop, closed_form.fibonacci_recursive])
    df = pd.read_csv(file_path)
    print(df)
    plot_results(df)