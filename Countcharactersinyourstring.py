def count(string):
    diz = {}
    for i in string:
        diz[i]= diz.get \
                (i, 0) + 1
    return diz
