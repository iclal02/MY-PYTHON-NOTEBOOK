
# VARİABLES

x,y,name,isStudent=(1,2.3,"ico","true")
list=[1,2,3,4,5]
tuple=(50,40)
student={"name":"ico","age": 21}
number={1,2,3}

#It tells you which data type it belongs to.
print(type(x)) #this is integer
print(type(y)) #this is float
print(type(name)) # this is string 
print(type(isStudent)) # this is boolean
print(type(list)) # this is list
print(type(tuple)) #this is tuple
print(type(student)) # this is dictionary
print(type(number)) # this is set


#USER İNPUT 

print("whats your name:")
name= input()
print(f"hello{name}")

#or
name= input("whats your name:")
print(f"hello {name}") # or print("hello " +name )   # or print("hello", name) this code automatically leaves itself blank


# OUTPUT EXP

print("hello")
print(name)
# screen output is hello
#                   ico

print("hello" ,end="")
print(name)
# screen output is hello ico

print("hello",name,sep="---")
#screen output is hello---ico

print('hello,"friend!"') #output is hello,"friend!"




# STRİNG METHODS

name=input("whats your name: ")

# remove whitespace from str
name=name.strip()

#the first character is uppercase
name=name.capitalize()

# Each word starts with an uppercase letter.
name=name.title()

#split users name into first name and last name
first,last=name.split(" ")

name=name.strip().title() # this other usage

name=input("whats your name: ").strip().title() # this other usage

print(f"hello{name}")



#DATA TYPES
#int
x=input("whats x: ")
y=input("whats y: ")

z=x+y

print(z) #  exp x=3 y=6 output is 36 because x and y string

z=int(x)+int(y)

print(z)# exp x=3 y=6 output is 9 

#or 

x=int(input("whats x: "))
y=int(input("whats y: "))

print((x+y))

#float

x=float(input("x: "))
y=float(input("y: "))

# this line rounded x+y and assigned it to z 
z=round(x+y)

#this Take the 2 characters after the comma.
z=round(x+y,2)
#or
print(f"{z:.2f}") # the same

print(z)

print(f"{z:,}") # this lines output is exp x=999 y=1 output is 1,000




def hello(to="world"):
    print("hello ",to)

hello()
name=input("whats your name: ")
hello(name) # output is exp name:ico  hello world
#                                     hello ico



def main():
    x= int(input("whats x: "))
    print("x squared is:",square(x)) 


def square(n):
    return n*n # or return n**2 or pow(n,2)

main()

