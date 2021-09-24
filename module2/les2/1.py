class MetaSingleton(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(MetaSingleton, cls).__call__()
        return cls._instance[cls]


class Config(metaclass=MetaSingleton):
    pass


conf1 = Config()
conf2 = Config()

print(conf2, conf1)
