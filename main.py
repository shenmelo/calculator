from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide,
}

def calculator():
  print(logo)
  
  num1 = float(input("What is your first number?: "))
  for symbol in operations:
    print(symbol)
  continue_calculating = True
  while continue_calculating:
    operation_symbol = input("Chose an operation: ")
    num2 = float(input("What is your second number?: "))
    calc = operations[operation_symbol]
    answer = calc(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer} ")
    
    should_continue = input(f"Type 'y' to continue calculating with {answer}, or 'n' to reset: ")
    if should_continue == 'y':
      num1 = answer
    elif should_continue == 'n':
      continue_calculating = False
      calculator()
    else:
      print("You enter an invalid inputs. Shutting down...")
      continue_calculating = False

calculator()