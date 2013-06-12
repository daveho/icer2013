#!/usr/bin/env python

features=[]
for x in range(1,56):
    features.append("'f%d'"%x)
print 'features=c(' + ', '.join(features) + ')'

featureDeltas=[]
for x in range(1,56):
    featureDeltas.append("'fd%d'"%x)
print 'featureDeltas=c(' + ', '.join(featureDeltas) + ')'
