import math
num_1 = float(input("Enter the first number: "))
num_2 = float(input("Enter the second number: "))

addition = 1
subtract = 2
multiplic = 3
division = 4
discriminant = 5
print("Addition: ", addition, "\nSubtraction: ", subtract, "\nMultiplication: ", multiplic, "\nDivision: ", division, "\nDiscriminant", discriminant)

act = int(input("Выберите действие из предложенных: "))
if act == 1:
    print(num_1 + num_2)
elif act == 2:
    print(num_1 - num_2)
elif act == 3:
    print(num_1 * num_2)
elif act == 4:
    print(num_1 / num_2)
elif act == 5:
    num_a = float(input("Enter value a = "))
    num_b = float(input("Enter value b = "))
    num_c = float(input("Enter value c = "))
    Dis = num_b * num_b - 4 * num_a * num_c
    if Dis < 0:
        print("No real roots")
        x1 = -num_b / (2 * num_a)
        x2 = math.sqrt(abs(Dis)) / (2 * num_a)
        print("Complex roots of the equation")
        print(num_a, "x^2 ", num_b, "x + ", num_c, " = 0")
        if x2 > 0:
            print(x1, " + ", x2, "i")
            print(x1, " - ", x2, "i")
        else:
            print(x1, " - ", abs(x2), "i")
            print(x1, " + ", abs(x2), "i")
    else:
        x1 = (-num_b + math.sqrt(Dis)) / (2 * num_a)
        x2 = (-num_b - math.sqrt(Dis)) / (2 * num_a)
        print("Real roots of the equation")
        print(num_a, "x^2 + ", num_b, "x + ", num_c, " = 0")
        print("x1 = ", x1, "x2 = ", x2)
else:
    print("Вы ввели несуществующую команду -_-")
