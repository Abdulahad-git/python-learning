import os
print(os.getcwd())
print(10-5)
try:
    f=10/0
except ZeroDivisionError as e:
    print("This is a exceptiononal statement",e)