import math

stand_calc = 1
discriminant = 2

print("Calculator: ", stand_calc, "\nDiscriminant: ", discriminant)
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
else:
    print("You entered a non-existent command -_-")
