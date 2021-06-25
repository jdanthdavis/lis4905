import os
from keras.models import Sequential
from keras.layers import Dense
import tensorflow as tf
import pandas as pd

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
tf.compat.v1.logging.set_verbosity(tf.compat.v1.logging.ERROR)


# def get_requirements():
#     print("\nProgram Requirements:\n"
#         + "1. Build deep-learning model to detect diabetes possibility.\n"
#         + "2. Import necessary libraries.\n"
#         + "3. Research how to install any missing packages, if necessary.\n"
#         + "4. Create at least three functions that are called by the program:\n"
#         + "     a. main(): calls at least two other functions.\n"
#         + "     b. get_requirements(): displays the program requirements\n"
#         + "     c. data_analysis_2(): displays the following data.\n"
#         + "5. Create neural network model.\n"
#         + "     a. Define neural network.\n"
#         + "     b. Compile model.\n"
#         + "     c. Train model with data.\n"
#         + "     d. Evaluate model.\n"
#         + "     e. Make predicitons.\n"
#         + "6. Use pima-indians-diabetes.csv dataset.\n"
#         + "7.  When running program:\n"
#         + "     a. Document any issues.\n"
#         + "     b. Document solutions attempted.\n"
#         + "8. Provide pithy answers to the following questions:\n"
#         + "     a. What are deep learning and neural network models?\n"
#         + "     b. Advantages\n"
#         + "     c. Disadvantages\n"
#         + "     d. What are hidden layers?\n")
#     print("***DataFrame composed of three components: index, columns, and data. Data also known as values.***")

# def deep_learning():
df=pd.read_csv('pima-indians-diabetes2.csv', delimiter=',')

# print("1. Print indexes:")
# df.index = pd.RangeIndex(start=0, stop=768, step=1)
# print (df.index)

# print("\n2. Print columns:")
# print(df.columns)

# print("\n3. Print data frame:")
# print(df)

# print("\n4. Print type:")
# print(type(df))

# print("\n5. Print attribute data types--object type represents strings (e.g., M and F in sex):")
# print(df.dtypes)

# print("\n6. Print values (truncated list), in array format.")
# print(df.values)

# print("\n7. Print index of all DataFrame column names:")
# print(list(df))

# print("\n8. Print DataFrame info (i.e., summary, similar to 'describe tablename;' in MySQL")
# print(df.info(verbose=True))

# print("\n9. Print *only* number of DataFrame rows:")
# print(len(df))

# print("\n10. Print *only* number of DataFrame columns:")
# print(len(df.columns))

# print("\n11. Print number of DataFrame rows and columns:")
# print(df.shape)

# print("\n12. Print number of DataFrame elements (i.e., rows * columns)")
# print(df.size)

print("\n13. Split into input (x) and output (y) variables: Indicate how x/y variables are split.")
x = df.iloc[:,0:8]
y = df.iloc[:,8]

print("\n\ta. Display input (x) variables:")
print(x)

print("\n\tb. Display output (y) variable (class): diabetic (1), non-diabetic (0):")
print(y)

print("\n14. Define, compile, fit, and evalute keras model on dataset:")
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
model.fit(x, y, epochs=100, batch_size=10, verbose=0)

_, accuracy = model.evaluate(x, y, verbose=0)
print('Accuracy: %.2f' % (accuracy * 100))

predictions = model.predict_classes(x)

for i in range(x):
    shift = x.iloc[i]
    print("%s=>%d(expected %d)"% (x[i].tolist(), predictions[i], y[i]))

# def main():
#     get_requirements()
#     deep_learning()
# if __name__ == "__main__":
#     main()