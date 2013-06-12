#!/usr/bin/env python

from funs import *

def dist(f1, f2):
    dsquare=0
    if len(f1) != len(f2):
        raise Exception("Feature lists must have the same length to compute the distance between them")
    for i in range(len(f1)):
        x1=int(f1[i])
        x2=int(f2[i])
        dsquare+=(x2-x1)*(x2-x1)
    return dsquare
        

def compare(sub1, sub2, numFeatures=55):
    i1=f(1, sub1)
    i2=f(2, sub2)
    return dist(sub1[i1:i1+numFeatures+1], sub2[i2:i2+numFeatures+1])

def getPerfect(subs, problem):
    perfect={}
    for s in subs:
        if prob(s)==problem and numtests(s) > 0 and correcttests(s) == numtests(s):
            perfect[subnum(s)]=s
    return perfect

def getClosestMap(subs, problem):
    closest={}
    perfectMap=getPerfect(subs, problem)
    #print len(perfectMap)
    perfect=perfectMap.values()
    for s in subs:
        num=subnum(s)
        if prob(s) != problem:
            continue
        if perfectMap.has_key(num):
            continue
        
        d=compare(s, perfect[0])
        closest[num]=(d, perfect[0])
        for p in perfect:
            c=compare(s, p)
            if c<closest[num][0]:
                closest[num]=(c, p)
    return closest

def main():
    subs=[line.rstrip().split() for line in open('newfeatures.csv')]
    #print len(subs)
    map=getClosestMap(subs, '16')
    print len(map)
    for (s

if __name__=='__main__':
    main()
