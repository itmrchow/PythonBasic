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


helloWorld()
print(area(5, 3))

b = 2
changeInt(b)
print(b)

cList = ['a', 'b', 'c']
changeMe(cList)
print(cList)
