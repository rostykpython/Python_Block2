class NewMeta(type):
    def __new__(cls, class_name, base, class_attrs):
        print(class_attrs)
        a = {}
        for key, val in class_attrs.items():
            if key.startswith('__'):
                a[key] = val
            else:
                a[key.upper()] = val
        print(a)
        return type('', base, a)

class JustClass(metaclass=NewMeta):
    x = 1
    b = 2

y = JustClass()
print(y.X)