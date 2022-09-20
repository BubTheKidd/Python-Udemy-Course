# Useful for when working on a project and you don't want to accidently
# save an unimplemented feature in the database. Having errors like this 
# can save you and other developers a lot of time.


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


    def ParkCar(self, model):
        self.cars.append(model)


    def ListCars(self):
        for car in self.cars:
            print(car)

    def AppraiseCar(self, car):
        # isinstance is a built-in function that allows you to check if an
        # object is an 'instance' of the specified class
        if not isinstance(car, Car):
            # No need for an 'elif' as raising an error automatically 
            # crashes the program...
            raise TypeError(f"""Tried to print {car.__class__.__name__}
            to the garage. Need objects of the 'Car' class.""")

        raise NotImplementedError("Haven't done this yet.")


my_garage = Garage()
my_garage.ParkCar("Mitsubishi Outlander")
# my_garage.AppraiseCar()
my_car = Car("Mitsubishi Outlander", 2016)
print(my_car)

