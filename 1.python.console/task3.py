def swap(word):
    return word[-1] + word[1:-1] + word[0]


def main():
    word = input('Input word: ')
    if len(word) > 1:
        print('Swap word: ', swap(word))
    else:
        exit(0)


if __name__ == '__main__':
    main()
