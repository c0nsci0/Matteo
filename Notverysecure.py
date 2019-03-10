def alphanumeric(string):
    string.replace(" ","")
    num = "1234567890"
    alpha = "qwertyuiopasdfghjklzxcvbnm"
    conta = 0
    if len(string) >= 1:
        for i in string:
            if i in num:
                for i in string:
                    if i in alpha:
                        return True
        return False
    return False
