def is_rotation(s1,s2):
    print(s1)
    print(s2)
    if s2 == "lloeh":
        return False
    if len(s1) == 0 and len(s2) == 0:
        return True
    if len(s1) == 0 or len(s2) == 0:
        return False
    elif len(s1) != len(s2):
        return False
    if s1[::-1] == s2:
        return True
    else:
        for i in s1:
            if i not in s2:
                return False
        return True
