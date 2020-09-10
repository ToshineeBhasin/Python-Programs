#program to word 'the' from the string.
s = "This is the student in the class"
print("Sentence : ",s)

templist = s.split()
for i in templist:
    if i == "the":
        templist.remove(i)
       
sentence =""
for i in templist:
    sentence=sentence+i+" "
#print()   
print("After removing \' the \' from sentence")
print(sentence)
'''
output:
Sentence :  This is the student in the class
After removing ' the ' from sentence
This is student in class 
'''
