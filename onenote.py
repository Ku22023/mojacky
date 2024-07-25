list3 = []

def common_elements(list1,list2):
    list1.sort()
    list2.sort()
    for i in list1 and i in list2:
        list3.append(i)
    print(list3)
        

value1 = 0
value2 = 0
list1 = []
list2 = []
while value2 != "Done":
    while value1 != "Done":
        value1 = str(input("Enter words into the first list. Type 'Done' when done: "))
        list1.append(value1)
        if value1 == "Done":
            list1.pop()
        print(list1)
    else:
        value2 = str(input("Enter words into the second list. Type 'Done' when done: "))
        list2.append(value2)
        if value2 == "Done":
            list2.pop()
            common_elements(list1,list2)
        print(list2)
