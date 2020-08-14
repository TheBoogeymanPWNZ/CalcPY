import math

stand_calc = 1
discriminant = 2
logarithm = 3

print("Calculator: ", stand_calc, "\nDiscriminant: ", discriminant, "\nLogarithm", logarithm)
operation = int(input("Select operation: "))

if operation == 1:
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    addition = 1
    subtract = 2
    multiplic = 3
    division = 4
    print("Addition: ", addition, "\nSubtraction: ", subtract, "\nMultiplication: ", multiplic, "\nDivision: ",
          division)
    act = int(input("Choose an action from the suggested: "))
    if act == 1:
        print(num_1 + num_2)
    elif act == 2:
        print(num_1 - num_2)
    elif act == 3:
        print(num_1 * num_2)
    elif act == 4:
        print(num_1 / num_2)
elif operation == 2:
    num_a = float(input("Enter value a = "))
    num_b = float(input("Enter value b = "))
    num_c = float(input("Enter value c = "))
    Dis = num_b * num_b - 4 * num_a * num_c
    if Dis > 0:
        x1 = (-num_b + math.sqrt(Dis)) / (2 * num_a)
        x2 = (-num_b - math.sqrt(Dis)) / (2 * num_a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif Dis == 0:
        x = -num_b / (2 * num_a)
        print("x = %.2f" % x)
    else:
        print("No Roots")
elif operation == 3:
    natur_log = 1
    decimal_Log = 2
    log_to_base = 3
    print("Select the type of logarithm")
    print("Natural logarithm", natur_log, "\nDecimal logarithm", decimal_Log, "\nlogarithm of b to base a", log_to_base)
    log = int(input("Select the type of logarithm: "))
    if log == 1:
        b = int(input("Enter number b: "))
        print(math.log(b))
    elif log == 2:
        b = int(input("Enter number b: "))
        print(math.log10(b))
    elif log == 3:
        a = int(input("Enter base a: "))
        b = int(input("Enter number b: "))
        print(math.log(b, a))
else:
    print("You entered a non-existent command -_-")
