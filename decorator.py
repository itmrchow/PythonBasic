def print_hello(func):
    
    def wrapper(*args, **kwargs):
        print("Hello")
        return func(*args, **kwargs)
    return wrapper

def print_arg(arg):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(arg)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@print_hello  # print_hello = print_hello(print_world)
def print_world():
    print("world")


@print_hello
def print_single(arg):
    print(arg)


@print_hello
@print_arg("Hi")
def print_double(arg1, arg2):
    print(arg1)
    print(arg2)
    


# print_world()
# print_single("HeyHeyHeyHeyHey")
print_double("yaa","youyouyouyouyou")