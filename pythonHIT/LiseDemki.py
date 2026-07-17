mylist = [5, 2, 3, 5, 5, 5]
print(mylist[:])

print(len(mylist))
RegNo = []
for i in range(8101, 8153):
    RegNo.append(i)

print("______________________________")


def met(*n):
    print(n[1])


met(1, 2, 3, 4);
print("\n______________________________\n")
global h;


# Syntax for lambda ---> var_name = lambda agrs : code
x = lambda: print("Welcome to Lambda")
x()
y = lambda name, age: print("Welcome {} to lamda and age is {}".format(name, age))+print("Hello")
y("abdul", 20)
z = lambda *n :\
    print(n)
z(1,2,3,)