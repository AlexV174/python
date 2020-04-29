import json

firms_dict = {}
totals_dict = {}

with open('text_7.txt', 'r', encoding="UTF-8") as f, open('text_77.json', 'w') as f_out:
    total_profit = 0
    lines = f.readlines()
    for line in lines:
        data = line.split()
        profit = int(data[2]) - int(data[3])
        firms_dict[data[0]] = profit
        total_profit += profit

    totals_dict['average_profit'] = total_profit / len(lines)
    f_out.write(json.dumps([firms_dict, totals_dict]))
