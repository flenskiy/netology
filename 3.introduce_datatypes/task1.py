def main():
    boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
    girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

    if len(boys) != len(girls):
        print('The number of people on the lists does not match, someone may be left without a match!')

    else:
        boys.sort()
        girls.sort()

        print('Perfect couples:')
        for boy, girl in zip(boys, girls):
            print(f'{boy} & {girl}')


if __name__ == '__main__':
    main()
