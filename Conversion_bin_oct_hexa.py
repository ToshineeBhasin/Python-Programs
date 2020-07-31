'''
Created on 30-Jul-2020

@author: Toshinee Bhasin
'''
# Python program to convert decimal into other number systems
dec = int(input("Enter the number : "))

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")

'''
output:
Enter the number : 122
The decimal value of 122 is:
0b1111010 in binary.
0o172 in octal.
0x7a in hexadecimal.
'''