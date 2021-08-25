#You are going to write a program which will select a random name from a list of names. The     person selected will have to pay for everybody's food bill.
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

#Write your code below this line 👇
number_of_names = len(names)
import random
person_selected = names[random.randrange(0,number_of_names)]

print(f"{person_selected} is going to pay.")



