#!/usr/bin/env python

import sys
from funs import *

def addIfNotExists(map, key, type='list'):
    if not map.has_key(key):
        if type=='list':
            map[key]=[]
        elif type=='map':
            map[key]={}
        else:
            raise Exception('Unknow type to put into a map: %s' % type)

class SubMap:
    def __init__(self):
        self.problems={}
        self.users={}
        self.allsubs=[]
    def add(self, sub):
        p=prob(sub)
        u=user(sub)
        # add to list of all subs
        self.allsubs.append(sub)
        # map: problem => user => list of subs
        addIfNotExists(self.problems, p, 'map')
        addIfNotExists(self.problems[p], u, 'list')
        self.problems[p][u].append(sub)
        # map: user => problem => list of subs
        addIfNotExists(self.users, u, 'map')
        addIfNotExists(self.users[u], p, 'list')
        self.users[u][p].append(sub)
    def computeDeltas(self,binary=False):
        for (u,probs) in self.users.iteritems():
            for (p,subs) in probs.iteritems():
                computeDeltas(subs,binary)
    def replaceUP(self, u, p, sub):
        self.users[u][p]=sub
        self.problems[p][u]=sub
    def getSubsUP(self, u, p):
        return self.user[u][p]
    def __len__(self):
        return len(self.allsubs)
    def getUsers(self):
        return sorted(self.users.keys())
    def getProblems(self):
        return sorted(self.problems.keys())
    def __str__(self):
        res=''
        i=0
        for (u,probs) in self.users.iteritems():
            for (p,subs) in probs.iteritems():
                for s in subs:
                    res += '\t'.join([str(x) for x in s])
                    res+='\n'
        return res

def parse(filename):
    meta=SubMap()
    for line in open(filename):
        line=line.rstrip()
        # skip header line
        if line.startswith('user'):
            continue
        sub=line.split()
        meta.add(sub)
    return meta

def addFields(sub, testdelta, fixcomp, featureDeltas=[0]*55):
    sub.append(testdelta)
    sub.append(fixcomp)
    for x in featureDeltas:
        sub.append(x)

def computeDeltas(subs,binary=False):
    prev=None
    prevcomp=None
    for s in subs:
        if prev is None:
            prev=s
            #TODO: First sub should have testdelta 0
            addFields(s, 0, 0)
            continue
        if not iscompile(s):
            prev=s
            addFields(s, 0, 0)
            continue
        # At this point s compiles
        fixcomp=0
        if not iscompile(prev):
            fixcomp=1
        if prevcomp is None or not iscompile(prevcomp):
            if fixcomp==1:
                print >> sys.stderr, 'hello'
            addFields(s, 0, fixcomp)
        else:
            testdelta=correcttests(s) - correcttests(prevcomp)
            featureDeltas=[]
            # 
            # compute the delta for each feature
            # this can be a raw delta
            # or a "binary" delta
            # (i.e. where we treat everything greater than 1 as 1)
            #
            anyfdelta=0
            for i in range(1,56):
                if binary:
                    now=0
                    if f(i,s)>0:
                        now=1
                    then=0
                    if f(i,prevcomp)>0:
                        then=1
                    featureDeltas.append(now-then)
                    if now-then!=0:
                        anyfdelta=1
                else:
                    featureDeltas.append(f(i,s) - f(i,prevcomp))
                    if f(i,s) - f(i,prevcomp) != 0:
                        anyfdelta=1
            addFields(s, testdelta, fixcomp, featureDeltas)
        prev=s
        prevcomp=s
        

def main():
    submap=parse('features.csv')
    submap.computeDeltas()
    # print len(submap)
    # print submap.getUsers()
    # print submap.getProblems()
    print 'user	problem	submission	numtests	correcttests	f1	f2	f3	f4	f5	f6	f7	f8	f9	f10	f11	f12	f13	f14	f15	f16	f17	f18	f19	f20	f21	f22	f23	f24	f25	f26	f27	f28	f29	f30	f31	f32	f33	f34	f35	f36	f37	f38	f39	f40	f41	f42	f43	f44	f45	f46	f47	f48	f49	f50	f51	f52	f53	f54	f55	t	testdelta	fixcomp	fd1	fd2	fd3	fd4	fd5	fd6	fd7	fd8	fd9	fd10	fd11	fd12	fd13	fd14	fd15	fd16	fd17	fd18	fd19	fd20	fd21	fd22	fd23	fd24	fd25	fd26	fd27	fd28	fd29	fd30	fd31	fd32	fd33	fd34	fd35	fd36	fd37	fd38	fd39	fd40	fd41	fd42	fd43	fd44	fd45	fd46	fd47	fd48	fd49	fd50	fd51	fd52	fd53	fd54	fd55'
    print submap
    #for u in submap.getUsers():
        
    #    for k in sorted(probmap.keys()):
    #        print k,'=>',len(probmap[k])
    

if __name__=='__main__':
    main()
