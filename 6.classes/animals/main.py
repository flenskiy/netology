import classes


def main():
    goose1 = classes.Goose('Серый', 'га-га-га', 10)
    goose2 = classes.Goose('Белый', 'га-га-га', 11)
    chicken1 = classes.Chicken('Ко-Ко', 'ко-ко-ко', 5)
    chicken2 = classes.Chicken('Кукареку', 'ко-ко-ко', 6)
    duck = classes.Duck('Кряква', 'кря-кря-кря', 7)
    cow = classes.Cow('Манька', 'муу', 170)
    sheep1 = classes.Sheep('Барашек', 'мее', 40)
    sheep2 = classes.Sheep('Кудрявый', 'мее', 45)
    goat1 = classes.Goat('Рога', 'бее', 40)
    goat2 = classes.Goat('Копыта', 'бее', 43)

    # goose1
    print(f'Класс: {goose1.__class__}',
          f'Имя: {goose1.name}',
          f'Вес: {goose1.weight}',
          f'Голос: {goose1.sound}',
          sep='\n')
    goose1.collect_eggs()
    print()

    # goose2
    print(f'Класс: {goose2.__class__}',
          f'Имя: {goose2.name}',
          f'Вес: {goose2.weight}',
          f'Голос: {goose2.sound}',
          sep='\n')
    goose2.collect_eggs()
    print()

    # chicken1
    print(f'Класс: {chicken1.__class__}',
          f'Имя: {chicken1.name}',
          f'Вес: {chicken1.weight}',
          f'Голос: {chicken1.sound}',
          sep='\n')
    chicken1.collect_eggs()
    print()

    # chicken2
    print(f'Класс: {chicken2.__class__}',
          f'Имя: {chicken2.name}',
          f'Вес: {chicken2.weight}',
          f'Голос: {chicken2.sound}',
          sep='\n')
    chicken2.collect_eggs()
    print()

    # duck
    print(f'Класс: {duck.__class__}',
          f'Имя: {duck.name}',
          f'Вес: {duck.weight}',
          f'Голос: {duck.sound}',
          sep='\n')
    duck.collect_eggs()
    print()

    # cow
    print(f'Класс: {cow.__class__}',
          f'Имя: {cow.name}',
          f'Вес: {cow.weight}',
          f'Голос: {cow.sound}',
          sep='\n')
    cow.milk()
    print()

    # goat1
    print(f'Класс: {goat1.__class__}',
          f'Имя: {goat1.name}',
          f'Вес: {goat1.weight}',
          f'Голос: {goat1.sound}',
          sep='\n')
    goat1.milk()
    print()

    # goat2
    print(f'Класс: {goat2.__class__}',
          f'Имя: {goat2.name}',
          f'Вес: {goat2.weight}',
          f'Голос: {goat2.sound}',
          sep='\n')
    goat2.milk()
    print()

    # sheep1
    print(f'Класс: {sheep1.__class__}',
          f'Имя: {sheep1.name}',
          f'Вес: {sheep1.weight}',
          f'Голос: {sheep1.sound}',
          sep='\n')
    sheep1.shear()
    print()

    # sheep2
    print(f'Класс: {sheep2.__class__}',
          f'Имя: {sheep2.name}',
          f'Вес: {sheep2.weight}',
          f'Голос: {sheep2.sound}',
          sep='\n')
    sheep2.shear()
    print()

    # считаем общий вес животных и находим животного с максимальным весом
    total_weight = 0
    max_weight = 0
    heaviest_animal = None
    for animal in classes.Animal.animals:
        total_weight = total_weight + animal.weight

        if animal.weight > max_weight:
            max_weight = animal.weight
            heaviest_animal = animal.name

    print(f'Общий вес всех животных: {total_weight}')
    print(f'Самое тяжелое животное: {heaviest_animal} ({max_weight})', '\n')

    # вызываю в цикле общий родительский метод .feed()
    for animal in classes.Animal.animals:
        animal.feed()


if __name__ == '__main__':
    main()
