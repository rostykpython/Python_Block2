class X():
    def __new__(cls, *args, **kwargs):
        print('Here we are!')
        return super().__new__(cls, *args, **kwargs)

    def __init__(self):
        print('Initialize')

y = X
y()
