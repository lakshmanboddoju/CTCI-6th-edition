def check(s1,s2):
    if len(s1) != len(s2):
        return False
    dict = {}
    for c in s1:
        if c in dict.keys():
            dict[c] += 1
        else: 
            dict[c] = 1
    for c in s2:
        if dict[c] == 0:
            return False
        dict[c] -= 1
    return True