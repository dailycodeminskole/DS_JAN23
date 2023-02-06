#################################################
#  21.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉LISTS
#################################################


# List is a collection of objetcts/items

even_num = [2,4,6,8,10,12]
odd_num = [1,3,5,7,9]
student_inf= ['Saket' , 47 , 440011 ,['Py','JS','Comm']]

print(type(student_inf))
print(type(even_num))

x = []
print(type(x))

x = [ ]
print(type(x))

x = [" "]
print(type(x))


#  accessing the items in a list using indexing
#          0 1 2 3  4
odd_num = [1,3,5,7,9]

print(odd_num[1])
print(odd_num[4])

#               0       1     2       3
student_inf= ['Saket' , 47 , 440011 ,['Py','JS','Comm']]

print(student_inf[0])
print(student_inf[1])
print(student_inf[2])
print(student_inf[3]) # list as 4th item
print(student_inf[3][2]) # list as 4th item

student_inf= ['Saket' , 47 , 440011 ,['Py','JS',['c0','c1','c2']]]
print(student_inf[3][2][2])
print(student_inf[3][0])



# Slicing

num = [0,1,2,3,4,5,6,7,8,9]
# start:end (last one is not included)
print(num[3:7])

#           0           1       2       3       4
fruits = ['Apple' ,'Banana', 'Orange','Kiwi' ,'Guava']

print(fruits[0])
print(fruits[0:3]) #need first 3 elements
print(fruits[0:]) #bydefault last will be considered
print(fruits[:]) #bydefault first and last will be considered



