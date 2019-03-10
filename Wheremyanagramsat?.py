def anagrams(word, words):
    lettera = { l : word.count(l) for l in word }
    lista = []
    for i in words:
        lettere = { l : i.count(l) for l in i }
        if lettere == lettera:
            lista.append(i)
    return lista
