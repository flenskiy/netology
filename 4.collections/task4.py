stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}


def main():
    global stats
    max_sales = 0
    top_channel = None

    for channel in stats:
        if stats[channel] > max_sales:
            max_sales = stats[channel]
            top_channel = channel

    print(f'Канал с максимальным объемом продаж - {top_channel}')


if __name__ == '__main__':
    main()