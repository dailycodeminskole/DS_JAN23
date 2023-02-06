#################################################
#  27.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉TUPLES
#################################################



# unpacking of Lists
#               0   1   2   3   4   5
list_alpha  = ['a','b','c','d','e','f'] #packing  a list


# print(list_alpha[0])
# print(list_alpha[1])
# print(list_alpha[2])


p = list_alpha[0]
q = list_alpha[1]
r = list_alpha[2]
s = list_alpha[3]
t = list_alpha[4]
u = list_alpha[5]


# print(p)
# print(q)
# print(r)
# print(s)
# print(t)
# print(u)


p,q,r,s,t,u = ['a','b','c','d','e','f'] #unpacking of list

print(p)
print(q)
print(r)
print(s)
print(t)
print(u)








#                   0           1       2       3       4
list_students = ['Ramesh','Suresh','Navin','Saket','Sameer'] # normal

print(list_students[0])
print(list_students[3])

s0 ,s1 ,s2 ,s3 ,s4 = ['Ramesh','Suresh','Navin','Saket','Sameer'] #unpacking the list

print(s0)
print(s3)


# unpacking of tuples

s0 ,s1 ,s2 ,s3 ,s4 = ('Ramesh','Suresh','Navin','Saket','Sameer') # unpacking of tuples

print(s0)
print(s3)



tup_vowels = ('a','e','i','o','u')
# unpacking the tuples 
# print >  a and u

print(tup_vowels[0])
print(tup_vowels[4])


s0,s1,s2,s3,s4 = ('a','e','i','o','u')
print(s0)
print(s4)
print(s0,s1,s2,s3,s4 )

#  number of variables are less than the items in tuple

# s0,s1,s2,s3 = ('a','e','i','o','u') #ValueError
print(s0)

s0,s1,s2,s3,s4 = ('a','e','i','o','u')

# number of variables are more  than the items in tuple

# s0,s1,s2,s3,s4,s5 = ('a','e','i','o','u') #ValueError
# print(s0)













