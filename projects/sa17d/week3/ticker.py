# dev: Seb Angel-Riano
# course: LIS4905
# sum2021

print("\nProgram Requirements: \n"
 + "1. Work with your team. \n"
 + "2. Backwards engineer screenshot below.\n"
 + "3. If errors, check missing installs.\n" 
 + "4. If needed, research how to do any installs\n" 
 + "5. Include at *least* three graphs for each company\n"
 + "6. Create a different * style * of graphs  for each company shown below\n")
 
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

start = dt.datetime(2010, 1, 1)
end = dt.datetime.now()
df = web.DataReader('RACE', 'yahoo', start, end)
hmcf = web.DataReader('HMC', 'yahoo', start, end)
tmf = web.DataReader('TM', 'yahoo', start, end)
num = len(df)


print(f"\nPrint number of records: \n{num}")

print("\nPrint columns: \n")
print(df.columns)

print("\nPrint data frame: \n")
print(df)

print ("\nPrint first 8 rows.\n")
print(df.head(8))

print ("\nPrint last 6 rows.\n")
print(df.tail(6))

style.use('ggplot')
df['High'].plot()
df['Adj Close'].plot()
plt.title("Ferrari ($RACE)")
plt.legend()
plt.show()


style.use('dark_background')
tmf['High'].plot()
tmf['Adj Close'].plot()
plt.title("Toyota ($TM)")
plt.legend()
plt.show()

style.use('classic')
hmcf['High'].plot()
hmcf['Adj Close'].plot()
plt.title("Honda ($HMC)")
plt.legend()
plt.show()
