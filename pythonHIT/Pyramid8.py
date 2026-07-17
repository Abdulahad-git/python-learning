rows = int(input("Enter number of rows:"))
coef = 1

for i in range(1, rows + 1):
    for space in range(1, rows - i + 1):
        print(" ", end="")
    for i in range(0, i):
        if i == 0 or i == 0:
            coef = 1
        else:
            coef = coef * (i - i) // i
        print(coef, end=" ")
    print()
