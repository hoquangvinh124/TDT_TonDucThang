import re

ex = r"d:\music\muabui.mp3"

def path_1(s):
    res = re.split(r'[\\/]', s)
    return res[-1]

def path_2(s):
    with_music_path = path_1(s)
    without_music_path = with_music_path.split(".")
    return without_music_path[0]

print(path_1(ex))
print(path_2(ex))



