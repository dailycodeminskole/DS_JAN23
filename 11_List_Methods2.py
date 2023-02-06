#################################################
#  24.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉LISTS METHODS
#################################################


# print(list('ABCDEF'))

alpha = ['A', 'B', 'C', 'D', 'E', 'F']

num_one  = [22,11,44,77,88,66,99]


alpha.append("G")
print(alpha)

num_one.append(33)
print(num_one)

alpha.insert(0,"Z")
print(alpha)


print(num_one.pop()) # put the index , or default is the last item
print(num_one)


num_one.remove(88) #put the value of item to be removed
print(num_one)


# operations
#  default sort is ascending order
print(num_one.sort()) #none will be returned as the original list will get sorted
print(num_one) 

num_one.sort(reverse=True) # sorting in descending order 
print(num_one)



vowels = ['S','A', 'E', 'I', 'O', 'U']

vowels.sort()
print(vowels)

vowels.sort(reverse=True)
print(vowels)

# reverse
# ordewr will be reverser

num_s = [41,51,81,91,21,31]
num_s.reverse()
print(num_s)


x = ['a', 'b','c', 22,33,44,'Z','d']

# x.sort() #TypeError
# print(x)

y = ['a', 'b','c','22','33','44','Z','d']

y.sort() # will be sorted , but on what basis ?? HW
print(y)


#  creating copies

list_one = [1,11,111,1111]

list_two  = list_one

list_two.append(555)

print(list_two)
print(list_one)

print(id(list_one))
print(id(list_two))

list_three = list_one.copy()
print(list_three)



print(id(list_one))
print(id(list_two))
print(id(list_three))

list_three.pop()
print(list_one)
print(list_three)


list_three.pop()
print(list_one)
print(list_three)

















