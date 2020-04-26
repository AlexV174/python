my_list = [8, 14, 16, 7, 1, 2, -3, 11, 44]
next_list = [el for ind, el in enumerate(my_list) if el > my_list[ind - 1]]
print(next_list)