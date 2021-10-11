f = open("4.txt", "r")
f_res = open("4_res.txt", "w")

for line in f.readlines():
    if len(line.split("—")) >= 2:
        n, v = line.split("—")[0].strip(), line.split("—")[1].strip()
        translate = ""

        if n == "One":
            translate = "Один"
        elif n == "Two":
            translate = "Два"
        elif n == "Three":
            translate = "Три"
        elif n == "Four":
            translate = "Четыре"
        else:
            continue

        f_res.write(translate + " - " + v + "\n")

f.close()
f_res.close()