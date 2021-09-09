class MyMeta(type):
    def __new__(mcs, name, bases, attrs):
        print('_________')
        print('Created place for: ', name)
        print(mcs)
        return super(MyMeta, mcs).__new__(mcs, name, bases, attrs)

    def __init__(cls, name, bases, attrs):
        print('_________')
        print('Initiated place for: ', name)
        print(cls)
        super(MyMeta, cls).__init__(name, bases, attrs)


class MyClass(metaclass=MyMeta):
    def __init__(self):
        print('Object has been created')


x = MyClass()