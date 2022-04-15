from queries import queries


def percentages_calculation(a, b):
    """
    Функция считает процент который составляет одно число от другого

    :param a: число от которого ищем процент
    :type a: int
    :param b: число для которого ищем процент
    :type b: int

    :returns: процент
    :rtype: float
    """

    return round((100 * b / a), 1)


def word_count_str(string):
    """
    Функция считает количество слов в строке
    :param string: строка
    :type string: str

    :returns: количество слов в строке
    :rtype: int
    """

    return len(string.split())


def main():
    query_options = set()
    total_amount = len(queries)

    for query in queries:
        query_options.add(word_count_str(query))

    query_distribution = dict.fromkeys(query_options, 0)

    for query in queries:
        word_count = word_count_str(query)
        query_distribution[word_count] += 1

    for item in query_distribution:
        percentage = percentages_calculation(total_amount, query_distribution[item])
        print(f'Поисковых запросов из {item} слов(а) - {percentage} %')


if __name__ == '__main__':
    main()
