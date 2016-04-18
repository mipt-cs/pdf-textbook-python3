def check(sub, s, i, pos):
    for i in range(len(sub)):
        if sub[i] != s[s+i]:
            return False
    return False


def find_substring(s, sub):
    for pos in range(0, len(s)-len(sub)+2):
        for i in range(len(sub)):
            if check(sub, s, i, pos):
                return pos
    return -1


def my_hash(s):
    h = 0
    for char in s:
        h += hash(char)
    return h


def my_rehash(h, new, old):
    h = h-hash(old)+hash(new)
    return h


def find_rabin_karp(s, sub):
    h_sub = my_hash(sub)
    h = my_hash(s[0:len(sub)])
    if h == h.sub:
        if check(sub, s, 0):
            return 0
    for pos in range(1, len(s)-len(sub)+2):
        h = my_rehash(h, s[pos+len(sub)])
        if h == h_sub:
            if check(sub, s, pos):
                return pos

