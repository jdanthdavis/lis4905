#!/usr/bin/env python3
import pandas as pdr
#import numpy as np
def get_requirements():
    print("Data Manipulation")
    print("\nProgram Requirements:")
    print("1. Data Cleaning and Manipulation.")
    print("2. Import necessary libraries.")
    print("3. Research how to install any missing packages, if necessary.")
    print("4. Create at least three functions that are called by the program.")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the programs requirements.")
    print("\tc. data_manipulation(): displays the programs requirements.")
    print("5. Use imbd-movie-data.csv dataset.")
    print("6. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")
    print("\n***DataFram composed of three components: index, columns, and data. Data also known as values***")

def data_manipulation():
    my_path = r"C:\Users\Alex\lis4905_sum21\projects\ab16m\week8\imdb-movie-data.csv"
    df = pdr.read_csv(my_path)

    print("\n1. Print indexes:")
    print(df.index)

    print("\n2. Print columns: (Due to confidentiality, only attributes/features 'Time,' 'Amount,' and 'Class' available.")
    print(df.columns)

    print("\n3. Print data frame:")
    print(df)

    print("\n4. Print type:")
    print(type(df))

    print("\n5. Print attribute data types--object type represents strings:")
    print(df.dtypes)

    print("\n6. Print values (truncated list) in array format:")
    print(df.values)

    print("\n7. Print first 5 records, in non-array format:")
    print(df.head())

    print("\n8. Print index of all DataFrame columns names:")
    print(df.columns)

    print("\n9. Print DataFrame info (i.e., summary, similar to 'describe tablename;' in MySQL):")
    print(df.info())

    print("\n10. Print *only* number of DataFrame rows:")
    print(len(df))

    print("\n11. Print *only* number of DataFrame columns:")
    print(len(df.columns))

    print("\n12. Print number of DataFrame rows and columns:")
    print(df.shape)

    print("\n13. Print number of DataFrame elements (i.e., rows * columns):")
    print(df.size)

    print("\n14. Series: one-dimensional labeled array, can hold disparate date types")
    print("(e.g., integer, string, float, Boolean, Python objects, etc.):")
    my_list = [1, "Hello World", 3.5, True, 6, {"banana", "cherry", "apple"}]
    my_series = pdr.Series(my_list)
    print(my_series)

    print("\n15. DataFrame: multi-dimensional table, essentially, two Series.")
    print("Note: Various ways to create DataFrame.")
    print("Here, create dictionary (key:value pairs), ordered (since 3.7), mutable, and doesnot allow duplicates.")
    print("Then, pass it to pandas DataFrame constructor (Note: indexes automatically provided.):")
    vegetable = [3, 2, 0, 1, 5, 4, 7, 6]
    fruit = [0, 3, 7, 2, 1, 6, 4, 5]
    stuff = {"vegetables" : vegetable,
             "fruits" : fruit}
    names = ["Bob", "Jane", "Joe", "Peter", "Viola", "Thomas", "Raquel", "Nicole"]
    td_dataframe = pdr.DataFrame(data=stuff)
    print(td_dataframe)
    print("\nThen, add customer names as indexes:\n")
    td_dataframe2 = pdr.DataFrame(data=stuff, index=names)
    print(td_dataframe2)

    print("\nLocate customer's order by name:")
    print(td_dataframe2.loc["Jane"])

    print("\n17. Convert DataFrame to following file type: .csv and .json (save to same directory):")
    td_dataframe2.to_csv(path_or_buf=r"C:\Users\Alex\lis4905_sum21\projects\ab16m\week8\file.csv")
    td_dataframe2.to_json(path_or_buf=r"C:\Users\Alex\lis4905_sum21\projects\ab16m\week8\jfile.json")

    print("\n18. Create DataFrame for imdb-movie-data.csv, designate movie ***titles*** as index, and print 1st five records:")

    df.index = df["Title"]
    print(df)

    print("\n19. Display last three records:")
    print(df.tail(3))

    print("\n20. Handling duplicates using append(). (Note: Twice as many rows.):")
    df = df.append(df)
    print(df.shape)

    print("\n21. Cleaning duplicates using drop_duplicates():")
    df = df.drop_duplicates()
    print(df.shape)

    print("\n22. Cleaning column names using rename(), and list comprehension.")
    print("Original column names:")
    #df = pdr.read_csv(my_path)
    print(df.columns)
    print("\n22a. Remove parentheses using rename():")
    df = df.rename(columns={'Revenue (Millions)':"revenue_millions"})
    print(df.columns)
    print("\n22b. Make column names lower case, manually using list assignment")
    columns=['rank','title', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
    df.columns = columns
    print(df.columns)
    print("\n22c. Make column names lower case using list comprehension and lower():")
    df.columns = [i.lower() for i in df.columns]
    print(df.columns)
    print("23. Working with missing (null) values: 1) remove, or 2) replace (imputation).")
    print("\n\tStep 1: Identify null cells:")
    print(df.isna())
    print("\n\tStep2: Count number of nulls in each column:")
    print(df.isna().sum())
    print("\n\t23a. NB: Remove nulls, *only* with small amount of missing data (<5%): \n Note: dropna() removes rows w/at least one null value, \n and returns new DataFrame, w/o affecting original. \n axis=0 (rows default), axis = 1 columns \n Where does \'axis\' come from? Remember: df.shape returns rows(0)/cols(1).")
    print(df.dropna(axis=0))
    print("\t23b. Remove nulls (columns):")
    print(df.dropna(axis=1))
    print("\t23c. Imputation: Replace missing values with guessed/estimated value. \n Use data and relationships among non-missing predictors to estimate missing values.\n One (simple) way: Apply central tendency values (i.e., mean, median, mode).")
    print("\n\tStep 1: Extract column with null values into variable, and print 1st 5 records: \n Note: \"Title\" index remains.")
    print(df["revenue_millions"].head())
    print("\n\tStep 2: Return mean value:")
    print(df["revenue_millions"].mean())
    print("\n\tStep 3: Impute mean value using fillna() and inplace=True, then print nulls. \n Remember: inplace=True affects original DataFrame.")
    df["revenue_millions"].fillna(df["revenue_millions"].mean(),inplace=True)
    print(df.isna().sum())
    print("\n24. Basic statistical analyses using describe(), summary of *continuous* variables. \n Understanding data values (e.g., continuous vs. categorical) assists when determining plot types.")
    print(df.describe())
    print("\n25. Basic statistical analyses using describe(), summary of *categorical* variable (here, only *one* attribute). \n Returns row count, unique count of categories, top category, and freq of top categor(y/ies).")
    print(df['genre'].describe())


def main():
    get_requirements()
    data_manipulation()

if __name__ == "__main__":
    main()