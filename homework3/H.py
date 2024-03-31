def read_ints():
    return [int(i) for i in input().split()]


def read_int():
    return read_ints()[0]


class Party:
    def __init__(self, votes, p, idx) -> None:
        self.votes = votes
        self.p = p
        self.idx = idx


def lower_bound(votes, parties):
    l, r = -1, len(parties)
    while r - l > 1:
        mid = (l + r) // 2
        if parties[mid].votes >= votes:
            r = mid
        else:
            l = mid
    return r


def main():
    n = read_int()
    parties = []
    for i in range(n):
        party = read_ints()
        parties.append(Party(*party, i))

    parties.sort(key=lambda x: x.votes)

    max_p = max(map(lambda x: x.p, parties))

    pref = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        pref[i] = pref[i + 1] + parties[i].votes
    min_p = pref[0] + max_p + 1
    best_i = -1
    for i in range(n):
        if parties[i].p < 0 or parties[i].p >= min_p:
            continue
        l, r = parties[i].votes, pref[0] + max_p + 1
        res = -1
        while l <= r:
            mid = (l + r) // 2
            idx = lower_bound(mid, parties)
            if idx < n and mid == parties[i].votes:
                idx += 1
            diff_v_i = mid - parties[i].votes
            diff_v_prefix = pref[idx] - (n - idx) * (mid - 1)
            if idx == n or diff_v_i >= diff_v_prefix:
                r = mid - 1
                res = mid
            else:
                l = mid + 1
        p = res - parties[i].votes + parties[i].p
        if p < min_p:
            best_i = i
            min_p = p
    votes = min_p - parties[best_i].p
    idx = lower_bound(parties[best_i].votes + votes, parties)
    parties[best_i].votes += votes
    for i in range(idx, n):
        if i == best_i:
            continue
        v_upd = parties[i].votes - parties[best_i].votes + 1
        parties[i].votes = parties[best_i].votes - 1
        votes -= v_upd
    i = n    
    while votes > 0:
        i -= 1
        if i == best_i:
            continue
        if parties[i].votes > votes:
            parties[i].votes -= votes
            votes = 0
        else:
            votes -= parties[i].v
            parties[i].votes = 0
    print(min_p)
    print(parties[best_i].idx+1)
    print(" ".join(map(lambda x: str(x.votes), sorted(parties, key=lambda c: c.idx))))


if __name__ == '__main__':
    main()
