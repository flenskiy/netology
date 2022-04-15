def main():
    try:
        salary = float(input('Введите заработную плату в месяц: '))
        if salary <= 0:
            raise ValueError('value less than or equal to zero')

        percent_mortgage = float(input('Введите, какой процент(%) уходит на ипотеку: '))
        if percent_mortgage < 0:
            raise ValueError('value less than zero')
        elif percent_mortgage > 100:
            raise ValueError('value greater than one hundred')

        percent_life = float(input('Введите, какой процент(%) уходит на жизнь: '))
        if percent_life < 0:
            raise ValueError('value less than zero')
        elif percent_mortgage > 100:
            raise ValueError('value greater than one hundred')
        elif (100 - percent_mortgage) < percent_life:
            raise ValueError('the total percentage is more than a hundred')

        total_mortgage_payment = (salary / 100) * percent_mortgage * 12
        total_life_payment = (salary / 100) * percent_life * 12
        total_balance = 12 * salary - total_mortgage_payment - total_life_payment

        print(f'На ипотеку было потрачено: {total_mortgage_payment} р.')
        print(f'Было накоплено: {total_balance} р.')

    except ValueError as e:
        print('error:', e)


if __name__ == '__main__':
    main()
