import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)

def get_requirements():
    print("Deep Learning\n")
print("\nProgram Requirements:\n"
        + "1. Build deep-learning learning model to detect diabetes possibility.\n"
        + "2. Import necessary libraries.\n"
        + "3. Research how to install any missing packages, if necessary.\n"
        + "4. Create at least three functions that are called by the program:\n"
        + "\ta. main(): calls at least two other functions.\n"
        + "\tb. get_requirements(): displays the program requirements.\n"
        + "\tc. data_analysis_2(): displays the following data.\n"
        + "5. Create neural network model.\n"
        + "\ta. Define neural network.\n
        + "\tb. Compile model.\n"
        + "\tc. Train model with data.\n"
        + "\td. Evaluate model.\n"
        + "\te. Make predictions\n"
        + "6. Use pima-indians-diabetes.csv dataset."
        + "7. When running program:"
        + "\ta. Document any issues.\n"
        + "\tb. Document solutions attempted.\n"
        + "8. Provide pthy answers to the following questions:"
        + "\ta. What are deep learning and neural network models?\n"
        + "\tb. Advantages\n"
        + "\tc. Disadvantages\n"
        + "\td. What are hidden layers?\n")
        print("***Dataframe composed of three components: index, columns, and data. Data also known as values.***")


def deep_learning():
    df=pd.read_csv('pima-indians-diabetes2.csv', delimiter=',')
    print("1. Print indexes: ")
    df.index = pd.RangeIndex(start=0, stop=768, step=1)
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
    print(df.head())

    print("\n8. Print index of all dataframe column names:")
    print(list(df))

    print("\n9. Print dataframe info (i.e., summary, similar to 'describe tablename; in MySQL")
    print(df.info(verbose=True))

    print("\n10. Print *only* number of dataframe rows:")
    print(len(df))

    print("\n11. Print *only* number of dataframe columns:")
    print(len(df.columns))

    print("\n12. Print number of dataframe rows and columns:")
    print(df.shape)

    print("\n13. Print number of dataframe elements (i.e., rows * columns")
    print(df.size)

    print("\n14. Split into input(x) and output(y) variables. Indicate how x/y variables are split.")
    x = df.iloc[:, 0:8]
    y = df.iloc[:,8]

    print("\n\ta. Display input (x) variables:")
    print(x)

    print("\n\tb. Display output(y) variable (class): diabetic (1), nondiabetic(0):")
    print(y)

    print("\n15. Define, compile, fit and evauluate keras model on dataset:")
    model = Sequential()

    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    mode.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    model.fit(x,y, epochs=150, batch_size=10, verbose=0)

    _, accuracy= model.evaluate(x,y, verbose=0)
    print('Accuracy: %.2f' % (accuracy * 100))

    predictions = model.predict_classes(x)

    for i in range(1-10):
        print("%s=>%d(expected %d)"% (x[i].tolist(), predictions[i], y[i]))


def main():
        get_requirements()
        deep_learning()

        main()