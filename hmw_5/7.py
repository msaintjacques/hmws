from json import dumps

results = [{}, {}]

with open("7.txt") as f:
    lines = f.readlines()

for line in lines:
    if len(line.split(" ")) == 4:
        name, _, proceeds, expenses = line.split()
        results[0][name] = int(proceeds) - int(expenses)

results[1]['average_profit'] = round(sum(profit for _, profit in results[0].items() if profit > 0) / len(results[0]))

with open("7.json", "w") as f:
    f.write(dumps(results))
