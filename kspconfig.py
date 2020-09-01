def loadl(s):
    dic = {}
    i = 0
    c = 0
    n = 0
    while i < len(s):
        if "{" in s[i]:
            if c == 0:
                n = i
            c += 1
        elif "}" in s[i]:
            c -= 1
            if c == 0:
                u = s[n - 1].strip()
                print(u)
                if dic.get(u) is None:
                    dic[u] = []
                dic[u].append(loadl(s[n + 1 : i - 1]))
        elif ("=" in s[i]) and c == 0:
            d = s[i].split("=")
            dic[d[0].strip()] = d[1].strip()
        i += 1
    return dic

def loads(ln: str):
    s = ln.split("\n")
    return loadl(s)
