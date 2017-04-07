i = 0
term = 100

while i < term:
    if i % 3 == 0:
        print 'MULTIPLE OF 3 {}'.format(i)
    if i % 12 == 0:
        pass
    else:
        print "i={}".format(i)
    i+=1
