def add(*arg):
    sum = 0
    for n in arg:
        sum += n
    return(sum)

# print(add(3, 5, 6))

def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs:
    #     print(key)
    #     print(value)

    n += kwargs["add"]
    n *= kwargs["multiply"]

    print(n)

calculate(2, add=3, multiply=5)

class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")  # .get() gets the value of the key but returns none if key doesn't exist instead of an error
        self.model = kw.get("model")

my_car = Car(make="Nissan", model="GT-R")
print(my_car.make, my_car.model)

second_car = Car(make="Nissan")
print(second_car.model)