
from art import logo
from replit import clear

#calculator
#add
def add(n1, n2):
  return(n1 + n2)

#subtract
def subtract(n1, n2):
  return(n1 - n2)

#multiply
def multiply(n1, n2):
  return(n1 * n2)

#devide
def divide(n1, n2):
  return(n1 / n2)

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():

  print(logo)

  numb1 = float(input("What's the first number?: "))

  for symbol in operations:
    print(symbol)

  perform_calculation = True

  while perform_calculation:

    operation_symbol = input("Pick an operation symbol from the symbols above.")

    numb2 = float(input("What's the next number?: "))

    calculation_function = operations[operation_symbol]

    answer = calculation_function(numb1, numb2)

    print(f"{numb1} {operation_symbol} {numb2} = {answer}")

    keep_calculating = input(f"Type 'y' to continue calculating with {answer} or 'n' to start a new calcultaion:\n")

    if keep_calculating == "y":
      numb1 = answer
    else:
      perform_calculation = False
      clear()
      calculator()

calculator() 

