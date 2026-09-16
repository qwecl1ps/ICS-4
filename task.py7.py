a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

for i in range(int((b - a) / h) + 1):
    y = 1 / (x**2 + 1) + x**2
    print("x = %.2f y = %.3f" % (x, y))
    x = x + h
