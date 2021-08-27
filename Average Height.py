# We are going to write a program that calculates the average height from a list of heights.
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#Write your code below this row 👇
summ = 0
for height in student_heights:
  summ += height
  number_of_heights = n + 1
average = round(summ / number_of_heights)
print(average)


 




