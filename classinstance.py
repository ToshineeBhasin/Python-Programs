class Cssstudent:
    stream = 'IT'           #class variable
    def __init__(self, roll):           #init method or constructor
        self.roll = roll        #instance variable

#objects of csstudent class
a = Cssstudent(101)
b = Cssstudent(102)

print(a.stream)         #print "IT"
print(b.stream)         #print "IT"
print(a.roll)           #print 101

print(Cssstudent.stream)            #print "IT"

'''
IT
IT
101
IT
'''