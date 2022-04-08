def list_test():
    my_list = [1, 20, 30, 400, 5000, 6]

    my_list2 = [7, 78, 778, 30, 20]

    my_list.append(90)
    # myList.extend(myList2)
    my_list.remove(30)
    my_list.pop(-2)

    print("myList:", my_list)
    print("myList2:", my_list2)

    print("len:", len(my_list))
    print("sum:", sum(my_list))
    print("max:", max(my_list))
    print("min:", min(my_list))


def dict_in_list_test():

    students = [
        {'Name': 'Jay', 'Number': '001', 'Age': 18},
        {'Name': 'Jojo', 'Number': '002', 'Age': 20},
        {'Name': 'Dio', 'Number': '003', 'Age': 23}
    ]

    for student in students:
        print(student)


# list_test()
dict_in_list_test()
