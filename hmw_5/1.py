f = open("file.txt", "w")

end = True

while end:
    str = input("Введите строку: ")

    if str == "":
        end = False
    else:
        f.write(str+"\n")

f.close()