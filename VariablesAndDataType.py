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
str1 = "milk"
print(str1)
print(str1[0:2])
print(str1[-1:-4])

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
tuple1 = ('apple', 'banana', 'orange', 3)
tuple2 = ('t', )
print(tuple1[0:])
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
dict1 = {}
dict1["Jeff"] = 27
dict1["Tony"] = 23
print(dict)

dict2 = {"tea": 20, "coke": 30}
print(dict2)

print(dict1.keys())  # 取key
print(dict1.values())  # 取values

# dataType transformation
print(int("123"))  # 轉整數
print(float("12.3"))  # 轉浮點
print(str(123))  # 轉可讀字串
reprStr = "Hello world!\n"
print(str(reprStr))  # 轉編譯器可讀 ->定義一些在例項執行
print(repr(reprStr))
print(eval("33+33"))

# set tuple list 轉換
print(tuple(t))
