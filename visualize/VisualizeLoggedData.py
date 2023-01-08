import pandas as pd
import matplotlib.pyplot as plt

def plot_graph():
    colnames = ['Datetime', 'Download', 'Upload']
    df = pd.read_csv('log.csv', names=colnames)
    df['Download'].plot()
    df['Upload'].plot()
    plt.legend(['Download', 'Upload'])
    plt.show()