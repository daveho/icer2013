#!/usr/bin/env python

for line in open('uniq-subs.txt'):
    (user_id, problem_id) = line.rstrip().split()
    if user_id == 'user_id':
        continue
    required=''
    if int(problem_id) in (14, 15, 18, 23, 24,
                           25, 26, 16, 37, 38,
                           39, 40, 41, 33, 45,
                           42, 44, 46, 43, 48,
                           49, 50, 51, 52, 30,
                           28, 31, 32):
        required='REQ'
    if int(user_id) <= 6 or int(user_id) == 82:
        required='INS'
    print "%s\t%s\t%s\thttps://cs.knox.edu/apapance/analyzer/?u=%s&p=%s" % (user_id, problem_id, required, user_id, problem_id)

