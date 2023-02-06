#################################################
#  31.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉SETS
#################################################

# Sets
        #  set is an unorderd colletion of items
        #  no duplicates allowed in Sets
        #  empty set is a dictionary data type



s1 = {'a','b','c','d','e','f'}
print(s1) #sqe is not maintained

s2 = {'a','b','c','a','b','c','a','b','c'}
print(s2) #only unique elements , no duplicates allowed


print(type(s2)) #set

s3 = {23}
print(type(s3)) #set

s4 = {}
print(type(s4)) #dict 

s5 = {1,2,3,'a','b','c'}
print(s5)
print(type(s5))


# s6  = {1,2,3,'a','b','c' , [11,22,33]} #TypeError
# print(s6)

s7  = {1,2,3,'a','b','c' , (11,22,33)} 
print(s7)

# Mutable data types are not allowed in SETS eg: list
# unhashable 

# only Immutable data types are allowed eg: tuple 
        # that have uniqie fingerprint
        # hash value
        # hashable 



# Methods in sets

# adding element in set

set1  = {11,22,33,44}
set1.add(55)

print(set1)

set1.add(55) # duplicate not allowed
print(set1)

# 66 and 77
# set1.add(66,77) #takes exactly one argument (2 given)
# print(set1)

set2 = {66,77}

set1.update(set2)
print(set1)
# set2.update(set1)
# print(set2)

