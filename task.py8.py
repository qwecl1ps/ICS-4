a = float(input("Введіть а: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a

while x <= b:
    y = 1 / (x **2 + 1) + x**2
    print("x = %.2f y = %.3f" % (x, y))
    x = x + h
    