#This program calculates the amount each person pays after adding tip.
print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_of_tip = float(input("What percentage of tip would you like to give? 10, 12, or 15? "))
number_of_people = float(input("How many people to split bill? "))
amount_after_tip = total_bill + (total_bill * (percentage_of_tip / 100))
each_person_pays = amount_after_tip / number_of_people
final_amount_each_pays=(round(each_person_pays,2))
print(f"Each person should pay: ${final_amount_each_pays}")
