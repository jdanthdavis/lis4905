import datetime
# import pandas as pd  # Pandas = “Python Data Analysis Library”
import pandas_datareader as pdr  # remote data access for pandas
import matplotlib.pyplot as plt
from matplotlib import style

# Pandas datareader: sub package that allows one to create a dataframe from various internet data sources:
# Yahoo! Finance, Google Finance, St.Louis FED (FRED), World Bank, Google Analytics, etc.
# https://pandas-datareader.readthedocs.io/en/latest/
# Starting in 0.19.0, pandas no longer supports pandas.io.data or pandas.io.wb.
# Must replace imports from pandas.io with those from pandas_datareader:
# https://pandas-datareader.readthedocs.io/en/latest/remote_data.html
# Ticker Symbol List: https://gretlcycu.files.wordpress.com/2013/08/quick-ticker-symbol-list.pdf


def get_requirements():
    print("Data Analysis 1")
    print("\nProgram Requirements:\n"
          + "1. Work with your team.\n"
          + "2. Backward-engineer screenshot below.\n"
          + "3. If errors, check missing installations (e.g., pandas_datareader, matplotlib pyplot and style).\n"
          + "4. Research how to do any necessary installations, *only* if needed:\n"
          + "5. Also, include at *least* three graphs (dates from Jan. 1st 2010 until now).\n"
          + "6. Create a different * style * of graph for each of the companies shown below.\n"
          + "7. Optional: Create at least three functions that are called by the program:\n"
          + "\ta. main(): calls at least two other functions.\n"
          + "\ta. get_requirements(): displays the program requirements.\n"
          + "\tc. data_analysis_1(): displays the following data.")


def data_analysis_1():
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()

    # Read data into Pandas DataFrame, implicitly created by DataReader
    # Find eBay, Microsoft, and Apple stock market symbols, and compare.
    # How did 2020 fare for all three? Any thoughts?
    # EBAY, MSFT, APPL
    df = pdr.DataReader("EBAY", "yahoo", start, end)
    df1 = pdr.DataReader("MSFT", "yahoo", start, end)
    df2 = pdr.DataReader("AAPL", "yahoo", start, end)

    print("\nPrint number of records: ")
    print(len(df))

    print("\nPrint columns: ")
    print(df.columns)

    # Demo this in class:
    # print("\nPrint data info: ")
    # print(df.info())

    print("\nPrint data frame: ")
    print("\nNote: pandas displays \"max_rows\" number of rows (default, first and last 5). \nOther rows are truncated. Value can be changed--research how! :)")
    # Note: for efficiency, only prints first and last 5 rows--not *all* records
    print(df)

    print("\nPrint first 8 rows:")
    # Note: "Date" is displayed lower than other columns as it is treated as an index
    print(df.head(8))  # head() Prints top 8 rows. Here, with 7 columns

    print("\nPrint last 6 rows:")
    print(df.tail(6))

    print("\nDisplay at *least* three graphs (dates from Jan. 1st 2010 until now).\n"
          + "Create a different *style* of graph for each of the following companies:\n")

    print("\nAvailable Matplotlib styles:")
    for styles in style.available:
        print(styles)

    print("\nExamples:")
    # Research what these styles do!
    # https://problemsolvingwithpython.com/06-Plotting-with-Matplotlib/06.13-Plot-Styles/
    # compare with...
    style.use('ggplot')
    # style.use('bmh')
    # style.use('dark_background')
    # style.use('fivethirtyeight')

    df['High'].plot()
    df['Adj Close'].plot()
    plt.title("eBay Stock - ggplot")
    plt.legend()
    plt.show()

    style.use('bmh')
    df1['High'].plot()
    df1['Adj Close'].plot()
    plt.title("Microsoft Stock - bmh")
    plt.legend()
    plt.show()

    style.use('dark_background')
    df2['High'].plot()
    df2['Adj Close'].plot()
    plt.title("Apple Stock - dark_background")
    plt.legend()
    plt.show()

# https://www.learndatasci.com/tutorials/python-finance-part-yahoo-finance-api-pandas-matplotlib/
# https://stackoverflow.com/questions/7744697/how-to-show-two-figures-using-matplotlib/47956978
