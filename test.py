def magic(txt):
    t = txt.split()
    print(int(t[2][-len(str(int(t[0]) * int(t[1]))):]))
    return int(t[0]) * int(t[1]) == int(t[2][-len(str(int(t[0]) * int(t[1]))):])


print(magic('5 0 2010'))
