class Animal:

    def behave(self):
        return 'My behaviour!'


class Dog:
    def __init__(self, name, w, h):
        self.name = name
        self.weight = w
        self.height = h

    def info(self):
        info = {
            'name': self.name,
            'weight': self.weight,
            'height': self.height

        }
        return info

    def barking(self):
        noise = ('{} is doing: Bark! '.format(self.name))
        return noise


class AggressiveDog(Dog):
    def __init__(self, name, weight, height, aggression):
        super(AggressiveDog, self).__init__(name, weight, height)
        self.aggression = aggression

    def barking(self):
        return super().barking() + ' .But stay away from it!'

    def aggressiveness(self):
        """
        Aggressiveness could be medium or high
        """
        print('This is {} and it is {} aggressive'.format(self.name, self.aggression))
        return super().info()


class NoneAggressiveDog(Dog, Animal):
    def __init__(self, name, weight, height, color):
        super(NoneAggressiveDog, self).__init__(name, weight, height)
        self.color = color

    def barking(self):
        return super().behave() + 'And its very cute!'

    def happiness(self):
        print('{} its so friendly'.format(self.name))
        return super().info()


jack_pug = NoneAggressiveDog('Jack', 10, 20, 'gray')

print(jack_pug.barking())
print(jack_pug.happiness())

mark_boxer = AggressiveDog('mark', 20, 60, 'medium')

print(mark_boxer.barking())
print(mark_boxer.aggressiveness())

print( NoneAggressiveDog.mro())





