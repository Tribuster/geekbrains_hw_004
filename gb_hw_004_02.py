list1 = "1234566"
list2 = "554652"
list3 = "68545576"
new_list = []

for i in list1:
    for j in list2:
        for k in list3:
            new_list.append(i + j + k)
            # print(i + j + k)


print(new_list)