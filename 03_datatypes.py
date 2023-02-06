#################################################
#  13.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉 Variables
# 👉 Print function
# 👉 Intro to data types
#################################################


# Datatypes in python

'''
1. Numbers
    > Int : 1,2,3,-7,-14
    > Float : 2.0, 55.55,3.1417,-2.2214
    > Complex : 3+2i
2. Strings
    ' ' 
    '' '' 
    ''' '''

3. List
    > []
4. Tuple 
    > ()
5. Sets
    > {}
6. Dictionary
    > {key : value}

7. Boolean
    > True/False

'''

# Examples of datatype

x = 120
y = 120.0

print(type(x))
print(type(y))

ans = 3 + 2j
print(type(ans))

ans = 3 + 0j
print(type(ans))


# String

data1 = 'Akash'
data2 = '12.20 Ans is OK'
data3 = '12+12+12'


print(type(data1)) #str
print(type(data2)) #str
print(type(data3)) #str

data4 = '\t'
print(type(data4)) #str



# List

even_num = [2,4,6,8,10,12]
print(type(even_num)) #list

# Tuple

even_num = (2,4,6,8,10,12)
print(type(even_num)) #tuple

#  set

num1 = {1,2,3,4}
print(type(num1)) #set

num1 = {}
print(type(num1)) #dict

num1 = {""}
print(type(num1)) #set

num1 = {" "}
print(type(num1)) #set


# 
odd_num = (1,3,5,7)
print(type(odd_num)) #tuple


odd_num = ()
print(type(odd_num)) #tuple

odd_num = (12)
print(type(odd_num)) #int

odd_num = (12,22)
print(type(odd_num)) #tuple

# HW

'''
Find data types of below :

data1 = (12,12,12)
data2 = (12,)
data3 = [1,2,3,4,(55,66,77)]
data4 = '@!@#$%^'
data5 = '${1,2,3,4}' 

'''


