class MyClass:
    # 返回迭代器對象，會實作next方法並透過stopiteration來標示完成
    def __iter__(self):
        self.a = 1
        return self

    # 返回下一個迭代器對象
    def __next__(self):
        x = self.a
        self.a += 1
        return x


myClass = MyClass()
myIter = iter(myClass)

print("MyIteration")
print(next(myIter))
print(next(myIter))
print(next(myIter))
