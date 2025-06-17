print('Hello, World!')
#define the function to call
def hello():
    print("hello")
    
name = input("What your Name?: ")
hello()
print(name)
print()
print()

def welcom():
    print("welcom")
    
name = input("What your name?: ")
welcom()
print(name)

#We can go furter
#Creat our own function
def hello(to="World"):
    print("hello,", to)
    
name = input("What your name? ")
hello(name)

hello()