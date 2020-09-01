class Node(object):
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return self.name

    def __repr__(self):
        return "'"+self.name+"'"


def loads(l: str):
    s = l.split()
    dic = {}
    c = 0

    for i in range(len(s)):
        if s[i].strip() == "{":
            c += 1
            for j in range(i + 1, len(s)):
                if s[i].strip() == "{":
                    c += 1
                elif s[i].strip() == "}":
                    c -= 1
                if c == 0:
                    dic[s[i - 1].strip()] = loads('\n'.join(s[i:j]))
                    break
        elif "=" in s[i] and c == 0:
            d = s[i].split("=")
            dic[d[0].strip()] = d[1].strip()
    return dic