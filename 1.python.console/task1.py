def area_calculate(a, b):
    return a * b


def perimeter_calculate(a, b):
    return 2 * (a + b)


def main():
    try:
        square_side = float(input('Enter the length of square side: '))
        if square_side <= 0:
            raise ValueError('value less than or equal to zero')
        perimeter_of_square = perimeter_calculate(square_side, square_side)
        area_of_square = area_calculate(square_side, square_side)
        print('Perimeter of square =', perimeter_of_square)
        print('Area of square =', area_of_square, '\n')

        rectangle_side_1 = float(input('Enter the length of rectangle side 1: '))
        rectangle_side_2 = float(input('Enter the length of rectangle side 2: '))
        if rectangle_side_1 <= 0 or rectangle_side_2 <= 0:
            raise ValueError('value less than or equal to zero')
        perimeter_of_rectangle = perimeter_calculate(rectangle_side_1, rectangle_side_2)
        area_of_rectangle = area_calculate(rectangle_side_1, rectangle_side_2)
        print('Perimeter of rectangle =', perimeter_of_rectangle)
        print('Area of rectangle =', area_of_rectangle)

    except ValueError as e:
        print('Wrong value has entered: ', e)


if __name__ == '__main__':
    main()
