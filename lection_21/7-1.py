__author__ = 'Егор'
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
