# while
a, b = 0, 1
list = []
while b < 10:
    print(b, sep=',', end=',')
    a, b = b, a+b
    list.append(b)

print(b, sep=",")

# if else
index = 0
while index < 10:
    if index % 2 == 0:
        print(index, ":偶數")
    else:
        print(index, ":奇數")
    index += 1
