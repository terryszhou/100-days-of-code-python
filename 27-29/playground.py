def add(*args):
    return sum(args)

# print(add(3, 5, 6, 8))

def calculate(n, **kwargs):
    # PRINT KWARGS
    print(kwargs)

    # PRINT KEYS, VALUES FOR KWARG DICT
    for key, value in kwargs.items():
        print(key, value)

    # PRINT KWARG BY KEY
    print(kwargs["add"])

    # KWARG MANIPULATION
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

# calculate(2, add=3, multiply=5)

# REQUIRED KWARGS
class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]

my_car = Car(make="Nissan")
# print(my_car) # <-- RETURNS ERROR

# OPTIONAL KWARGS
class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")

my_car = Car(make="Nissan")
# print(my_car.make) # <-- NO ERROR

