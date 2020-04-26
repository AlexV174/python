from itertools import count, cycle

#for el in count(int(input("Введите начальное число: "))):
#    print(el)

my_list = ['Python', 'Programming']
for i in cycle(my_list):
    print(i)