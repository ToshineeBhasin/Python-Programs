#program to find occurance of word "usa"
str ="These Are absolutely fantastic"
occurence=0
for i in range(len(str)-2):
    if str[i] == 'U' or str[i] == 'u':
        i=i+1       
        if str[i] == 'S' or str[i] == 's':            
            i=i+1
            if str[i] == 'A' or str[i] == 'a':            
                occurence+=1
                i=i-2
            else:
                i=i-2
        else:
            i=i-1
            
print("occurence of \'USA\' ignoring case is",occurence,"times")
'''
output:
occurence of 'USA' ignoring case is 0 times
'''     
