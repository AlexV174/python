my_list = [1, 1, 13, 14, 15, 0, 0, 56, 56, 98]
next_list = [el for el in my_list if my_list.count(el) < 2]

print(next_list)

#my_list = [1, 1, 13, 14, 15, 0, 0, 56, 56, 98]
#next_list = [el for el in my_list if my_list.count(el) == 1]

#print(next_list)