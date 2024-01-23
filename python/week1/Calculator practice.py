def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    try:
        return num1/num2
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed"

# try to use "try A ... except B " which is a efficient way to deal with error
# when try A is successful, except will be skiiped.

# This is a simple version
# def calculator():
   # print("Select an operation:")
   # print("1. Add")
   # print("2. Subtract")
   # print("3. Multiply")
   # print("4. Divide")

    # choice = input()

    # if choice == "1":
    # num1 = int(input("Enter number: "))
    # num2 = int(input("Enter number: "))
    # print(add(num1, num2))
    # if choice == "2":
    # num1 = int(input("Enter number:"))
    # num2 = int(input("Enter number:"))
    # print(subtract(num1, num2))
    # if choice == "3":
    # num1 = int(input("Enter number:"))
    # num2 = int(input("Enter number:"))
    # print(multiply(num1, num2))
    # if choice == "4":
    # num1 = int(input("Enter number:"))
    # num2 = int(input("Enter number:"))
    # print(divide(num1, num2))


def calculator():
    print("Pupil Calculator")
    print
    print("=================")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ["1", "2", "3", "4"]:
            # float can support decimal point
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
            elif choice == "2":
                result = subtract(num1, num2)
            elif choice == "3":
                result = multiply(num1, num2)
            elif choice == "4":
                result = divide(num1, num2)
            # \n add a newline # f-string is used for string
            print(f"Result: {result}\n")

        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")


calculator()
