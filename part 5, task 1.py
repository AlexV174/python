with open("text1.txt", "w") as cool:
    while True:
        user_text = input()
        if len(user_text) == 0:
            break
        cool.write(user_text + "\n")