class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'User {} {} years old'.format(self.name, self.age)


class GameUser(User):
    def __init__(self, n, a, game):
        super().__init__(n, a)
        self.game = game

    def __repr__(self):
        return super(GameUser, self).__repr__() + f' {self.game}'


l = User('r', 23)
print(l)
x = GameUser('r', 23, 'spider-man')
print(x)
