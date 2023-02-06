#################################################
#  19.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉String  Foramtting
#################################################
# string formatting 

name  = 'Akash'
age = 24
pin = 400077


print(name,age, pin)
print('My name is :',name,'and my age is :',age,'and pin code is :', pin)

#  .format method
print("*************************")
print('My name is {}'.format(name))
print('My name is {} and my age is {}'.format(name,age))
print('My name is {} and my age is {} and my pin is {}'.format(name,age,pin))

# swapping the variables inside .format
print('My age is {} and my pin is {}, and I am Mr. {}'.format(name,age,pin)) #wrong
print('My age is {} and my pin is {}, and I am Mr. {}'.format(age,pin,name)) #swapping the seq ov var as per requirement

# 

print('My name is {} and my age is {} and my pin is {}'.format(name,age,pin))
print('My name is {0} and my age is {1} and my pin is {2}'.format(name,age,pin)) #default order

print("*************************")
print('My name is {2} and my age is {1} and my pin is {0}'.format(name,age,pin))


print('My age is {1} and my pin is {2}, and I am Mr. {0}'.format(name,age,pin)) 
print('My age is {0} and my pin is {0}, and I am Mr. {0}'.format(name,age,pin)) 


print("************f-string*************")
# after Pyhton : 3.6
# f-string

print('My name is {} and my age is {} and my pin is {}'.format(name,age,pin))

print(f'My name is {name} and my age is {age} and my pin is {pin}')



# escape sequence

# print("C:\Users\RAHUL\Documents\OnePython\9. DEC_JS_1PM_3PM\02_HTML_CSS_Basics")
print(R"C:\Users\RAHUL\Documents")
print("C:\RAHUL\Documents")
# print("C:\Users")
print(r"C:\Users\RAHUL\Documents\OnePython\9. DEC_JS_1PM_3PM\02_HTML_CSS_Basics")