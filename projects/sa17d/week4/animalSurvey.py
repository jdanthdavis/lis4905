# dev: Seb Angel-Riano
# course: LIS4905
# sum2021

import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pdr
from pandas.core.frame import DataFrame
from pandas.core.indexing import IndexSlice
import pandas_datareader.data as web

print("\nProgram Requirements:")
print("\n1. Automate data manipulation process.")
print("\n2. Easily reproduce analysis on different datasets using similar formats - saves time.")
print("\n3. Import necessary libraries.")
print("\n4. Research how to install and missing packages, if necessary.")
print("\n5. Create at least three functions that are called by the program:")
print("\n\ta. main(): calls at least two other functions.")
print("\n\ta. get_requirements(): display the program requirements.")
print("\n\tb. data_analysis_2(): display the following data.")

animal_survey = pdr.read_csv("animal_survey.csv")
x = len(animal_survey)
y = len(animal_survey.columns)


print("\n1. Print Indexes: ")
print(animal_survey.index)

print("\n2. Print columns: \n.")
print(animal_survey.columns)

print("\n3. Print data frame: \n")
print(animal_survey)

print("\n4. Print type: \n")
print(type(animal_survey))

print("\n5. Print attribute data types: \n")
print(animal_survey.dtypes)

print("\n6. Print Values (truncated list), in array format: ")
print(animal_survey.values)

print("\n7. Print index of all dataframe column names: ")
print(animal_survey.columns)

print("\n8. Print DataFrame Info")
animal_survey.info

print("\n9. Print *only* number of DF rows")
print(len(animal_survey))

print("\n10. Print *only* number of DF columns")
print(animal_survey.columns)

print("\n11. Print number of DataFrame rows and columns:")
print(f"({x}, {y})")

print("\n12. Print number of dataframe elements")
print(animal_survey.size)

print("\n13. Print first and last 5 species")
print(animal_survey['spec_id'].head(5).append(animal_survey['spec_id'].tail(5)))

print("\n14. Print all *unique* species")
print(animal_survey.spec_id.unique())

print("\n15. Display number of species caught")
print(animal_survey['spec_id'].isna().count())

print("\n16. Display number of *unique* species caught")
print(len(animal_survey['spec_id'].unique()))

print("\n17. Display number of unqiue species caught, excluding species not identified")
print(animal_survey.spec_id.nunique())

print("\n18. Display summary statistics of animal weights")
print(animal_survey.weight.describe())

print("\n19. Display individual aggregate weight metrics")
print(animal_survey.aggregate({'weight': {'min','max','std','count'}}))

print("\n20. Display mean weight, rounded to two decimal ")
print(animal_survey.aggregate({'weight':['mean']}),round(2))

print("\n21. Group by one column (sex), and display mean of only *one* specific column in group (weight):")
print(animal_survey.groupby('sex')['weight'].mean())

print("\n22. Display number of records of species")
print(animal_survey.groupby('spec_id')['rec_id'].count())

print("\n23. Display number of records per species")
print(int(animal_survey.spec_id.str.count('PF').sum()))

print("\n24. Display bar charty of number of records per species, include legend")

animal_survey['spec_id'].value_counts().sort_index().plot.bar()
plt.xlabel('spec_id')
plt.legend(['total per species'])
plt.show()

print("\n25. Display bar char of how many unique species recorded from each location excluding missing value")
animal_survey['loc_id'].value_counts().sort_index().plot.bar()
plt.xlabel('loc_id')
plt.legend(['total unique species per location'])
plt.show()
