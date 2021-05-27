#!/usr/bin/env python3
print("\nUser Input :")
meal_cost = float(input("Cost of Meal: "))
tax_percent = float(input("Tax percent: "))
tip_percent = float(input("Tip percent: "))
people_num = int(input("Party number: "))
tax_amount = round(meal_cost * (tax_percent / 100), 2) # convert to percentage
due_amount = round(meal_cost + tax_amount, 2)
tip_amount = round((due_amount) * (tip_percent / 100), 2) # percentage of cost + tax
total = round(meal_cost + tax_amount + tip_amount, 2)
split = round(total / people_num, 2)
print("\nProgram Output:")
print("Subtotal:\t", "${0:,.2f}".format(meal_cost))  # subtotal
print("Tax:\t\t", "${0:,.2f}".format(tax_amount))
print("Amount Due:\t", "${0:,.2f}".format(due_amount))
print("Gratuity:\t", "${0:,.2f}".format(tip_amount))
print("Total:\t\t", "${0:,.2f}".format(total))
print("Split " + "(" + str(people_num) + "):\t", "${0:,.2f}".format(split))