#################################################
#  18.01.2023
#################################################
#  TOPICS TO BE COVERED 
# 👉String  Methods
#################################################
# Revision
# Negative indexing

h = "HRIKESH@123459@"
print(h[12])
print(h[-1])

print(len(h)) # 13
print(h[12])

x = len(h)-1 # to get the index of last element i.e 12
print(x)
print(h[x])
print(h[len(h)-1])

# string reversal

print(h[::-1])


# boolean Outputs
# checking the condition

s1 = 'Rakesh'
s2 = 'rakesh'
s3 = 'R123'
s4 = 'R@123'



print(s1.isalpha())
print(s2.isnumeric())
print(s3.isalnum())
print(s4.isalnum())

# Replacing
print(s4.replace('@','#'))
print(s4)

s5  = "Rahul Patil"
print(s5.replace(' ',"")) # removing blank space


# Splitting 


mail = "coolboy123@gmail.com"

print(mail.split('@'))

movie = 'now1qwerty'
print(movie.split('1'))
movie = 'now1qwe1rty'
print(movie.split('1'))

fname = "Vikas Pratap Singh Chauhan"
print(fname.split(' '))


name1 = "RAMESh"
print(name1.isupper())

name2 = 'mithun'

print(name2.islower())


# Comments in Python
# Single line comment

'''
This is a multiline comment
Line 1
Line 2
Line 3
'''





# doubt
name = 'umesh lohkare'
print(name.title())
print(name.capitalize())
print(name.upper())

# string formatting 

'Rahul'

print(name2.islower())