from sys import argv

script, filename = argv

print(f"Я собираюсь стереть файл {filename}.")
print("Если вы не хотите стирать файл, нажмите сочетание КТРЛ+С (^C).")
print("Если вы хотите стереть файл, нажмите клавишу Энтер.")

input("?")

print("Открытие файла.....")
target = open(filename, 'w')

print("Очистка файла. До свидания!")
target.truncate()

print("Теперь я запрашиваю три строки...")

line1=input("строка 1: ")
line2=input("строка 2: ")
line3=input("строка 3: ")

print("Это я запишу в файл.")

#target.write(line1)
#target.write("\n")
#target.write(line2)
#target.write("\n")
#target.write(line3)
#target.write("\n")

target.write(f"""{line1}\n{line2}\n{line3}\n""")

print("И наконец, я закрою файл.")
target.close()
