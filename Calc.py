import math

constant_values = 1
stand_calc = 2
discriminant = 3
logarithm = 4
trigonometry = 5
exponent = 6


print("Constant: ", constant_values, "\nCalculator: ", stand_calc, "\nDiscriminant: ", discriminant, "\nLogarithm", logarithm, 
"\nTrigonometry", trigonometry, "\nExponent", exponent)
operation = int(input("Select operation: "))

if operation == 1:
    print('Speed of light in vacuum - c = 2,99792458⋅10^8 м·с^−1',
    '\n', "Planck's constant - h = 6,626 070 15⋅10^−34 Дж·с",
    '\n', 'Elementary charge - e = 1,602 176 634⋅10^−19 Кл',
    '\n', 'Boltzmann constant - k = 1,380 649⋅10^−23 Дж·К^−1',
    '\n', "Euler's number =", math.e,
    '\n', 'Pi =', math.pi)
elif operation == 2:
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
elif operation == 3:
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
elif operation == 4:
    natur_log = 1
    decimal_Log = 2
    log_to_base = 3
    print("Select the type of logarithm")
    print("Natural logarithm", natur_log, "\nDecimal logarithm", decimal_Log, "\nlogarithm of b to base a", log_to_base)
    log = int(input("Select the type of logarithm: "))
    if log == 1:
        b = float(input("Enter number b: "))
        print(math.log(b))
    elif log == 2:
        b = float(input("Enter number b: "))
        print(math.log10(b))
    elif log == 3:
        a = float(input("Enter base a: "))
        b = float(input("Enter number b: "))
        print(math.log(b, a))
elif operation == 5:
    sin = 1
    cos = 2
    tan = 3
    print("Sinus: ", sin, "\nCosine: ", cos, "\nTangent: ", tan)
    trig = int(input("What trigonometric function do you want to find: "))
    if trig == 1:
        a = float(input("Enter the angle: "))
        print(math.sin(a), " Radians")
        print(math.degrees(math.sin(a)), " Degrees")
    elif trig == 2:
        a = float(input("Enter the angle: "))
        print(math.cos(a), " Radians")
        print(math.degrees(math.cos(a)), " Degrees")
    elif trig == 3:
        a = float(input("Enter the angle: "))
        print(math.tan(a), " Radians")
        print(math.degrees(math.tan(a)), " Degrees")
elif operation == 6:
    x = float(input("Enter the number x: "))
    print(math.exp(x))
else:
    print("You entered a non-existent command -_-")
