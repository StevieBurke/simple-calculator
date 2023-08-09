#  addition
def add(x,y):
    return x + y

# subtraction
def subtract(x,y):
    return x - y

# multiplication
def multiply(x,y):
    return x * y

# division
def divide(x,y):
    return x / y 

# exponents
def pow(m,n):
    return m ** n

print("select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Solve an exponent")

while True: 
    # input from user
    choice = input("Enter choice(1/2/3/4/5): ")

    #Check if choice is an option
    if choice in ('1','2','3','4','5'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a listed choice.")
            continue

        if choice =='1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))

        elif choice == '5':
            print(num1, "**",num2, "=", pow(num1,num2))

        # is there another calculation
        # break the while loop if the answer is no
        next_calculation = input("Do you have another calculation? (yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid Input")
        
                


