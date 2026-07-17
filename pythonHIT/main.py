def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

t = True
while t:
    num = int(input("\nEnter a number to find factorial : \n"))
    if num == 0:
        t = False
    ans = factorial(num)
    print("The factorial of " + str(num) + " is " + str(ans))

