while True:
    n  = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
print()
print() 
   
# Let go deeper
while True:
    n = int(input("What's n? "))
    if n > 0:
        break
for _ in range(n):
    print("meow")
    
print()
print()

#Now we can use the function to further improve our programm
def main():
    meow(get_number())
    
def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n
        
def meow(n):
    for _ in range(n):
        print("meow")
    
    
main()