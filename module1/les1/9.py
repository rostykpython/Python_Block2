class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


class Dog(Animal):
    def __init__(self, *args):
        super(Dog, self).__init__(*args)


dog1 = Dog(40, 50)

print(dog1.height)
print(dog1.weight)