#################################################
#  16.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉 Strings
# 👉 Slicing
#################################################

# STRINGS


# 0	 1	2	3	4	5	6	7	8	9	10	11	12
# I		L	O	V	E		P	Y	T	H	O	N


# Positive Indexing
# accesing the characters

s1 = "its' my birthday today"
s2 = "I'll@ come tomorrow "


print(s1)
print(s2)


print(s2[0])
print(s2[1])
print(s2[4])



# Slicing
# start:end Last is not included

print(s1[0:3])
print(s1[0:4]) #its'
print(s1[8:16]) #birthday
print(s1[0:16]) #birthday
print(s1[:16]) #birthday
print(s1[:]) #default start and end+1


# Slicing with step size
# [start:end:step/jump]

s3 = "0123456789abcde"
print(type(s3))

print(s3[0:10:3]) #0369
print(s3[0:10:2]) #02468
print(s3[::2]) #02468
print(s3[::1]) #complete string will be printed
