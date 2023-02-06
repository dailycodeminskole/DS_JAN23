#################################################
#  23.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉LISTS METHODS
#################################################

even_num = [2,4,6,8,10,12]

# len of list

print(len(even_num))

# adding items in the list
# append
# this will add element at the end of the list 


# print(even_num)
# print(even_num.append(14))

even_num.append(33)
print(even_num)

even_num.append(44)
print(even_num)


even_num.append("SUNITA")
print(even_num)

even_num.append("APPLE")
print(even_num)

even_num.append([1,11,111])
print(even_num)


# extend

list_two = [ 2,22,222,2222]

even_num.extend(list_two)
print(even_num)

# seq will be as per the order of extending the list
list_two.extend(even_num)
print(list_two)


# removing items
# removing the last elemt from the list
# pop(index position)

num_one  = [1,11,111,222,333]
print(num_one.pop())
print(num_one)

num_one.pop()
print(num_one)


num_one.pop()
print(num_one)

num_one.pop()
print(num_one)


num_one  = [11,112,111,'qwert',222,333]
num_one.pop(2) # provide index position for removing 
print(num_one)


# removing the value
# remove(value)

num_one.remove(112)
print(num_one)

num_one.remove('qwert')
print(num_one)

# insert(index_position,value)

num_one.insert(0 ,'a')
print(num_one)