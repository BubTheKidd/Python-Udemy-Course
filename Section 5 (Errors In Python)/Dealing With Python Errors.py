# "Shouldn't ask permission, ask for forgiveness" is the model for this
# concept in Python. Reminding yourself this will make your code slightly
# more efficient...
class Bullshit:
    def __repr__(self):
        print(f"Bullshit class...")


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year

    def __repr__(self):
        return (f"<< Car: {self.model} from {self.year}")


class Garage:
    def __init__(self):
        self.cars = []


    def __len__(self):
        return len(self.cars)


    def ParkCar(self, car):
        if not isinstance(car, Car):
            raise TypeError(f"Tried adding: {car.__class__.__name__} to garage. Only excepts type 'Car.'")
        self.cars.append(car)


    def ListCars(self):
        for car in self.cars:
            print(car)


my_garage = Garage()
my_car = Car("Mitsubishi Outlander", 2016)
gf_car = Car("Toyota Corolla", 2003)
bullshit = Bullshit()

# Common way of checking whether an object belongs to a specified class
# before running code... (Asking Permission)
if isinstance(my_car, Car):
    my_garage.ParkCar(my_car)
else:
    print("Ummmm, that is NOT a car...")


# Here, we are instead trying to run code right off the bat. And if it
# fails, then run something else... (Asking Forgiveness)
try:
    my_garage.ParkCar(gf_car)
# Only catches what is specified (TypeError in this case). If a ValueError
# was specified, then Python would ignore this a carry on with the normal
# traceback procedure...
except TypeError:
    print("Fail! That's not a car!")
# Can add more exceptions
except NameError:
    print("It's called what now?!")
# 'finally' runs everytime. No matter what happened above. ALWAYS
finally:
    my_garage.ListCars()




"""
Accounting for these errors explicitly helps make your code more user friendly.
You don't want the user to have to deal with tracebacks and all the different
kinds of errors. If you can account for what might happen, you can redirect the
code, making it easier on everyone...
"""