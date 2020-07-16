class MyClass:
    # 返回迭代器對象，會實作next方法並透過stopiteration來標示完成
    def __iter__(self):
        self.a = 1
        return self

    # 返回下一個迭代器對象
    # def __next__(self):
    #     x = self.a
    #     self.a += 1
    #     return x

    def __next__(self):
        if(self.a <= 20):
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

    # 產生器
    def fibonacci(self, n):
        a, b, counter = 0, 1, 0
        while True:
            if counter > n:
                return

            yield a
            a, b = b, a+b
            counter += 1


myClass = MyClass()
myIter = iter(myClass)
fibonacci = myClass.fibonacci(10)

print("MyIteration")
for i in myIter:
    print(i)

print("yield method")
for f in fibonacci:
    print(f)
