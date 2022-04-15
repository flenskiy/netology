ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}


def main():
    global ids
    unique_ids = []

    for item in ids.values():
        for id in item:
            if id not in unique_ids:
                unique_ids.append(id)

    print(unique_ids)


if __name__ == '__main__':
    main()

