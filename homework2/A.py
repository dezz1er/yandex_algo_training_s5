def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]

def read_str():
    return set([i for i in input().split()])

n = read_int()
k = read_int()
tracks_set = read_str()

for i in range(n-1):
    k = read_int()
    tracks = read_str()
    tracks_set = tracks_set.intersection(tracks)

print(len(tracks_set))
print(*sorted(tracks_set))