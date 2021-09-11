class Power:
    def __init__(self, cls):
        self.__cls = cls

    def __call__(self, a, b):
        new_field = self.__cls(a*2, b*2)
        return new_field


@Power
class NormalClass:
    def __init__(self, field, b):
        self.field = field
        self.b = b

    def __call__(self):
        return self.field + self.b


x = NormalClass('b', 'a')
print(x())

