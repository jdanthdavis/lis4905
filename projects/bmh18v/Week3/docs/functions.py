import datetime
import pandas_datareader as pdr # remote access for pandas
import matplotlib.pyplot as plt
from matplotlib import style


def get_requirements():
    print("Data Anaylsis 1")
    print ("Developer: Bryan Humphries")
    print("\nProgram Requirements:\n"
        + "1. Work with your team.\n"
        + "2. Backward-engineer screenshot below.\n"
        + "3. If errors, check missing installations (e.g., pandas_datareader, matplotlib pyplot and style).\n"
        + "4. Research how to do any necessary installations, *only* if needed:\n"
        + "5. Also, include at *least* three graphs (dates from Jan. 1st 2010 until now).\n"
        + "6. Create a different *style* of graph for each of the companies shown below."
        + "7. Optional: Create at least three functions that are called by the program:"
        + "\ta. main(): calls at least two other functions."
        + "\tb. get_requirements(): displays the program requirements."
        + "\tc. data_analysis_1(): displays the following data.")


def data_analysis_1():
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()


    df = pdr.DataReader("GM", "yahoo", start, end)

    print("\nPrint number of records: ")
    print(len(df)) 

    print("Print columns: ")
    print(df.columns)

    print("\nPrint data frame: ")
    print(df)

    print("\nPrint first eight rows:")
    print(df.iloc[0:8])

    print("\nPrint last six rows:")
    print(df.tail(6))

    def displayGraph1():
        start = datetime.datetime(2010, 1, 1)
        end = datetime.datetime.now()
        df = pdr.DataReader("AAPL", "yahoo", start, end)
        style.use('ggplot')
        df['High'].plot()
        df['Adj Close'].plot()
        plt.title("Apple Stocks - ggplot")
        plt.legend()
        plt.show()

    def displayGraph2():
        start = datetime.datetime(2010, 1, 1)
        end = datetime.datetime.now()
        df = pdr.DataReader("GM", "yahoo", start, end)
        style.use('ggplot')
        df['High'].plot()
        df['Adj Close'].plot()
        plt.title("General Motors Stocks - classic")
        plt.legend()
        plt.show()

    def displayGraph3():
        start = datetime.datetime(2010, 1, 1)
        end = datetime.datetime.now()
        df = pdr.DataReader("AMC", "yahoo", start, end)
        style.use('ggplot')
        df['High'].plot()
        df['Adj Close'].plot()
        plt.title("AMC Stocks - seaborn-bright")
        plt.legend()
        plt.show()

    
    get_requirements()
    data_analysis_1()
    displayGraph1()
    displayGraph2()
    displayGraph3()