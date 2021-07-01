import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from sklearn import preprocessing
from sklearn.feature_selection import SelectKBest, chi2
from scipy import stats
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn import svm


def get_requirements():
    print("\nProgram Requirements:\n"
        + "1. Build machine learning model.\n"
        + "2. Predict if it will rain tomorrow (yes/no) by analyzing past data.\n"
        + "3. Import necessary libraries.\n"
        + "4. Research how to install any missing packages, if necessary.\n"
        + "5. Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays the program requirements.\n"
        + "\tc. data_analysis_2(): displays the following data.\n"
        + "6. Data set url (do *not* use downloaded file): https://rattle.togaware.com/weatherAUS.csv\n"
        + "7. When running program:\n"
        + "\ta. Document any issues"
        + "\tb. Document solutions attempted.\n"
        + "8. Algorithms used (identify each): Logistic Regression, Random Forest, Decision Tree, Support Vector Machine:\n"
        + "\ta. Advantages\n"
        + "\tb. Disadvantages\n"
        + "\tc. How did each compare?\n")
    print("***Dataframe composed of three components: index, columns, and data. Data also known as values.***")

    def data_analysis_2():
    df = pd.read_csv('https://rattle.togaware.com/weatherAUS.csv')
    print("1. Print indexes: ")
    df.index = pd.RangeIndex(start=0, stop=192918, step=1)
    print(df.index) 

    print("2. Print columns:\n ")
    print(df.columns)

    print("3. Print data frame:\n ")
    print(df)

    print("\n4. Print type:")
    print(type(df))

    print("\n5. Print attribute data types--object type represents strings (e.g., M and F in sex):")
    print(df.dtypes)

    print("\n6. Print values (truncated list), in array format.")
    print(df.values)

    print("\n7. Print index of all dataframe column names:")
    print(list(df))

    print("\n8. Print dataframe info (i.e., summary, similar to 'describe tablename; in MySQL")
    print(df.info(verbose=True))

    print("\n9. Print *only* number of dataframe rows:")
    print(len(df))

    print("\n10. Print *only* number of dataframe columns:")
    print(len(df.columns))

    print("\n11. Print number of dataframe rows and columns:")
    print(df.shape)

    print("\n12. Print number of dataframe elements (i.e., rows * columns")
    print(df.size)

    print("\n13. Find null values (based upon number of records returned):")
    print(df.count().sort_values())

    print("\n14. Find null values (based upon number of records returned):")
    print(df.count().sort_values())

    # Note: RainTomorrow is target variable (yes/no)
    print("\n15. Cleaning Data--drop following attributes (notes in comments):\n"
          + "Sunshine, Evaporation, Cloud3pm, Cloud9am (contain less than 60% data)\n"
          + "Also, no need for Location, Date, or RISK_MM (not considering amount of rain)")
    # axis=1, or, axis='columns', column-wise operation for each row
    df = df.drop(columns=['Sunshine', 'Evaporation',
                          'Cloud3pm', 'Cloud9am', 'Location', 'Date', 'RISK_MM'], axis=1)

    print("\n16. Print *new* number of DataFrame rows and columns (predictor variables:)")
    print(df.shape)

    print("\n17. Remove null values in df--then, print number of DataFrame rows and columns:")
    df = df.dropna(how='any')
    print(df.shape)

    print("\n18. Remove outliers--using Z-score (research: \"What is Z-score?\"):")
    z = np.abs(stats.zscore(df.select_dtypes(include=np.number)))
    df = df[(z < 3).all(axis=1)]

    print("\n19. Print *new* number of DataFrame rows and columns:")
    print(df.shape)

    print("\n20. Modify categorical columns (yes=1, no=0):")
    print("Before modification:")
    print(df['RainToday'])

    df['RainToday'].replace({'No': 0, 'Yes':1}, inplace=True)
    df['RainTomorrow'].replace({'No': 0, 'Yes':1}, inplace=True)
    print("After modification:")
    print(df['RainToday'])

    print("\n21. Print unique categorical column values (for each column):")
    categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
    for col in categorical_columns:
        print(np.unique(df[col]))

    print("\n22. Convert categorical column (character) values into dummy/indicator (integer) values:")
    df = pd.get_dummies(df, columns=categorical_columns)
    print("Before normalizing data:")
    print(df.iloc[4:9])

    print("\n23. Normalize input variables to eliminate biases (differences in values used for each category:")
    scaler = preprocessing.MinMaxScaler()
    scaler.fit(df)
    df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
    print("After normalizing data:")
    print(df.iloc[4:9])

    print("\n24. Exploratory data analysis--identify most significant variables that will help predict:")
    x = df.loc[:, df.columns != 'RainTomorrow']
    y = df[['RainTomorrow']]
    selector = SelectKBest(chi2, k=3)
    selector.fit(x,y)
    x_new = selector.transform(x)
    print(x.columns[selector.get_support(indices=True)])

    df = df[['Humidity3pm', 'Rainfall', 'RainToday', 'RainTomorrow']]
    x = df[['Humidity3pm']]
    y = df[['RainTomorrow']]

    print("\n25. Begin data modeling--comparing algorithms (Note: clf_indicates \"classifier\"):")
    print("Logistic Regression:")
    t0= time.time()
    x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=0.25)
    clf_logreg = LogisticRegression(random_state=0)
    clf_logreg.fit(x_train, y_train.values.ravel())
    
    y_pred = clf_logreg.predict(x_test)
    score = accuracy_score(y_test,y_pred)

    print("Accuracy using Logistic Regression (percentage): ", score)
    print("Time taken using Logistic Regression (seconds): ", time.time() - t0)
    print("\nRandom Forest:")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)
    clf_rf = RandomForestClassifier(
        n_estimators=100, max_depth=4, random_state=0)
    # End random forest

    # Begin decision tree
    print("\nDecision Tree:")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)
    clf_dt = DecisionTreeClassifier(random_state=0)
    clf_dt.fit(x_train, y_train.values.ravel())
    y_pred = clf_dt.predict(x_test)
    score = accuracy_score(y_test, y_pred)

    print("Accuracy using Decision Tree Classifier (percentage): ", score)
    print("Time taken using Decision Tree Classifier (seconds): ", time.time() - t0)

    # Begin support vector machine
    print("\nSupport Vector Machine:")
    t0 = time.time()
    x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.25)
    clf_svc = svm.SVC(kernel='linear')
    clf_svc.fit(x_train, y_train.values.ravel())
    y_pred = clf_svc.predict(x_test)
    score = accuracy_score(y_test, y_pred)

    print("Accuracy using Support Vector Machine Classifier (percentage): ", score)
    print("Time taken using Support Vector Machine Classifier (seconds): ", time.time() - t0)

    # End support vector machine

    def main():
        get_requirements()
        data_analysis_2()

        main()
