def get_guess():
    guess = int(input("Enter your guess: "))
    return guess

#use the main function
def main():
    guess = get_guess()
    if guess == 50:
        print("correct")
    else:
        print("incorrect")
    
main()