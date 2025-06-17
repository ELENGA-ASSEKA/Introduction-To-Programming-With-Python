#This Is The Main Function
def main():
#Inter Your Name Here
    Name=input("What Your Name? ").strip().title()
    hello(Name)
    
    #hello()
#This Is The Function For Hello
def hello(to ="World"):
    print("Hello,", to)
    
main()