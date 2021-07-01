# dev: Seb Angel-Riano
# course: LIS4905
# sum2021

import pandas_datareader.data as pdr
import datetime

def get_requirements():
    print("Artificial Intelligence2")
    print("\nProgram Requirements:")
    print("1. Build machine learning model")
    print("2. Predict if it will rain tomorrow (yes/no) by analyzing past data")
    print("3. Import necessary libraries")
    print("4. Research how to install any missing packages, if necessary.")
    print("5. Create at least 3 functions called by the program.")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. artificial_intelligence_2(): displays the following data.")
    print("6. Data set url (do not use downloaded file): https://rattle.togaware.com/weatherAUS.csv%22")
    print("7. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")
    print("8. Algorithms used (identify each): Logistic Regression, Random Forest, Decision Tree. Support Vector Machine:")
    print("\ta. Advantages")
    print("\tb. Disadvantages")
    print("\tc. How did each compare?")
    print("DataFrame composed of three components: index, columns, and data. Data also known as values.")

df = pdr.DataReader('https://rattle.togaware.com/weatherAUS.csv')
x = len(df)
y = len(df.columns)


print("1. Print indexes")
print(df.index)

print("\n2. Print columns")
print(df.columns)

print("\n3. Print dataframe")
print(df)

print("\n4. Print type")
print(type(df))

print("\n5. Print attribute data types")
print(df.dtypes)

print("\n6. Print values, in array format")
print(df.values)

print("\n7. Print first 5 records, in non-array format")
XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

print("\n8. Print index of all DataFrame column names:")
print(df.columns)

print("\n9. Print DataFrame info")
df.info()

print("\n10. Print *only* number of DataFrame rows:")
print(len(df))

print("\n11. Print *only* number of DataFrame columns:")
print(len(df.columns))

print("\n12. Print number of DataFrame rows and columns:")
print(f"({x}, {y})")

print("\n13. Print number of DataFrame elements:")
print(df.size)

print("\n14. Find null values (based upon number of records returned): ")
print(df.count().sort_values())

print("\n15. Cleaning Data--drop following attribures (notes in comments):\n"
	+ "Sunshine, Evaporation, Cloud3pm, Cloud9am (contain less than 60% data)\n"
	+ "Also, no need for Location, Date, or RISK_MM (not considering amount of rain)")

df = df.drop(column=['Sunshine', 'Evaporation', 'Cloud3pm', 'Cloud9pm', 'Location', 'Date', 'RISK_MM'], axis=1)

print("\n16. Print *new* number of DataFrame rows and columns (predictor variables): ")
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

df['RainToday'].replace({'No':0, 'Yes':1}, inplace=True)
df['RainTomorrow'].replace({'No':0, 'Yes':1}, inplace=True)
print("After modification:")
print(df['RainToday'])

print("\n21. Print unique categorical column values (for each column):")
categorical_columns = ['WindGustDir', 'WindDir3pm', 'WindDir9am']
for col in categorical_columns:
    print(np.unique(df[col]))

print("\22. Convert categorical column (character) values into dummy/indicator (integer) values:")
df = pd.get_dummies(df, columns=categorical_columns)
print("Before normalizing data:")
print(df.iloc[4:9])

print("\n23. Normalize input variables to eliminate biases (differences in values used for each category.)")
scaler = preprocess.MinMaxScaler()
scaler = fit(df)
df = pd.DataFrame(scaler.transform(df), index=df.index, columns=df.columns)
print("After normalizing data:")
print(df.iloc[4:9])

print("\n24. Exploratory data analysis--identify most significant variables that will help predict ...")
x = df.loc[:, df.columns != 'RainTomorrow']
y = df[['RainTomorrow']]
selector = SelectKBest(chi2, k=3)
selector.fit(x, y)
x_new = selector.transform(x)

print(x.columns[selector.get_support(indicies=True)])

df = df[['Humidity3pm', 'Rainfall', 'RainToday', 'RainTomorrow']]
x = df[['Humidity3pm']]
y = df[['RainTomorrow']]

print("\n25. Begin data modelng--comparing algorithims")
print("Logistic Regression:")
t0 = time.time()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
clf_logreg = LogisticRegression(random_state=0)

clf_logreg.fit(x_train, y_train.values.ravel())

y_pred = clf_logreg.predict(x_test)
score = accuracy_score(y_test, y_pred)

print("Accuracy using Random Forest Classifier (percentage): ", score)
print("Time taken using Random Forest Classifier (seconds): ", time.time() - t0)

print("\nDecision Tree:")
t0 = time.time()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
clf_dt = DecisionTreeClassifier(random_state=0)
clf_dt.fit(x_train, y_train.values.ravel())
y_pred = clf_dt.predict(x_test)
score = accuracy_score(y_test, y_pred)
print("Accuracy using Decision Tree Classifier (percentage): ", score)
print("Time taken using Decision Tree Classifier (seconds): ", time.time() - t0)


print("\nSupport Vector Machine")
t0 = time.time()
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
clf_svc = svm.SVC(kernel='linear')
clf_svc.fit(x_train, y_train.values.ravel())\

y_pred = clf_svc.predict(x_test)
score = accuracy_score(y_test, y_pred)
print("Accuracy using Support Vector Machine Classifier (percentage): ", score)
print("Time taken using Support Vector Machine Classifier (seconds): ", time.time() - t0)