#abstraction (encapsulation): hiding inner workings from outside code
#polymorphism: single interface to different types (operate on different objects in the same way)
#inheritance: build functionality off a superclass
#class: a blueprint for an object
#instance: an object created from a class (instantiation)
#constructor: a function called to instantiate a class
#attribute: instance variables
#method: function attached to an instance

class YourClass():
    #attributes and methods go here
    def __init__(self, name, size=20):
        self.name = name
        self.size = size
        self.questions = []
        self.max_size = 100
        self.full = False

    def __len__(self):
        return len(self.questions)

    def __str__(self):
        return: 'Name: {} Size: {}'.format(self.name, self.size)

    def __eq__(self, other): #defining what the equal sign represent
        return self.name == other.name

    def ask_question(self, question):
        self.questions.append('{}?'.format(question))

    def questions_asked(self):
        return self.questions

    def add_students(self, count):
        if self.size + count > self.max_size:
            print "No more!"
            self.full = True


    def at_capacity(self):
        return self.full


if __name__ == '__main__':
    your_class = YourClass('Boulder Galvanize')
    your_class.ask_question("Why Python")
    your_class.ask_question("Why not")
    print your_class.questions_asked()
    print your_class.at_capacity()
    print your_class.add_students(78)
    print your_class.name, your_class.size

their_class = YourClass('Boulder Galvanize')

print str(your_class == their_class)



#WARM-UP 1
class Dog():
    def __init__(self, name, happiness_level=5):
        self.name = name
        self.happiness_level = happiness_level

    def wag_tail(self, n):
        self.happiness_level += (5*n)

my_dog = Dog('Fido')
my_dog.wag_tail(7)
print my_dog.name, my_dog.happiness_level

#WARM-UP 2
class Cat():
    def __init__(self, name, laziness_level=5, location='home'):
        self.name = name
        self.laziness_level = laziness_level
        self.location = location

    def sense_earthquake(self, earthquake):
        if earthquake == True:
            self.location = "Gone dark"
            print '{} has gone dark!'.format(self.name)
        else:
            print '{} is at {}'.format(self.name, self.location)

my_cat = Cat("Boris")
my_cat.sense_earthquake(True)
print my_cat.location

#WARM-UP 3
class Car():
    def __init__(self, model, color, tank_size):
        self.model = model
        self.color = color
        self.tank_size = tank_size
        self.gallons_of_gas = self.tank_size

    def drive(self, miles_driven):
        self.gallons_of_gas -= miles_driven/10

class Fly():
    def __init__(self, destination, departure_city, trip_distance):
        self.destination = destination
        self.departure_city = departure_city
        self.trip_distance = trip_distance

    def fly(self):
        self.departure_city, self.destination = self.destination, self.departure_city
