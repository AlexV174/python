my_list = [123, 'task 1', True, 0.78, None, [1, 'str'], (4, 234), {'1', '2'}, {'key_1': 'val_1'}, b'text',
           bytearray(b'some text'), frozenset('123'), complex(5, 6)]
print(my_list)
for i in my_list:
    print(type(i))
