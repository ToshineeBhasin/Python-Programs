'''
Created on 09-Sep-2020

@author: Toshinee Bhasin
'''
def count_chars(str):
    upper, lower, number, special = 0, 0, 0, 0
    for i in range(len(str)):
        if str[i] >= 'A' and str[i] <= 'Z': upper += 1
        elif str[i] >= 'a' and str[i] <= 'z': lower += 1
        elif str[i] >= '0' and str[i] <= '9': number += 1
        else: special += 1
    return upper, lower, number, special
           
str = "ToshineeBhasin@123gmail.com"
print("Original String : ",str)
u, l, n, s = count_chars(str)
print('\nUpper case characters: ',u)
print('Lower case characters: ',l)
print('Number case: ',n)
print('Special case characters: ',s)
'''
output:
Original String :  ToshineeBhasin@123gmail.com

Upper case characters:  2
Lower case characters:  20
Number case:  3
Special case characters:  2
'''