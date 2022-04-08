with open("data.txt", 'w') as f:
    # print("read word", f.read(5))
    # print("read line", f.readline())
    # print("read lines", f.readlines())

    f.write("writeTest ")


with open("data.txt", 'r') as f:
    print(f.read())
