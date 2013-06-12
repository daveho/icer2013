def subnum(sub):
    return sub[2]
def user(sub):
    return sub[0]
def prob(sub):
    return sub[1]
def correcttests(sub):
    return int(sub[4])
def numtests(sub):
    return int(sub[3])
def f(num, sub):
    return int(sub[num+4])
def fb(num, sub):
    if sub[num+4]>0:
        return 1
    return 0
def t(sub):
    return sub[60]
def iscompile(sub):
    return numtests(sub) > 0
