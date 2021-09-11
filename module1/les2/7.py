class Power:
    def __init__(self, func):
        self.__func = func
        self._memory = []

    def __call__(self, a, b):
        result = self.__func(a, b)
        self._memory.append(result)
        return result

    def memory(self):
        return self._memory


@Power
def multiply(a, b):
    return a*b


print(multiply)
print(multiply(1, 2))
print(multiply(2,3))
print(multiply(3,4))
print(multiply.memory())
