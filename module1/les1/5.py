class MyMeta(type):
    def __call__(cls, *args, **kwargs):
        print('Call of', str(cls))
        print('Called', str(args))
        return type.__call__(cls, *args, *kwargs)

class MyClass(metaclass=MyMeta):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        print(self.a * self.b)


x = MyClass(4,8)
x()