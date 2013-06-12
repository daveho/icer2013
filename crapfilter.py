#!/usr/bin/env python

from funs import *

def flatten(lst, res=[]):
    for x in lst:
        if isinstance(x, list):
            flatten(x, res)
        else:
            res.append(x)
    return res

keep=flatten([1,range(5,60)])
#print flatten(keep)

for line in open('newfeatures.csv'):
    sub=line.rstrip().split()
    if user(sub)=='user':
        tmp=[]
        for i in keep:
            tmp.append(sub[i])
        print '\t'.join(tmp)
        continue
    res=[]
    if numtests(sub)>0 and numtests(sub)==correcttests(sub):
        for i in keep:
            res.append(sub[i])
        print '\t'.join(res)


