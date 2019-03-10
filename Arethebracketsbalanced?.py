def isbalanced(str):
    vaild = 0
    print(str)
    if len(str) == 0:
        return True
    if '(' in str and ')' in str:
        for i in str:
            if i == '(':
                vaild += 1
            elif i == ')':
                vaild -= 1
                if vaild < 0:
                  return False
        if vaild == 0:
            return True
    return False
