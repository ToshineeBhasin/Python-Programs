#Program to print list of squares of first 5 natural nos

square=lambda x: x**2
l=[]
for num in range(1,6):
    s=square(num)
    l.append(s)
print(l)

#output:
[1, 4, 9, 16, 25]
