from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Копирование даных из файла {from_file} в файл {to_file}")

# Можно в одну строку?
in_file=open(from_file);indata=in_file.read()

print(f"Исходный файл имеет размер {len(indata)} байт")

print(f"Целевой файл существует?{exists(to_file)}")
print("Готов. нажмите клавишу ЭНТЕР для продолжения или CTRL+С для отмены.")
input()

out_file=open(to_file,'w')
out_file.write(indata)

print("Отлично! Все готово!")

out_file.close()
in_file.close()