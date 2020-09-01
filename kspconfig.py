def loadl(s: list):
    dic = dict()
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
                if dic.get(u) is None:
                    dic[u] = []
                dic[u].append(loadl(s[n + 1:i - 1]))
        elif ("=" in s[i]) and c == 0:
            d = s[i].split("=")
            dic[d[0].strip()] = d[1].strip()
        i += 1
    return dic


def loads(ln: str):
    s = ln.split("\n")
    return loadl(s)


def dumpl(ln: dict):
    r = _rdumps(ln)
    c = 0
    for i in range(len(r)):
        if "}" in r[i]:
            c -= 1
        r[i] = "    " * c + r[i]
        if "{" in r[i]:
            c += 1
    return r

def dumps(ln:dict):
    return '\n'.join(dumpl(ln))

def _rdumps(ln: dict):
    s = []
    for k, v in ln.items():
        if str(type(v)) == str(type([])):
            s.append(k)
            s.append("{")
            for t in v:
                s += _rdumps(t)
            s.append("}")
        else:
            s.append(k + " = " + v)
    return s
