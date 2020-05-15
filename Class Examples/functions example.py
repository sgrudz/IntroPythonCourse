"""
def myfunc1(): # need to define f(x) before calling it 
    print("Hello")    
    
print("out of function")
myfunc1() #need to call the f(x)

def logan(x):
    print("In function still?") #yes
    return 7*x #says function is over
    print("In function still?") #no
logan_var = logan(4)
print(logan_var)

def logibear(x, y):
    return x+y

batch1 = logibear(3, 7)
print(batch1)

def special_func(z): #float, int, str all can be passed
    print(z)
    
special_func(100)
special_func("Can we print a string?")
special_func(100.00)
"""
print("How old are you?")
age = int(input()) #if you find a problem, google it

def age_func(age):
    if age >= 18:
        print("You're legal for stuff")
    else:
        print("Not allowed, only 18+")

age_func(age)