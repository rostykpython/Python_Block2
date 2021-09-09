class FirstMeta(type):
    class_number = -1
    def __new__(cls, class_name, base, attrs):

        attrs['class_number'] = FirstMeta.class_number + 1
        FirstMeta.class_number += 1
        print(attrs)
        return super(FirstMeta, cls).__new__(cls, class_name, base, attrs)


class X(metaclass=FirstMeta):
    x = 12
    z = 'some_value'

    def func(self):
        pass

class Y(metaclass=FirstMeta):
    rostyk = "rostyslav"

a = X()
b = Y()
print(X.class_number)
print(Y.class_number)
