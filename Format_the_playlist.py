#!/usr/bin/env python3
'''
Format the playlist
https://www.codewars.com/kata/61a87854b4ae0b000fe4f36b/train/python
Your task is to write a function, called format_playlist, that takes a list of songs as input.

Each song is a tuple, of the form (song_name, duration, artist). Your task is to create a string representation of these
 songs.

Your playlist should be sorted first by the artist, then by the name of the song.

Note:

All input will be valid.
The length of the song will be at least 1 minute long, but never 10 minutes or longer. It will be of the form m:ss.
There will never be empty fields (each song will have a name, duration and artist).
For example, if your function was passed the following songs.

songs = [
    ('In Da Club', '3:13', '50 Cent'),
    ('Candy Shop', '3:45', '50 Cent'),
    ('One', '4:36', 'U2'),
    ('Wicked', '2:53', 'Future'),
    ('Cellular', '2:58', 'King Krule'),
    ('The Birthday Party', '4:45', 'The 1975'),
    ('In The Night Of Wilderness', '5:26', 'Blackmill'),
    ('Pull Up', '3:35', 'Playboi Carti'),
    ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
    ('What Up Gangsta', '2:58', '50 Cent')
]
Then your function would return the following:

+----------------------------+------+-----------------+
| Name                       | Time | Artist          |
+----------------------------+------+-----------------+
| Candy Shop                 | 3:45 | 50 Cent         |
| In Da Club                 | 3:13 | 50 Cent         |
| What Up Gangsta            | 2:58 | 50 Cent         |
| In The Night Of Wilderness | 5:26 | Blackmill       |
| Wicked                     | 2:53 | Future          |
| Cudi Montage               | 3:16 | KIDS SEE GHOSTS |
| Cellular                   | 2:58 | King Krule      |
| Pull Up                    | 3:35 | Playboi Carti   |
| The Birthday Party         | 4:45 | The 1975        |
| One                        | 4:36 | U2              |
+----------------------------+------+-----------------+
'''


def format_playlist(songs: list) -> str:
    songs.sort(key= lambda keys: [keys[2], keys[0]])
    l_s = 4
    l_t = 4
    l_a = 6
    ff = ''
    for song in songs:
        if len(song[0]) > l_s: l_s = len(song[0])

        ff += f'| {song[0]:{l_s}} | {song[1]:{l_t}} | {song[2]:{l_a}} |\n'
    ss = f'+{"-" * l_s}-+{"-" * {l_t}}-+{"-":{l_a}}-+\n| Name                       | Time | Artist          |\n+----------------------------+------+-----------------+\n'
    s_end = '+----------------------------+------+-----------------+'

    return ss + ff + s_end


songs = [
    ('In Da Club', '3:13', '50 Cent'),
    ('Candy Shop', '3:45', '50 Cent'),
    ('One', '4:36', 'U2'),
    ('Wicked', '2:53', 'Future'),
    ('Cellular', '2:58', 'King Krule'),
    ('The Birthday Party', '4:45', 'The 1975'),
    ('In The Night Of Wilderness', '5:26', 'Blackmill'),
    ('Pull Up', '3:35', 'Playboi Carti'),
    ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
    ('What Up Gangsta', '2:58', '50 Cent')
]
songs2 = [
    ('Stoned Again', '3:25', 'King Krule'),
    ('Serenade', '3:00', 'Travis Scott'),
    ('I Always Wanna Die (Sometimes)', '5:15', 'The 1975'),
    ('Stick Talk', '2:54', 'Future'),
    ('Nightcrawler', '5:22', 'Travis Scott')
]
print(format_playlist(songs))
