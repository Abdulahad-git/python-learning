def lcm(x, y):
    if x > y:
        greater = x
    elif y < x:
        greater = y
    while (True):
        if ((greater % x == 0)) and (greater % y == 0):
            lcm = greater
            break
        greater += 1
    return lcm


num1 = int(input("please enter num1:"))
num2 = int(input("please enter num2:"))
print("The L.C.M is", lcm(num1, num2))
