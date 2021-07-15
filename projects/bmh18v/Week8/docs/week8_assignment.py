import pandas as pd


def get_requirements():
    print("Data Manipulation\n")
print("\nProgram Requirements:\n"
        + "1. Data Cleaing and Manipulation.\n"
        + "2. Import necessary libraries.\n"
        + "3. Research how to install any missing packages, if necessary.\n"
        + "4. Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays the program requirements.\n"
        + "\tc. data_manipulation(): displays the following data.\n"
        + "5. Use imdb-movie-data.csv dataset.\n"
        + "6. When running program:\n"
        + "\ta. Document any issues.\n"
        + "\tb. Document solutions attempted.\n")


def data_manipulation():
    df=pd.read_csv('imdb-movie-data.csv')
    print("1. Print index:")
    print(df.index) 

    print("2. Print columns: (Due to confidentiality, only attributes/features 'Time', 'Amount', and 'Class' available.)\n ")
    print(df.columns)

    print("3. Print data frame:\n ")
    print(df)

    print("\n4. Print type:")
    print(type(df))

    print("\n5. Print attribute data types--object type represents strings (e.g., M and F in sex):")
    print(df.dtypes)

    print("\n6. Print values (truncated list), in array format.")
    print(df.values)

    print("\n7. Print first 5 records, in non-array format:")
    print(df.columns)

    print("\n8. Print index of all dataframe column names:")
    print(list(df))

    print("\n9. Print dataframe info (i.e., summary, similar to 'describe tablename; in MySQL")
    print(df.describe)

    print("\n10. Print *only* number of dataframe rows:")
    print(df.shape[1])

    print("\n11. Print *only* number of dataframe columns:")
    print(df.shape)

    print("\n12. Print number of dataframe rows and columns:")
    print(df.shape)

    print("\n13. Print number of dataframe elements (i.e., rows * columns")
    print(df.shape[0] * df.shape[1])

    print("\n14. Series: one dimensional labeled array, can hold disparate data types (e.g., integer, strign, float, Boolean, Python objects, etc.):")
    ser = pd.Series([1, 'Hello World', 3.5, True, 6, {"banana", "cherry", "apple"}])

    print("\n15. DataFrame: multi-dimensiomnal table, essentially, two Series.\n Note: Various ways to create DataFrame.\n Here, create dictionary (key:value pairs), ordered (since 3.7), mutable, annd does not allow duplicate.")
    dic = {'vegetables': [3,2,0,1,5,4,7,6],'fruits':[0,3,7,2,1,6,4,5]}
    df1 = pd.DataFrame(dic)
    print(df1)
    print('Thenn, add customer names as indexes:')
    index = ['Bob', 'Jane', 'Joe', 'Peter', 'Viola', 'Thomas', 'Raquel', 'Nicole']
    df1= pd.DataFrame(dic, index=index)
    print(df1)

    print("\n16. Locate customer's order by name:")
    print(df1.loc['Jane',:])

    print("\n17. Convert DataFrame to following file types: .csv and .json (save to same directory):")
    df1.to_csv('produce_list.csv')
    df1.to_json('produce_list.json')

    print("\n18. Create DataFrame for imdb-movie-data.csv, designate movie ***titles*** as index, and print first five records:")
    df = pd.read_csv('imdb-movie-data.csv')
    df = df.set_index('Title')
    print(df.head())

    print("\n19. Display last three records:")
    print(df.tail(3))

    print("\n20. Handling duplicates using append(). (Note: twice as many rows.)")
    df = df.append(df)
    print(df.shape)

    print("\n21. Cleanign duplicates using drop_duplicates():")
    df = df.drop_duplicates()
    print(df.shape)

    print("\n22. Cleaning columns using rename(), and list comprehension.")
    print(df.columns)

    print("\n\t22a. Remove parentheses using rename():")
    df = df.rename(columns = {'Revenue (Millions)': " revenue_millions"})
    print(df.columns)

    print("\n\t22b. Make column names lower case, manually using list assignment")
    columns = ['rank', 'genre', 'description', 'director', 'actors', 'year', 'runtime', 'rating', 'votes', 'revenue_millions', 'metascore']
    df.columns = columns
    print(df.columns)

    print("\n\t22c. Make column names lower case using list comprehension and lower():")
    df.columns = [i.lower() for i in df.columns]
    print(df.columns)

    print("\n23. Working with missing (null) values: 1) remove, or 2) replace (imputation).")

    print("\tStep 1: Identify null cells:")
    print(df.isna())

    print("\tStep 2: Count number of nulls in each column:")
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

    print("\tStep 3: Impute mean value using fillna() and inplace=True, then print nulls. \nRemember: inplace=True affects original DataFrame.")
    df["revenue_millions"].fillna(df["revenue_millions"].mean(), inplace=True)
    print(df.insa().sum())

    print("\n24. Basic statistical analyses using describe(), summary of *continuous* variables. Understanding data values(e.g., continuous vs. categorial) assists when determining plot types.")
    print(df.describe())

    print("\n25. Basic statistical analyses using describe(), summary of *categorical* variable (here, only *one* attribute). Returns row count, unique count of categories, top category, and frequency of top category.")
    print(df['genre'].describe())

    def main():
        get_requirements()
        data_manipulation()

        main()