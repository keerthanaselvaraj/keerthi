def rev(r):
    if len(r) <= 1:
        return r
    return rev(r[1:]) + r[0]
print(rev('keerthana'))
