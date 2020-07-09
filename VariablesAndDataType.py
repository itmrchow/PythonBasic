# 變數、型態練習
# 多變數附值
a = b = c = 1
print(a)
print(b)
print(c)

# Number
print(3/2)  # 1.5
print(3 % 2)  # 1
print(2 ** -3)  # 2的次方

# String
str = "milk"
print(str)
print(str[0:2])
print(str[-1:-4])

# List : 可異動
t = ['a', 'b', 'c', 'd', 'e', 'x']
y = ['f', 'g']
print(t[1:3])
print(t[3:])
print(t[:4])
print(t[:])
print(t*2)  # 輸出多次
print(t+y)  # 串接
y[0] = 'change'  # 替換
print(y)

letter = ['c', 'h', 'e', 'c', 'k', 'i', 'o']
print(letter[1:4])
print(letter[0:-1:2])  # my_list[start:end:sep] 取間隔
print(letter[-1::-1])  # 反向輸出
print(len(letter))  # 取長

# Tuple : 不可異動
tuple = ('apple', 'banana', 'orange', 3)
tuple2 = ('t', )
print(tuple[0:])
print(tuple2)

# Set : 重複者被刪除，沒有順序
set1 = {"abc", "abc", "tttt"}
print(set1)

# 集合運算
set_a = set("abcdef")
set_b = set("defghi")
print(set_a)
print(set_a - set_b)  # 差集
print(set_a | set_b)  # 聯集
print(set_a & set_b)  # 交集
print(set_a ^ set_b)  # 同時不存在的

# Dictionary
dict = {}
dict["Jeff"] = 27
dict["Tony"] = 23
print(dict)

dict2 = {"tea": 20, "coke": 30}
print(dict2)

print(dict.keys())  # 取key
print(dict.values())  # 取values
