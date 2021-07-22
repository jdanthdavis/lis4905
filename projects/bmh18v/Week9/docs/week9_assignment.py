import pandas as pd
import numpy as np
import pandas_datareader.data as web
import datetime
import matplotlib.pyplot as plt
import seaborn as sns


def get_requirements(): 
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
        + "\tb. Document solutions attempted.\n"
        + "8. Algorithms used (identify each): Logistic Regression, Random Forest, Decision Tree, Support Vector Machine:\n"
        print("***DataFrame composed of three components: index, columns, and data. Data also known as values.***"))


def data_manipulation():
    df=pd.read_csv('imdb-movie-data.csv')
   
    print("26. Frequency of all values (value_counts()) in a column (here, 'genre'), return last 10:\n")
    print(df['Genre'].value_counts().head(10))

    print("27. Relationships between continuous variables using .corr() method:\n"
        + "Position numbers: position correlation. Negative numbers: inversive correlation. 1.0 indicates perfect correlation.\n"
        + "Correlation of interest: votes and revenue_millions.\n")
    print(df.corr(method='pearson'))

    print("28. Conditional selections.\n"
        + "28a. Display oldest and newest release years for movies in dataset:")
    least_recent_date = df['Year'].min()
    most_recent_date = df['Year'].max()
    print("Oldest:", least_recent_date, "Newest", most_recent_date)
    print("\n28b. Filter by one director, return 3 records:\n")
    options = ['Clint Eastwood']
    df = df.loc[df['Director'].isin(options)]
    pd.set_option('max columns', None)
    print(df.head(3))
    print("\n28c. Filter by rating (>=8.0), return 3 records:\n")
    df=pd.read_csv('imdb-movie-data.csv')
    pd.set_option('max_columns', None)
    df = df.loc[df['Rating'] >= 8.0]
    print(df.head(3))
    print("\n28d. Filter by two directors (using 'or'). Logical operators | for 'or' and for 'and', return first 5 records")
    df=pd.read_csv('imdb-movie-data.csv')
    pd.set_option('max_columns', None)
    df = df.loc[df['Director']. == ('Clint Eastwood') | (df['Director']== 'James Gunn')]
    print(df.head(5))
    print("\n28e. Filter by same two directors using ('isin'), return first 5 records:")
    df=pd.read_csv('imdb-movie-data.csv')
    pd.set_option('max columns', None)
    filter = df["Director"].isin(['Clint Eastwood', 'James Dunn'])
    print(df[filter].head(5))
    print("\n28f. Filter by all movies released between 2005 and 2010, inclusive, having rating above 8.5:")
    df=pd.read_csv('imdb-movie-data.csv')
    pd.set_option('max_columns', None)
    df = df.loc[(df['Year'] >= 2005) & (df['Year'] <= 2010) & (df['Rating'] > 8.5)]
    print(df.head(5))
    print("\n28g. Filter by all movies released 2005 and 2010, inclusive, having rating above 8.0, and made above or equal to 25th percentile in revenue:")
    df=pd.read_csv('imdb-movie-data.csv')
    df = df.loc[(df['Year'] >= 2005) & (df['Year'] <= 2010) & (df['Rating'] > 8.0) & (df['Revenue (Millions)'] >= 25)]
    print(df)
    print("\n29. Create function, watch_rating(), returns \"yes\" or \"no\" based upon 8.5 or greater rating\n"
        + "Use Python's apply() function to pass \"rating\" attribute to function,"
        + "and assign return values to new attribute \"watch_movies,\" display first 10 rows.")
    df=pd.read_csv('imdb-movie-data.csv')
    pd.set_option('max_columns', None)
    def watch_rating(Rating):
        if Rating >= 8.5:
            return "Yes"
        elif Rating < 8.5:
            return "No"
    df['Rating'] = df['Rating'].apply(watch_rating) 
    print(df.head(10))

    print("\n30. Plotting Recommendations: Categorical variables: bar charts and box plots.\n")
        + "Continuous variables: Histograms, Scatterplots, Line graphs, and boxplots.\n"
        + "Create following plots: scatter, histogram, two boxplots. And one heatmap.\n"
        + "BE SURE to include your boxplot interpretations.\n")

        df.plot(kind='scatter', x='Rating', y='Revenue (Millions)')
        plt.show()
        df.plot(kind='hist', x='Rating', y='Runtime (Minutes)')
        plt.show()
        df=pd.read_csv('imdb-movie-data.csv')    

    


    def main():
        get_requirements()
        data_manipulation()

        main()