num1 = float(input("Enter first number: "))
sign = input("Enter the sign: ")
num2 = float(input("Enter second number: "))

if sign == "+":
    print(f"Result: {num1 + num2}")
elif sign == "-":
    print(f"Result: {num1 - num2}")
elif sign == "*":
    print(f"Result: {num1 * num2}")
elif sign == "/":
    print(f"Result: {num1 / num2}")
else:
    print("Only '+', '-', '*' and '/' are supported")