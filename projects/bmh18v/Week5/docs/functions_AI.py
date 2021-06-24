import numpy as np
import os
import tensorflow as tf
import pandas as pd
import pandas_datareader.data as pdr # remote access for pandas
import matplotlib.pyplot as plt
import pandas_datareader.data as reader
from sklearn.model_selection import train_test_split

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)




def get_requirements():
    print("Week 5 Project")
    print ("Developer: Bryan Humphries")
    print("\nProgram Requirements:\n"
        + "1. Automate data manipulation process.\n"
        + "2. Easily reproduce analysis on different datasets using similar format--saves time!.\n"
        + "3. Import necessary libraries.\n"
        + "4. Research how to do any necessary installations, if necessary.\n"
        + "5. Give short, cognet answers to the following questions (in *your* words):\n"
        + "\ta. What is AI?\n"
        + "\tb. What is machine language?\n"
        + "\tc. What is deep learning and neural networks?\n"
        + "\td. What is natural language processing (NLP)?\n"
        + "6. Research differences between TensorFlow and PyTorch:\n"
        + "\ta. What are they used for?\n"
        + "\tb. List differences\n"
        + "\tc. Why would you use one over the other?\n"
        + "7. Download .csv dataset\n"
        + "8. Optional: Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays the program requirements.\n"
        + "\tc. data_analysis_2(): displays the following data.\n"
        + "9. When running program:\n"
        + "\ta. Document any issues.\n"
        + "\tb. Document solutions attempted\n"
        + "\tc. How good was data model--compared to actual data (accuracy percentage)?")
    print("***Dataframe composed of three components: index, columns, and data. Data also known as values.***")


def data_analysis_3():
    df = pd.read_csv("pima-indians-diabetes.csv", skiprows=0)
    print("1. Print indexes: ")
    df.index = pd.RangeIndex(start=0, stop=768, step=1)
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

    print("\n13. Cleaning Data:")
    all_cols = ['num_preg', 'gluc_concentrate', 'blood_press', 'triceps', 'insulin', 'bmi', 'pedigree', 'age', 'class']

    cols_to_norm = ['num_preg', 'gluc_concentrate', 'blood_press', 'triceps', 'insulin', 'bmi', 'pedigree']
    df[cols_to_norm] = df[cols_to_norm].apply(lambda x: (x- x.min()) / (x.max() - x.min()))

    print ("\n14. Begin TensorFlow Analysis - create variables:")
    num_preg = tf.feature_column.numeric_column('num_preg')
    plasma_concentrate = tf.feature_column.numeric_column('gluc_concentrate')
    blood_press = tf.feature_column.numeric_column('blood_press')
    triceps = tf.feature_column.numeric_column('triceps')
    insulin = tf.feature_column.numeric_column('insulin')
    bmi = tf.feature_column.numeric_column('bmi')
    diabetes_pedigree = tf.feature_column.numeric_column('pedigree')
    age = tf.feature_column.numeric_column('age')

    print("\n5. Create (generic) categorical features (used for analysis):")
    assigned_group = tf.feature_column.categorical_column_with_vocabulary_list('Group', ['A', 'B', 'C','D'])
    df['age'].hist(bins=20)
    plt.legend(['diabetes occurrences per age group'])
    plt.show

    print("\n16. Combining features:")
    age_groups = tf.feature_column.bucketized_column(age, boundaries=[20,30,40,50,60,70,80])
    # combine all features
    feat_cols = [num_preg, plasma_concentrate, blood_press, triceps, insulin, bmi, diabetes_pedigree, age_groups]

    # splitting data
    x_data = df.drop('class', axis=1)
    labels = df['class']
    x_train, x_test, y_train, y_test = train_test_split(x_data, labels, test_size=0.33, random_state=101)

    # get same command from TensorFlow Version1 into Version2
    input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=x_train, y=y_train, batch_size=10, num_epochs=1000, shuffle=True)

    # Create model
    model = tf.estimator.LinearClassifier(feature_columns=feat_cols, n_classes=2)
    model.train(input_fn=input_func, steps=1000)

    # Prediction
    pred_input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=x_test, batch_size=10, num_epochs=1, shuffle=False)

    predictions = model.predict(pred_input_func)
    list(predictions)

    # how good was data model compared to actual data?
    eval_input_func = tf.compat.v1.estimator.inputs.pandas_input_fn(x=x_test, y=y_test, batch_size=10, num_epochs=1, shuffle=False)
    results=model.evaluate(eval_input_func)
    print(results)

    def main():
        get_requirements()
        data_analysis_3()

        main()