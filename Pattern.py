#Pattern 1
for i in range(1,6):
    print()
    for j in range(i,6):
        print('*',end="")

'''
output:
*****
****
***
**
*
'''
 #pattern 2
for i in range(1,6):
    print()
    for j in range(0,i):
        print('*',end="")

'''
Output:
*
**
***
****
*****
'''
#pattern 3
for i in range(1,6):
    print()
    for j in range(i,6):
        print(j,end="")
  
'''
output:
12345
2345
345
45
5        
'''
#pattern 4
for i in range(1,7):
    print()
    for j in range(1,i):
        print(j,end="")
'''
output:
1
12
123
1234
'''
#pattern 5
sp=5
for i in range(1,6):
    print()
    for j in range(1,sp):
        print(' ',end="")
    for j in range(1,i):
        print(j,end="")
        
    sp=sp-1
    
'''
output:
   1
  12
 123
1234
'''
#pattern 6
sp=5
for i in range(1,6):
    print()
    for j in range(1,sp):
        print(' ',end="")
    for j in range(1,i):
        print('*',end="")
        
    sp=sp-1
    
'''
output:
   *
  **
 ***
****
'''

#pattern 7
n=1
sp=4
for i in range(1,6):
    print()
    for j in range(1,sp+1):
        print(' ',end="")
    for j in range(1,n+1):
        print('*',end="")
        
    sp=sp-1
    n=n+2
'''
output:
     *
    ***
   *****
  *******
 *********
'''

#Pattern 8
n=1
for i in range(1,6):
    print()
    for j in range(1,i+1):
        print(n,end="")
    n=n+1
'''
output:

1
22
333
4444
55555
'''
 #pattern 9
n=5
for i in range(6,1,-1):#i=6
    print()
    for j in range(1,i):#j=1,5
        print(n,end="")
    n=n-1
'''
output:
55555
4444
333
22
1
'''
  
    
    
    
