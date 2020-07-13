# while
a, b = 0, 1
while b < 10:
    a, b = b, a+b
    if b < 10:
        print(b, end=",")
    else:
        print(b, end="")
else:
    print(" End")


# if else
index = 0
while index < 10:
    if index % 2 == 0:
        print(index, ":偶數")
    else:
        print(index, ":奇數")
    index += 1

# for
fruit_list = ["apple", "banana", "mango"]
for fruit in fruit_list:
    print(fruit)
else:
    print("End")

# for range
for x in range(3, 5):
    print(x)

for x in range(len(fruit_list)):
    print(x, fruit_list[x])
