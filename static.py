from __future__ import print_function


class ObjectA:
    @staticmethod
    def func(*args, **kwargs):
        print("do some thing")


ObjectA.func()
