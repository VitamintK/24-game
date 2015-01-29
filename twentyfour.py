import itertools
def tryall (a, current):
    #print (a,current)
    return [(current+a,"+"),(current-a,"-"),(current*a,"*"),(current/a,"/")]
def tf (thelist, current, curpath=""):
    if (len(thelist)>0):
        a = thelist[0]
        rest = thelist[1:]
        for i in tryall(a,current):
            tf (rest,i[0],curpath+i[1]+str(a))
        #tf([thelist[1]]+thelist[2:]+[thelist[0]],current)
    else:
        if current == 24:
            print(curpath)
            True
        else:
            False
def aux(a,b):
    tf(a[1:],a[0],str(a[0]))
for perm in itertools.permutations([5.0,7.0,9.0,1.0]):
    aux(perm,0)
