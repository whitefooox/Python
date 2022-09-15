x = "start"

while x != "x":
    number1 = int(input())
    x = input()
    if x == "+":
        print(number1 + int(input()))
    elif x == "-":
        print(number1 - int(input()))
    elif x == "*":
        print(number1 * int(input()))
    elif x == "/":
        number2 = int(input())
        if number2 != 0:
            print(number1 // number2)
    elif x == "%":
        number2 = int(input())
        if number2 != 0:
            print(number1 % number2)
    elif x == "!":
        if number1 >= 0:
            factorial = 1
            for i in range(2, number1 + 1):
                factorial *= i
            print(factorial)
    elif x == "x":
        print(number1)
