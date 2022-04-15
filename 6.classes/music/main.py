import classes


def main():
    track1 = classes.Track('Lonely Day', 4)
    track2 = classes.Track('Chop Suey!', 3)
    track3 = classes.Track('Toxicity', 5)
    album1 = classes.Album('Album 1', 'System of a Down', [track1, track2, track3])

    track4 = classes.Track('Pump It', 3)
    track5 = classes.Track('My Humps', 3)
    track6 = classes.Track('RITMO', 4)
    album2 = classes.Album('Album 2', 'Black Eyed Peas', [track4, track5, track6])

    track1.show()
    print(f'Название: {track1.name}, длительность: {track1.duration}')
    track5.show()
    print(f'Название: {track2.name}, длительность: {track2.duration}')

    print(f'Название: {album1.name}, группа: {album1.group}')
    album1.get_tracks()
    album1.add_track(classes.Track('Casino Play', 2))
    album1.get_tracks()
    album1.get_duration()

    album2.get_tracks()
    album2.get_duration()

    print(track1)
    print(track5)

    print(album1)
    print(album2)

    print(track1 > track5)
    print(track6 > track3)
    print(track6 == track1)


if __name__ == '__main__':
    main()
