#!/usr/bin/env python3
import pandas as pdr
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense

def get_requirements():
    print("Deep Learning\n")
    print("Program Requirements:")
    print("1. Build deep-learning model to detect diabetes possibility.")
    print("2. Import necessary libraries.")
    print("3. Reasearch how to install any missing packages.")
    print("4. Create at least three functions that are called by the program:")
    print("\ta. main(): calls at least two other functions.")
    print("\tb. get_requirements(): displays the program requirements.")
    print("\tc. deep_learning(): displays the following data.")
    print("5. Create neural network model.")
    print("\ta. Define neural network.")
    print("\tb. Compile model.")
    print("\tc. Train model with data.")
    print("\td. Evaluate model.")
    print("\te. Make predictions.")
    print("6. Use pima-indians-diabetes.csv dataset.")
    print("7. When running program:")
    print("\ta. Document any issues.")
    print("\tb. Document solutions attempted.")
    print("8. Provide pithy answers to the following questions:")
    print("\ta. What are deep learning and neural network models?")
    print("\tb. Advantages")
    print("\tc. Disadvantages")
    print("\td. What are hidden layers?")

def deep_learning():
    my_file = r"C:\Users\Alex\lis4905_sum21\projects\\ab16m\week7\pima-indians-diabetes.csv"
    df = pdr.read_csv(my_file)
    
    print("\n***DataFrame composed of three components: index, columns, and data. Data also known as values.***")
    
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

    print("\n14. Split into input (x) and output (y) variables. Indicate how x/y varibales are split.")
    x = df.iloc[:, 0:8] 
    y = df.iloc[:,8]

    print("\n\ta. Display input (x) variables:")
    print(x)

    print("\n\tb. Display output (y) variable (class): diabetic (1), nondiabetic (0):")
    print(y)


    print("\n15. Define, compile, fit and evaluate keras model on dataset:")
    model = Sequential()

    model.add(Dense(12, input_dim=8, activation='relu'))
    model.add(Dense(8, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                    optimizer='adam', metrics=['accuracy'])

    model.fit(x,y, epochs=150, batch_size=10, verbose=0)

    _, accuracy = model.evaluate(x,y,verbose=0)
    print('Accuracy: %.2f' % (accuracy * 100))

    predictions = model.predict_classes(x)

    for i in range(1-10):
            print('%d  => %d (expected %d)' % (x[i].tolist(), predictions[i], y[i]))

def main():
    get_requirements()
    deep_learning()

if __name__ == "__main__":
    main()