class A:
    def __init__(self, a):
        self.a = a

    def show_a(self):
        print(self.a)

    def __call__(self, *args, **kwargs):
        print('I`m called!')
        return [args, kwargs]


a = A(1)
print(a(1,2,3))