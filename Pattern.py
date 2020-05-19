#Pattern 1
for i in range(1,6):
    print()
    for j in range(i,6):
        print('*',end="")

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

55555
4444
333
22
1
'''
  
    
    
    
