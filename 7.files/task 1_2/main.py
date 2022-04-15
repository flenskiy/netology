def read_file(name):
    with open(name, 'r', encoding='utf-8') as file:
        text = file.read()
    return text


def get_cook_book(text):
    cook_book = {}
    recipe_list = text.split('\n\n')
    for item in recipe_list:
        recipe = item.split('\n')
        cook_book[recipe[0]] = []
        for ingredient in range(2, 2 + int(recipe[1])):
            ingredient_name, quantity, measure = recipe[ingredient].split(' | ')
            cook_book[recipe[0]] += [{'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure}]
    return cook_book


def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingredient in cook_book[dish]:
                ingredient_name = ingredient['ingredient_name']
                measure = ingredient['measure']
                quantity = int(ingredient['quantity']) * person_count
                if ingredient_name in shop_list_by_dishes.keys():
                    shop_list_by_dishes[ingredient_name]['quantity'] += quantity
                else:
                    shop_list_by_dishes[ingredient_name] = {'measure': measure, 'quantity': quantity}
        else:
            print(f'Блюда "{dish}" нет в книге рецептов')
    return shop_list_by_dishes


def main():
    text = read_file('recipes.txt')

    cook_book = get_cook_book(text)
    print(cook_book)

    shop_list_by_dishes = get_shop_list_by_dishes(cook_book, ['Омлет', 'Запеченный картофель'], 2)
    print(shop_list_by_dishes)


if __name__ == '__main__':
    main()
