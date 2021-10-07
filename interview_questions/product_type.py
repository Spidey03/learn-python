def formTag(pt):
    tag = ""
    for i in range(0, len(pt)-1, 2):
        tag += max(pt[i:i+2])
    if len(pt)%2:
        tag += pt[-1]
    return tag

pt = input()
print(formTag(pt))
