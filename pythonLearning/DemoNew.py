class Car():
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer=0;

    def get_descriptive_name(self):
        long=str(self.year) + ' ' + self.make + ' ' + self.model
        return long.title()

    def read_odometer(self):
        print("This car has " + str(self.odometer) + " miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer:
            self.odometer = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer += miles


class ElectricCar(Car):
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())



class Cat():
    def __init__(self,breed,age):
        self.breed=breed
        self.age=age

    def get_descriptive_name(self):
        varr=str(self.breed)+' of age :'+'20'
        return varr
    def get_age(self):
        return self.age



class WhiteCat(Cat):
    def __init__(self,breed,age):
        super().__init__(breed,age)


hiphop=WhiteCat("fluffy" , 3)
name=hiphop.get_descriptive_name()
age=hiphop.get_age()
print(name)

