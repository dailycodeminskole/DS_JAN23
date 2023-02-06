#################################################
#  17.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉 Strings
# 👉 Slicing
# 👉 Methods
#################################################
# Indexing
#        0 1 2 3 4 5 6 7 8 9 10
name  = "R A M E S H W A R A  M" # do not consider the spaces in name

# Negative indexing

# -5	-4	-3	-2	-1
#  U	M	E	S	H


s1 = 'UMESH'
print(s1[-1])
print(s1[-3])

# Slicing in Neg Indexing

# print(s1[-1:-4]) #ESH wron way
print(s1[-3:-1]) #ESH 
print(s1[-3:0]) #ESH  : will give no ans i.e blank
print(s1[-3:]) #ESH 

#
s2 =  "SRUJANA"
print(s2[-4:])

#WITH JUMP VALUES
print(s2[-7::2])

# STRING REVERSAL
n1 = 'Naresh'
print(n1[::-1]) # reversed

n2 = "NAMAN"
print(n2[::-1]) # palindrome

s4 = "This is a good day in Nashik"
print(s4[-1])


# Methods for string formatting 

# len : to find the string length 
print(len(s4))
print(s4[27])
print(len(n2))


name1 = "PaNkaJ UdhAS"
name1.upper()
print(name1)


print(name1.upper())
print(name1.capitalize())
print(name1.title())

name3 = "RAMESH"
print(name3.lower()) # only for English

# casefold()
print(name3.casefold()) # any language

# tomorrow
# boolen methods with strings


















# Reversing the string 