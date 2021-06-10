import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
from pandas_datareader import data as web

start = dt.datetime(2010,1,1)
end = dt.datetime.now()

def get_requirements():
    print('''Program Requirements:
        1. Work with your team.
        2. Backward-engineer screenshot below.
        3. If errors, check missing installations (e.g., pandas_datareader, matplotlib pyplot and style).
        4. Research how to do any necessary installations, *only* if needed:
        5. Also, include at *least* three graphs (dates from Jan. 1st 2020 until now.)
        6. Create a different *style* of graph for each ofthe companies show below.
        7. Optional: Create at least three functions that are called by the program:
                a. main(): calls at least two other functions.
                b. get_requirements(): display the program requirements.
                c. data_analysis_1(): displays the following data.\n''')
    
def data_analysis_1():
    df = web.DataReader('DOGE-USD', 'yahoo', start, end)
    
    print('Print number of records:')
    print(len(df))
    print('\n')
    print('Print columns:')
    print('Index([High, Low, Open, Close, Volume, Adj Close], dtype=object)\n')
    print('Print data frame:\n')
    print('Note: pandas displays "max_rows" number of rows (default, first and last 5).')
    print('Other rows are truncated. Value can be changed--research how!\n')

    doge = [
    {
        'ticker': 'DOGE-USD',
        'name': 'DogeCoin'
    }
    ]

    apple = [
    {
        'ticker': 'AAPL',
        'name': 'Apple'
    }
    ]

    tesla = [
    {
        'ticker': 'TSLA',
        'name': 'Tesla'
    }
    ]

    for stock in doge:
        df = web.DataReader([stock['ticker']], 'yahoo', start, end)
        df = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]
        print(df.head())
        print('\n')
        print('Print first 8 rows:')
        print(df.head(8))
        print('\n')
        print('Print last 6 rows:')
        print(df.tail(6))

    for stock in doge:
        df = web.DataReader([stock['ticker']], 'yahoo', start, end)
        df[['High', 'Adj Close']].plot(label=stock['name'])
        plt.style.use('bmh')
        plt.legend()
        plt.xlabel('Date')
        plt.show()

    for stock in tesla:
        plt.style.use('seaborn-pastel')
        df = web.DataReader([stock['ticker']], 'yahoo', start, end)
        df[['High', 'Adj Close']].plot(label=stock['name'])
        plt.legend()
        plt.xlabel('Date')
        plt.show()

    for stock in apple:
        plt.style.use('dark_background')
        df = web.DataReader([stock['ticker']], 'yahoo', start, end)
        df[['High', 'Adj Close']].plot(label=stock['name'])
        plt.legend()
        plt.xlabel('Date')
        plt.show()

def main():
    get_requirements()
    data_analysis_1()

if __name__ == "__main__":
    main()