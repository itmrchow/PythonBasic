import math
import os



def math_test():
    print(math.pi)
    print(math.e)
    print(math.tau)

    print(math.ceil(3.14))
    print(math.ceil(2.9))

    print(math.floor(3.14))
    print(math.floor(2.9))
    
def os_test():
    print("cwd:", os.getcwd())
    print("listdir:",os.listdir())
    print("cat:",os.listdir('.vscode'))
    
os_test()