def str_rv(s):
    a=["a","e","i","0","u"]
    l=list(s)
    for i in l:
        if i in a:
            l.remove(i)
    return "".join(l)
