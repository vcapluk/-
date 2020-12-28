stuff = "Яблоки Апельсины Вороны Телефоны Свет Сахар".split(' ')
more_stuff = [
    "День",
    "Ночь",
    "Песня",
    "Мишка",
    "Кукуруза",
    "Банан",
    "Девочка",
    "Мальчик"
]


def main():
    print(f"Кол-во объектов: {stuff}")
    print("Погодите, тут меньше 10 объектов. Давайте исправим это.")

    if len(stuff) + len(more_stuff) < 10:
        print('В обоих списках меньше 10 элементов в сумме!')
        return

    stuff.extend(more_stuff[:10-len(stuff)])
    print(f"Теперь у нас {len(stuff)} объектов.")

    print("Давайте кое-что сделаем с нашими объектами.")
    print(stuff[1])
    print(stuff[-1])  # хм! интересно
    print(stuff.pop())
    print(' '.join(stuff))  # что? круто!
    print('#'.join(stuff[3:5]))  # просто супер!


if __name__ == '__main__':
    main()
