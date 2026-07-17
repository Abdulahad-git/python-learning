# How to create custom exceptions
class exception(Exception):
    def __init__(self, message="Incorrect input"):
        self.message = message
        super().__init__(self, message)

try:
    name = input("Enter your name:\n")
    for s in name:
        if (name.isdigit() or name.isnumeric()):
            raise exception
        print("Name is:", name)
except exception as e:
    print(e)
