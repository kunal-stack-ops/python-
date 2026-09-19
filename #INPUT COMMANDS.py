#INPUT COMMANDS
name= input("Enter your name: ")
colour= input("Enter your favourite colour: ")
print("Hello " + name + "! Your favourite colour is " + colour + ".")

print("HI " + name + " Welcome to \tMIT")
 


print("Hello", name)
print(type(name))   
 

age_str = input("Enter your age: ")
print(int(age_str))
print(type(age_str))  
 

age_int = int(input("Enter your age: "))
print(age_int)
print(type(age_int))  
 


height = float(input("Enter your height: "))
print(height)
 

name2 = input("Enter your name: ")
age2 = int(input("Enter your age: "))
print(name2, age2)
 

a = input("Enter numbers: ")
b = input("Enter numbers: ")
print(a)
print(b)
print(type(a))
print(a + b)   

fname, lname = input("Enter your full name: ").split()
print(fname)
print(lname)
 
x, y = map(int, input("Enter two numbers: ").split())
print(type(x))
print(x + y)   
 
ck