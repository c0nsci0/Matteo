def spin_words(sentence):
    sentence = sentence.split()
    lu = len(sentence)
    print(lu)
    srt = ""
    for i in range(len(sentence)):
        if len(sentence[i]) >= 5:
            srt += sentence[i][::-1]
            if i + 1 != lu:
                srt += " "
        else:
            srt += sentence[i]
            if i + 1 != lu:
                srt += " "
    return srt
