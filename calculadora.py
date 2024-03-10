def sum(num1, num2):
     return num1 + num2


def subtraction(num1, num2):
     return num1 - num2


def multiplication(num1, num2):
     return num1 * num2

def division(num1, num2):
     if num2 == 0:
         return "Error: Cannot divide by zero"
     else:
         return num1 / num2


def calculator():
     while True:
         print("\nSelect the operation you want to perform:")
         print("1. Sum")
         print("2. Subtraction")
         print("3. Multiplication")
         print("4. Division")
         print("5. Exit")

         option = input("\nEnter the number of the desired operation: ")

         if option == '5':
             print("Exiting calculator...")
             break

         num1 = float(input("Enter the first number: "))
         num2 = float(input("Enter the second number: "))

         if option == '1':
             print("The result of the addition is:", sum(num1, num2))
         elif option == '2':
             print("The result of the subtraction is:", subtraction(num1, num2))
         elif option == '3':
             print("The result of the multiplication is:", multiplication(num1, num2))
         elif option == '4':
             print("The result of division is:", division(num1, num2))
         else:
             print("Invalid option. Please select a valid option.")


calculator()