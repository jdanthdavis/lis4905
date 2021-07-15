import numpy as np
import pandas as pd
import pandas_datareader.data as web

def get_requirements():
    print("\nProgram Requirements:\n"
        + "1. Data Cleaning and Manipulation.\n"
        + "2. Import necessary libraries.\n"
        + "3. Research how to install any missing packages, if necessary.\n"
        + "4. Create at least three functions that are called by the program:\n"
        + "     a. main(): calls at least two other functions.\n"
        + "     b. get_requirements(): displays the program requirements\n"
        + "     c. data_manipulation(): displays the following data.\n"
        + "5. Use imdb-movie-data.csv dataset.\n"
        + "6.  When running program:\n"
        + "     a. Document any issues.\n"
        + "     b. Document solutions attempted.\n"
        + "8. Algorithms used (identify each): Logistic Regression, Random Forest, Decision TRee, Support Vector Machine:\n")
    print("***DataFrame composed of three components: index, columns, and data. Data also known as values.***")

def data_manipulation():
    df = pd.read_csv('imdb-movie-data.csv')

    print("1. Print Index:")
    print(df.index)

    print("2. Print Columns:\n")
    print(df.columns)

    print("3. Print Dataframe:\n")
    print(df)

    print("4. Print type:\n")
    print(type(df))

    print("5. Print attribute data types:\n")
    print(df.dtypes)

    print("6. Print values (truncated list), in array format:\n")
    print(df.values)

    print("7. Print first 5 records in non-array format:\n")
    print(df.columns)

    print("8. Print index of all Dataframe column names:\n")
    print(df.columns)

    print("9. Print Dataframe info(i.e summary, similar to 'describe tablename;' in MySQL ): \n")
    print(df.describe)

    print("10. Print *only* number of Dataframe rows: \n")
    print(df.shape[0])

    print("11. Print *only* number of DataFrame columns:\n")
    print(df.shape[1])

    print("12. Print number of DataFrame rows and columns:\n")
    print(df.shape)

    print("13. Print number of Dataframe elements:\n")
    print(df.shape[0] * df.shape[1])

    print("14. Series: one-dimensional labeled array, can hold disparate data types (e.g., integer, string, float, Boolean, Python objects, etc.):\n")
    ser = pd.Series([1,'Hello World', 3.5, True, 6, {"banana", "cherry", "apple"}])
    print(ser)

    print("15. DataFrame: multi-dimensional table, essentially, two Series.\n Note: Various ways to create DataFrame.\n Here, create dictionary (key:value pairs), ordered (since 3.7), mutable, and does not allow duplicate. \n Then, pass it to pandas DataFrame constructor (Note: indexes automatically provided.)\n")
    dic = {'vegetables': [3,2,0,1,5,4,7,6],'fruits':[0,3,7,2,1,6,4,5]}
    df1 = pd.DataFrame(dic)
    print(df1)
    print('Then, add customer names as indexes:\n')
    index = ['Bob','Jane','Joe','Peter','Viola','Thomas','Raquel','Nicole']
    df1 = pd.DataFrame(dic, index = index)
    print(df1)

    print("16. Locate customer's order by name:\n")
    print(df1.loc['Jane',:])

    print("17. Convert DataFrame to following file types: .csv and .json (save to same directory):\n")
    df1.to_csv('produce_list.csv')
    df1.to_json('produce_list.json')

    print("18. Create DataFrame for imdb-movie-data.csv, designate movie ***titles*** as index, and print 1st five records:\n")
    df = pd.read_csv('imdb-movie-data.csv')
    df = df.set_index('Title')
    print(df.head())

    print("19. Display last three records:\n")
    print(df.tail(3))

    print("20. Handling duplicates using append(). (Note: twice as many rows.)\n")
    df = df.append(df)
    print(df.shape)

    print("21. Cleaning duplicates using drop_duplicates():\n")
    df = df.drop_duplicates()
    print(df.shape)

    print("22. Cleaning column names using rename(), and list comprehension. \n Original column names:\n")
    print(df.columns)
    print("\t22a. Remove parentheses using rename():")
    df = df.rename(columns = {'Revenue (Millions)':" Revenue_millions"})
    print(df.columns)

    print("\t22b. Make column names lower case, manually using list assignment")
    columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
    df.columns = columns
    print(df.columns)

    print("\t22c. Make column names lower case using list comprehension and lower():")
    df.columns = [i.lower() for i in df.columns]
    print(df.columns)

    print("23. Working with missing (null) values: 1) remove, or 2) replace (imputation).\n")

    print("\tStep 1: Identify null cells:")
    print(df.isna())

    print("\tStep2: Count number of nulls in each column:")
    print(df.isna().sum())

    print("\t23a. NB: Remove nulls, *only* with small amount of missing data (<5%): \n Note: dropna() removes rows w/at least one null value, \n and returns new DataFrame, w/o affecting original. \n axis=0 (rows default), axis = 1 columns \n Where does \'axis\' come from? Remember: df.shape returns rows(0)/cols(1).")
    print(df.dropna(axis=0))
    print("\t23b. Remove nulls (columns):")
    print(df.dropna(axis=1))
    print("\t23c. Imputation: Replace missing values with guessed/estimated value. \n Use data and relationships among non-missing predictors to estimate missing values.\n One (simple) way: Apply central tendency values (i.e., mean, median, mode).")

    print("\tStep 1: Extract column with null values into variable, and print 1st 5 records: \n Note: \"Title\" index remains.")
    print(df["revenue_millions"].head())

    print("\tStep 2: Return mean value:")
    print(df["revenue_millions"].mean())

    print("\tStep 3: Impute mean value using fillna() and inplace=True, then print nulls. \n Remember: inplace=True affects original DataFrame.")
    df["revenue_millions"].fillna(df["revenue_millions"].mean(),inplace=True)
    print(df.isna().sum())

    print("24. Basic statistical analyses using describe(), summary of *continuous* variables. \n Understanding data values (e.g., continuous vs. categorical) assists when determining plot types.\n")
    print(df.describe())

    print("25. Basic statistical analyses using describe(), summary of *categorical* variable (here, only *one* attribute). \n Returns row count, unique count of categories, top category, and freq of top categor(y/ies).\n")
    print(df['genre'].describe())

def main():
    get_requirements()
    data_manipulation()
if __name__ == "__main__":
    main()