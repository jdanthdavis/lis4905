import random

def get_requirements():
    print("Create a Python program based upon the following requirements: ")
    print("1. Use ***all*** four intrinsic Python Data Structures: List, Tuple, Set, Dictionary"
        + "2. Randomly assign grades of \'S' or \'U' \n(satisfactory or unsatisfactory) to each DIS member.\n"
        + "3. Display code and results to your Bitbucket repo.\n")

def get_grades():
    names = [
        'Justin Davis', 
        'Philip Bowman',
        'Sebastian Angel-Riano', 
        'Alexander Boehm', 
        'Andrew Vargas', 
        'Rachel Hester', 
        'Mitchell Mujwit',
        'Bryan Humphreies']

    scores = ['S', 'U']

    print("Here are the grades in a List:")
    x = [(i,random.choice(scores)) for i in names]
    print(x)

    print("\nHere are the grades in a Tuple:")
    print(tuple(x))

    print("\nHere are the grades in a Set: ")
    s=set(x)
    print(s)

    print("\nHere are the grades in a Dictionary: ")
    tuple_as_dict = dict(tuple(x))

    print(tuple_as_dict)

get_requirements();
get_grades();