a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
h = float(input("Введіть h: "))

x = a
spisok = []

while x <= b:
    y = 1 / (x**2 + 1) + x**2
    spisok.append([x, y])
    x = x + h

print("\n Список:")
for item in spisok:
    print(item)

max_row = max(spisok, key = lambda row: row[1])

print("\n Рядок з найбільшим значенням функції:")
print(max_row)
