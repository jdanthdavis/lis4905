import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web

def get_requirements():
    print("\nProgram Requirements:\n"
            + "1. Automate data manipulation process.\n"
            + "2. Easily reproduce analysis on different datasets using similar format--saves time!\n"
            + "3. Import necessary libraries.\n"
            + "4. Research how to install any missing packages, if necessary.\n"
            + "5. Create at least three functions that are called by the program:\n"
            + "     a. main(): calls at least two other functions.\n"
            + "     b. get_requirements(): display the program requirements.\n"
            + "     c. data_analysis_2(): display the following data.\n")
    print("***DataFrame composed of three components: index, columns, and data. Data also known as values.***")

def get_analysis_2():
    df = pd.read_csv('animal_survey.csv')
    
    print("1. Print indexes:")
    df.index = pd.RangeIndex(start=0, stop=35549, step=1)
    print (df.index)

    print("2. Print columns:\n")
    print(df.columns)

    print("3. Print data frame:\n")
    print(df)

    print("4. Print type:")
    print(type(df))

    print("5. Print attribute data types--object type represents strings (e.g., M and F in sex):")
    print(df.dtypes)

    print("6. Print values (truncated list), in array format.")
    print(df.values)

    print("7. Print index of all DataFrame column names:")
    print(list(df))

    print("8. Print DataFrame info (i.e., summary, similar to 'describe tablename;' in MySQL")
    print(df.info(verbose=True))

    print("9. Print *only* number of DataFrame rows:")
    print(len(df))

    print("10. Print *only* number of DataFrame columns:")
    print(len(df.columns))

    print("11. Print number of DataFrame rows and columns:")
    print(df.shape)

    print("12. Print number of DataFrame elements (i.e., rows * columns")
    print(df.size)

    print("13. Display the first and last 5 species (Why NaN?):")
    print(df['spec_id'])

    print("14. Display all *unique* species:")
    print(df['spec_id'].unique())

    print("15. Display total number of species caught:")
    print(len(df))

    print("16. Display number of *unique* species caught:")
    print(len(df['spec_id'].unique()))

    print("17. Display the number of *unique* species, excluding species not identified:")
    print(df['spec_id'].nunique())

    print("18. Display summary statistics of animal weights--assign to variable, print variable:")
    d = pd.read_csv('animal_survey.csv')
    df = pd.DataFrame(d)
    print (df['weight'].describe())

    print("19. Display individual aggregate weight metrics (i.e., min, max, mean, std, count);")
    print(df.aggregate({"weight" : ['min', 'max', 'mean', 'std', 'count']}))

    print("20. Display mean weight, rounded to two decimal places:")
    print(df['weight'].mean().round(2))

    print("21. Groupby one column (sex), and dislay mean of only *one* specific column in group (weight):")
    print(df.groupby("sex")["weight"].mean())

    print("22. Display number of records per species:")
    print(df.groupby("spec_id")["rec_id"].count())

    print("23. Display number of records per specific species (PF):")
    print(int(df.spec_id.str.count("PF").sum()))

    print("24. Display bar chart of number of records per species, include legend:")
    df['spec_id'].value_counts().sort_index().plot.bar()
    plt.legend(['total per species'])
    plt.xlabel("spec_id")
    plt.show()

    print("25. Display bar char of how many unique species recorded from each location, excluding missing values, include legend:")
    df['loc_id'].value_counts().sort_index().plot.bar()
    plt.legend(['total unique species per location'])
    plt.xlabel("loc_id")
    plt.show()

def main():
    get_requirements()
    get_analysis_2()
if __name__ == "__main__":
    main()