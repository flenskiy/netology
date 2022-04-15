class Album:
    def __init__(self, name, group, track_list):
        self.name = name
        self.group = group
        self.track_list = track_list

    def __str__(self):
        tracks = ''
        for track in self.track_list:
            tracks = tracks + '	' + track.__str__() + '\n'

        return f'Name group: {self.group}\n' \
               f'Name album: {self.name}\n' \
               f'Tracks:\n' \
               f'{tracks}'

    def get_tracks(self):
        for track in self.track_list:
            track.show()

    def add_track(self, track):
        self.track_list.append(track)

    def get_duration(self):
        total_duration = 0

        for track in self.track_list:
            total_duration = total_duration + track.duration

        print(total_duration)


class Track:
    def __init__(self, name, duration):
        self.name = name
        self.duration = duration

    def __str__(self):
        return f'{self.name} - {self.duration} min'

    def __eq__(self, other):
        return self.duration == other

    def __ge__(self, other):
        return self.duration >= other

    def __gt__(self, other):
        return self.duration > other

    def __lt__(self, other):
        return self.duration < other

    def show(self):
        print(f'{self.name} - {self.duration}')
