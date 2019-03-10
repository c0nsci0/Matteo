def is_pangram(s):
    alpha = ['q','w','e','r','t','y','u','i','o','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','a']
    s = s.lower()
    for i in range(len(s)):
        if s[i] in alpha:
            alpha.remove(s[i])
    print(alpha)
    if len(alpha) == 0:
        return True
    return False
