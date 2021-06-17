#This program finds out whether a year is a leap year or not.
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("leap year")
    else:
      print("not leap year")
  else:
      print("leap year")
else:
  print("not leap year")



