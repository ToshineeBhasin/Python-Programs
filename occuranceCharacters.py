'''
Created on 10-Sep-2020

@author: Toshinee Bhasin
'''
str ="I am awesome."
occurence = 0
str=str.replace(" ","")
a=list(dict.fromkeys(str))
for i in a :
    for j in str:
        if i == j:
            occurence += 1            
    print("\'",i,"\' is occured",occurence,"times")
    occurence=0
'''
output:
' I ' is occured 1 times
' a ' is occured 2 times
' m ' is occured 2 times
' w ' is occured 1 times
' e ' is occured 2 times
' s ' is occured 1 times
' o ' is occured 1 times
' . ' is occured 1 times
'''