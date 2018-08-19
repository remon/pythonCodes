# class animal inherit all class object's attributes
class animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print("{} is eating {}".format(self.name, food))

# class dog inherit all class animal's attributes
# plus its attributes
class dog(animal):
    def fetch(self, thing):
        print("{} fetched {}".format(self.name, thing))

# class cat inherit all class animal's attributes
# plus its attributes
class cat(animal):
    def cat_eat(self, eat):
        print("{} eats {}".format(self.name, eat))
