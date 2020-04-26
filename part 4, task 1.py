#from sys import argv

#script_name, staff_name, hours, per_hour, prize = argv

#print("Имя cкрипта: ", script_name)
#print("Имя работника: ", staff_name)
#print("Наработка часов: ", hours)
#print("Ставка в час: ", per_hour)
#print("Премия: ", prize)


#print(f"Заработная плата сотрудника {staff_name} = {(int(hours) * int(per_hour)) + int(prize)}")

from sys import argv

script_name, staff_name, hours, per_hour, prize = argv
try:
    hours = int(hours)
    per_hour = int(per_hour)
    prize = int(prize)
    salary = (hours * per_hour) + prize
    print(f"Заработная плата сотрудника {staff_name} = {salary} руб.")
except ValueError:
    print("Введите число !")

# передача данных через Run - Edit Configurations ...