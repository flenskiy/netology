from cook_book import cook_book

person = 5


def main():
    for dish in cook_book:
        print(f'{dish[0]}:'.capitalize())

        for ingredient in dish[1]:
            print(f'{ingredient[0]}, {ingredient[1] * person} {ingredient[2]}')

        print()


if __name__ == '__main__':
    main()
