class Calculator:
    total_object = 0
    def __new__(cls):
        cls.total_object += 1


class MyClass(Calculator):
    @classmethod
    def total_objects(cls):
        print(MyClass.total_object)

obj1 = MyClass()
obj2 = MyClass()
MyClass.total_objects()

