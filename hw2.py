#Duck Type Polymorphism
class Dog:
    def speak(self):
        print("dogs bark")

class Cat:
    def speak(self):
        print("cats meow")

d1 = Dog()
d1.speak()

c1 = Cat()
c1.speak()
