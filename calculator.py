#comput the value between x and y using float
x=float(input('What the x?'))
y=float(input('What the y?'))
z=round(x/y,2)

#Calculate the result and round
print(z)
print()
print()

#The Main def for computing
def main():
    x=int(input("What The X? "))
    print("X squarde is", square(x))

def square(n):
    return n * n
    
main()