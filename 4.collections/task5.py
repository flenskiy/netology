l = ['2018-01-01', 'yandex', 'cpc', 100]


def main():
    global l

    x = {l[-2]: l[-1]}
    for i in l[:-2][::-1]:
        x = {i: x}

    print(x)


if __name__ == '__main__':
    main()