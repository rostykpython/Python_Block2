class A:
    def __init__(self, a, b):
        self.first = a
        self.second = b


obj1 = A(1, 2)
obj1.third = 3
obj1.fourth = 4

print(obj1.__dict__)


class SlotClass:
    __slots__ = ('foo', 'bar')


class ChildSlotClass(SlotClass):
    __slots__ = ('baz',)


obj2 = ChildSlotClass()
obj2.foo = 1
obj2.bar = 2
obj2.baz = 3

