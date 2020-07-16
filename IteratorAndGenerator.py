#iter and next
mList = [1, 2, 3, 4]
it = iter(mList)
print(next(it))
print(next(it))

# for迴圈遍歷iter
for i in it:
    print(i, end=" ")
