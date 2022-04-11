class ObjectB:
    class_value = "gogogo"

    @classmethod
    def func(cls, *args, **kwargs):
        print(cls.class_value)
        print('do some thing')

ObjectB.func()
ObjectB.func()