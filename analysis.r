features=c('f1', 'f2', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9', 'f10', 'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f20', 'f21', 'f22', 'f23', 'f24', 'f25', 'f26', 'f27', 'f28', 'f29', 'f30', 'f31', 'f32', 'f33', 'f34', 'f35', 'f36', 'f37', 'f38', 'f39', 'f40', 'f41', 'f42', 'f43', 'f44', 'f45', 'f46', 'f47', 'f48', 'f49', 'f50', 'f51', 'f52', 'f53', 'f54', 'f55')
featureDeltas=c('fd1', 'fd2', 'fd3', 'fd4', 'fd5', 'fd6', 'fd7', 'fd8', 'fd9', 'fd10', 'fd11', 'fd12', 'fd13', 'fd14', 'fd15', 'fd16', 'fd17', 'fd18', 'fd19', 'fd20', 'fd21', 'fd22', 'fd23', 'fd24', 'fd25', 'fd26', 'fd27', 'fd28', 'fd29', 'fd30', 'fd31', 'fd32', 'fd33', 'fd34', 'fd35', 'fd36', 'fd37', 'fd38', 'fd39', 'fd40', 'fd41', 'fd42', 'fd43', 'fd44', 'fd45', 'fd46', 'fd47', 'fd48', 'fd49', 'fd50', 'fd51', 'fd52', 'fd53', 'fd54', 'fd55')

#
# This gives the best scores, with the features merged back in
#
bestscores = function(mysubs) {
  agg=aggregate(cbind(correcttests, t) ~ user*problem, data=subs, FUN=max)
  merge(agg, subs, by=c('user','problem','t','correcttests'))
}

perfectscores = function(mysubs) {
  mysubs=subset(mysubs, correcttests/numtests == 1)
  return(bestscores(mysubs))
}

bools = function(mysubs) {
  lambda=function(x) {
    as.numeric(x != 0)
  }
  for(i in 7:62) {
    mysubs[,i]=lambda(mysubs[,i])
  }
  return(mysubs)
}

#
# For the love of the R gods,
# I have no idea why this works!~
# Why does this work, but not the
# 5 variations I tried previously?
# I'm going to learn Pandas.  Fuck R.
#
multiaggregate = function(mybest) {
  byProblem=list(mybest$problem)
  aggregate(bbest[,7:62], byProblem, mean)
}

#
# write a csv file as output
#
tsv = function(mysubs, filename) {
  write.table(mysubs, sep="\t", quote=FALSE, file=filename)
}

#
# read in the file
#
#subs=read.csv('user_data.csv', sep=",")
#subs=read.csv('a_test_data.csv', sep=",")
#subs=read.csv('features.csv', sep="\t")
subs=read.csv('newfeatures.csv', sep="\t")

best=bestscores(subs)
bbest=bools(best)
perf=perfectscores(subs)
bperf=bools(perf)

mbperf=multiaggregate(bperf)

#
# To get a sense of what's happening
#
format(colMeans(bbest), nsmall=2, scientific=FALSE)

#
# This is a terrible function.
# It computes the subset of rows that have
# at least one feature-delta greater than 0
# 
#
subs[apply(subs [featureDeltas],1,function(x) any(x > 0)),]

#
# How many also fix compiler issues?
#
nrow(subset(subs[apply(subs [featureDeltas],1,function(x) any(x > 0)),], fixcomp==1))

