list1=['a','b','c']
list2=[1,2,3]

zip_list = zip(list1,list2)

print("first iteration...")
for first_iteration_list1,first_iteration_list2 in zip_list:
    print(first_iteration_list1, first_iteration_list2)

print("second iteration...")
for second_iteration_list1,second_iteration_list2 in zip_list:
    print(second_iteration_list1, second_iteration_list2)