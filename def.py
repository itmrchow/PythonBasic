def helloWorld():
    """
    : first def
    """
    print("Hello World")


def area(width, height):
    """
    : 帶參數def
    """
    return width*height


def changeInt(input_i):
    """
    :傳不可變對象
    """
    input_i = 10
    return input_i


def changeMe(inputList):
    """
    :傳可變對象
    """
    for i in range(len(inputList)):
        inputList[i] = inputList[i]*2


def printMe(str1, str2):  # 必須參數
    print("第一組:"+str1)
    print("第二組:"+str2)


def printInfo(arg1, *vartuple):  # 不定長參數 *tuple
    print(arg1, end=",")
    for var in vartuple:
        print(var, end=",")


def printInfo_2(arg1, **vardict):  # 不定長參數 *tuple
    print(arg1)
    print(vardict)


helloWorld()
print(area(5, 3))

b = 2
changeInt(b)
print(b)

cList = ['a', 'b', 'c']
changeMe(cList)
print(cList)

printMe("hello", "world")
printMe(str2="JJJJJ", str1="YYYY")

printInfo(4, 5, 6, 7, 8)
printInfo_2(4, a=2, b=3)
