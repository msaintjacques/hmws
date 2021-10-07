time_in_sec = int(input("Укажите время в секундах: "))

hours = time_in_sec // 3600
min = (time_in_sec % 3600) // 60
sec = ((time_in_sec % 3600) % 60) % 60

print('{:02d}:{:02d}:{:02d}'.format(hours, min, sec))