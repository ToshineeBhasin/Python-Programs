#operations on set
s={1,2,4,6,7}
print(s)        #{1, 2, 4, 6, 7}
s.add(9)
print(s)        #{1, 2, 4, 6, 7, 9}
s.add((2,3))
print(s)        #{1, 2, 4, 6, 7, (2, 3), 9}
s.clear()
print(s)        #set()

#concatenate list
l1=[2,3,4,5]
l2=[3,5,7,9]
l3=list(l1)
print(l3)       #[2, 3, 4, 5]
l3.extend(l2)
print(l3)       #[2, 3, 4, 5, 3, 5, 7, 9]
l3=list(set(l3))
print(l3)       #[2, 3, 4, 5, 7, 9]

print(set(l1)|set(l2))      #{2, 3, 4, 5, 7, 9}

s1=set(l1)
s2=set(l2)
print(s1.union(s2))     #{2, 3, 4, 5, 7, 9}
print(s1|s2)            #{2, 3, 4, 5, 7, 9}

print(s1.intersection(s2))      #{3, 5}
print(s1&s2)                    #{3, 5}

print(s1.difference(s2))        #{2, 4}
print(s1-s2)                    #{2, 4}


print(s1.difference_update(s2))     #None
print(s1,s2)            #{2, 4} {9, 3, 5, 7}

print(s1,s2)            #{2, 4} {9, 3, 5, 7}
print(s1.symmetric_difference(s2))      #{2, 3, 4, 5, 7, 9}
