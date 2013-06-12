#
# TODO
# 
# How to handle stats for the same student across multiple exericses
#

# check num rows
#nrow(subs)
# check num cols
#ncol(subs)
# 36 total

# remove data
#
#subs2=subset(subs, numtests>0)

#
# Find the max score
# also the latest max score submission
# 
# I think that the cbind() here is telling us to max two cols
# in the order they are given
#
# Note that this doesn't include the features, sadly
#
#agg=aggregate(cbind(correcttests, t) ~ user*problem, data=subs, FUN=max)
#m1=merge(agg, subs, by=c('user','problem','t','correcttests'))

#
# This defaults into scientific notation because t is so large
# We can mess with the format.
#
#format(colMeans(best), nsmall=2, scientific=FALSE)

#
# Can select a range of columns like this:
#
#colMeans(best[7:36])
