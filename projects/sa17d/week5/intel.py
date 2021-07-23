# dev: Seb Angel-Riano
# course: LIS4905
# sum2021

import pandas as pdr
import datetime
import matplotlib.pyplot as plt
import pandas_datareader.data as web
import numpy as np
import tensorflow as tf

def program_requirements():
print("\nArtificial Intelligence")
print("\nProgram Requirements:")
print("\n1. Automate data manipulation process.")
print("\n2. Easily reproduce analysis on different datasets using similar format")
print("\n3. Import necessary libraries")
print("\n4. Research how to install any missing packages, if necessary")
print("\n5. Give short, cogent answers to the following questions:")
print("\ta. What is AI? Artificial Intellegence is adding computer automation at completing provided task.")
print("\tb. What is machine language? Machine language is a computer language, either 0's and 1's or a programming language that a computer uses to interpret information")
print("\tc. What is deep learning and neutral networks? Deep learning is a function of AI that replicates the 'thought process' of a humans' brain.")
print("\td. What is natural language processing (NLP)? Natural language processing is a part of AI that looks into how machines and computers would understand the language of humans.")
print("\n6. Research differences between TensorFlow and PyTorch:")
print("\ta. What are they used for? They are libraries used for machine learning")
print("\nb. list differences.")
print("\t- Static vs dynamic graph definition/n")
print("\t- Debugging/n")
print("\t- Visualization/n")
print("\t- Deployment/n")
print("\t- Data Parallelism/n")
print("\t- A framework vs library/n")
print("\nc. why would you use one over the other")
print("\t It seems that TensorFlow is far more established and is better for developing models for production and models th at need to ne deployed on mobile platforms where Pytoch seems to have a better debugger since it can use your normal python debugger")

print("\n***Data Frame composed of three components ")

df = pdr.read_csv("pima-indians-diabetes.csv")
x = len(df)
y = len(df.columns)

def artificial_intellegence():
print("\n1. Print indexes")
print(df.index)

print("\n2. Print columns: \n")
print(df.columns)

print("\n3. Print data frame: \n")
print(df)

print("\n4. Print type: \n")
print(type(df))

print("\n5. Print attribute data types: \n")
print(df.dtypes)

print("\n6. Print Values (truncated list), in array format: \n")
print(df.values)

print("\n7. Print index of all DataFrame column names: \n")
print(df.columns)

print("\n8. Print DataFrame info: \n")
df.info()

print("\n9. Print *only* number of Dataframe rows: ")
print(len(df))

print("\n10. Print *only* number of Dataframe columns:")
print(len(df.columns))

print("\n11. Print number of DataFrame rows and columns: ")
print(f"({x}, {y})")

print("\n12. Print number of DataFrame elements: ")
print(df.size)

print("\n13. Cleaning Data: ")
    all_cols = ['num_preg', 'gluc_concentrate', 'blood_press', 'triceps', 'insulin', 'bmi', 'pedigree', 'age', 'class' ]
    cols_to_norm = ['num_preg', 'gluc_concentrate', 'blood_press', 'triceps', 'insulin', 'bmi', 'pedigree']
    df[cols_to_norm] = df[cols_to_norm].apply( lambda x: (x - x.min()) / (x.min() - x.min()))

print("\n14. Begin TensorFlow Analysis - create variables:")
    num_preg = tf.feature_column.numeric_column('num_preg')
    plasma_gluc = tf.feature_column.numeric_column('gluc_concentrate')
    dias_press = = tf.feature_column.numeric_column('blood_press')
    tricep = tf.feature_column.numeric_column('triceps')
    insulin = tf.feature_column.numeric_column('insulin')
    bmi = tf.feature_column.numeric_column('bmi')
    diabetes_pedigree = tf.feature_column.numeric_column('pedigree')
    age = tf.feature_column.numeric_column('age')

rint("\n15. Create (generic) categorial features (used for analysis):")
    assigned_group = tf.feature_column.categorial_column_with_vocabulary_list(
        'Group', ['A', 'B', 'C', 'D'])
    df['age'].hist(bins=20)
    pdr.legend(['diabetes occurrences per age group'])
    pdr.show()

print("\n16. Combinging features:")
age_groups = tf.feature_column.bucketized_column(
    age, boundaries=[20,30,40,50,60,70,80])

# combine all features (using variables above)
feat_cols = [num_preg, plasma_gluc, dias_press, tricep, insulin, bmi, diabetes_pedigree, age_groups]

#splitting data (test_size=33%)
x_data = df.drop('class', axis=1)
labels = df['class']
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(
    x_data, labels, test_size=0.33, random_state=101)

