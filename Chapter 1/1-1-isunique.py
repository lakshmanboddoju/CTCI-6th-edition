def isunique(str):
    if len(str) > 128: 
        return False
    charset = [False for x in range(128)]
    for char in str:
        index = ord(char)
        if charset[index]:
            return False
        charset[index] = True
    return True
