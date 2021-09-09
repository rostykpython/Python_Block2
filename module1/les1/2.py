class Test:
    some_name = 'Mike'

class Foo:
    def greeting(self):
        print('Hello!')

x = Test()

print(x.some_name)

Test2 = type('Test2', (), {})

def dynamic_atr(self):
    self.z = 9

Test3 = type('Test3', (Foo,), {'some_name': 'Rostyslav', 'dynamic_atr': dynamic_atr})

MyList = type('MyList', (list,), dict(new_len = lambda self: len(self)))

l = MyList()
l.append(2)
print(l)
print(l.new_len())


