from geo_logs import geo_logs


def main():
    geo_logs_russia = []

    for geo_log in geo_logs:
        for visit in geo_log.values():
            if 'Россия' in visit:
                geo_logs_russia.append(geo_log)

    print(geo_logs_russia)


if __name__ == '__main__':
    main()
