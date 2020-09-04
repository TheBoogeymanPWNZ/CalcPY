import math

constant_values = 1
stand_calc = 2
discriminant = 3
logarithm = 4
trigonometry = 5
exponent = 6

print("Constant: ", constant_values, "\nCalculator: ", stand_calc, "\nDiscriminant: ", discriminant, "\nLogarithm",
      logarithm,
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

    def calc(num_1, num_2):
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

    calc(float(input("Enter the first number: ")),
         float(input("Enter the second number: ")))
elif operation == 3:
    def dis(a, b, c):
        Dis = b * b - 4 * a * c
        if Dis > 0:
            x1 = (-b + math.sqrt(Dis)) / (2 * a)
            x2 = (-b - math.sqrt(Dis)) / (2 * a)
            print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
        elif Dis == 0:
            x = -b / (2 * a)
            print("x = %.2f" % x)
        else:
            print("No Roots")
    dis(float(input("Enter value a = ")), float(
        input("Enter value b = ")),  float(input("Enter value c = ")))
elif operation == 4:
    def logar(log):
        print("Natural logarithm: ", 1, "\nDecimal logarithm: ",
            2, "\nlogarithm of b to base a: ", 3)
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
    logar(print("Select the type of logarithm"))

elif operation == 5:
    sin=1
    cos=2
    tan=3
    print("Sinus: ", sin, "\nCosine: ", cos, "\nTangent: ", tan)
    trig=int(input("What trigonometric function do you want to find: "))
    if trig == 1:
        a=float(input("Enter the angle: "))
        print(math.sin(a), " Radians")
        print(math.degrees(math.sin(a)), " Degrees")
    elif trig == 2:
        a=float(input("Enter the angle: "))
        print(math.cos(a), " Radians")
        print(math.degrees(math.cos(a)), " Degrees")
    elif trig == 3:
        a=float(input("Enter the angle: "))
        print(math.tan(a), " Radians")
        print(math.degrees(math.tan(a)), " Degrees")
elif operation == 6:
    x=float(input("Enter the number x: "))
    print(math.exp(x))
else:
    print("You entered a non-existent command -_-")
