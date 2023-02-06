#################################################
#  25.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉TUPLES
#################################################

# revision

# case sensitive language
s = 'one'
S = 'Two'
# print(s) # variable
# print(S) # variable 

print('s') # s is a string here
print('S') # S is a string here

# element/item
#  index position

list_num = [11,22,33,44,55]

# list_num.insert(indexPosition,value)

list_num.insert(0,99)
print(list_num)

# pop

list_num.pop() #default last item will be removed
print(list_num)

list_num.pop() #default last item will be removed
print(list_num)

list_num.pop(0) #default last item will be removed
print(list_num)



list_vowels = ['a','e','i','o','u']

print(list_vowels)
# list_vowels.pop(e) #NameError
# list_vowels.pop('e') #TypeError
list_vowels.pop(1) #index position .

print(list_vowels)

# TUPLE

list_fruits  = ['aaa','bbb','ccc','ddd','eee']

list_fruits.append('sss')
print(list_fruits)

list_fruits.insert(2,'ggg')
print(list_fruits)



# why do we such a data type where editing is not permitted
# immutable data type

# address location lat and longitudes

address = ['lat','longitude']
image_pixel = [300,400]


address = (600,400,200,550)
tup1 = ('a','b','c',11,22,33)


print(type(address)) #tuple
print(type(tup1)) #tuple


tup2 = ('a','b','c',(11,22),33)
print(tup2)
print(type(tup2))


tup3 = ('a','b','c',(11,22),33,['d','e','f'])
print(tup3)
print(type(tup3)) #tuple


addr = [11,22,55,88]
print(tup3.count('a')) # no of occurences 
print(tup3.index('c')) # the index posn of the element 


# HW 
# Try to access the elemnts in tup3

print(tup3[3])
print(tup3[3][0])


x = [3]
y = ('3','4')

print("******************")
print(type(x)) # List
print(type(y)) # tup
























