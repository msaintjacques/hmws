revenue = float(input("Укажите размер выручки компании: "))
costs = float(input("Укажите размер издержек компании: "))

result = revenue - costs

if revenue > costs:
    print("Кажется, у вас все отлично 👌🏻")
    profit = revenue - costs
    print(f"Рентабельность выручки составляет {profit / revenue}")
    workers = int(input("Укажите кол-во сотрудников в компании: "))
    print(f"Прибыль фирмы, в расчете на человека, составляет: {profit / workers}")

elif revenue < costs:
    print("Дела у вас идут не важно 😬")
elif revenue == costs:
    print("Кажется, вы работаете в ноль 😅")