# iter and next
import sys

mList = [1, 2, 3, 4]
it = iter(mList)
print("iter and next")
print(next(it))
print(next(it))

# for迴圈遍歷iter
print("for遍歷iter")
for i in it:
    print(i, end=" ")

print("\n")

# while loop next
mList2 = [1, 2, 3, 4]
it2 = iter(mList2)
print("while遍歷iter")
while True:
    try:
        print(next(it2))
    except StopIteration:
        sys.exit()
