t = True
while t:
    ops = input("Do you want to read or write inside a file :\n")
    if ops == "read":
        with open("Demmm", "r") as file:
            data = file.readlines();
            print(data)
    elif ops == "write":
        with open("Demmm", "a") as file:
            data = input("Enter Your Name :\n")
            if data == "EXIT":
               break
            else:
               file.write("\n" + data + " has submitted data")
