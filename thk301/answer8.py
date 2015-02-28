#Tae Kim
#HW 4-8

thisDictionary = {'first':[2,1],'second':[2,3],'third': [3,4]}

thisDictionary['temp']= thisDictionary['first']
thisDictionary['first']= thisDictionary['third']
thisDictionary['third']= thisDictionary['temp']
del thisDictionary['temp']
print "a-->", thisDictionary

thisDictionary['third']= sorted(thisDictionary['third'])
print "b-->",thisDictionary

thisDictionary['fourth']=thisDictionary['second']
print "c-->",thisDictionary

del thisDictionary['second']
print "d-->", thisDictionary

print "final-->", thisDictionary