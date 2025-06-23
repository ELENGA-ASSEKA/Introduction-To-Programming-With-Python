#Let call the function
def main():
    Dificulty = input("Difucult or Casual ")
    Players = input("Multiplayer or Single-palayer ")
    
    if Dificulty == "Dificult":
        if Players == "Multiplayer":
            recommand("Poker")
        else:
            recommand("Klondlike")
    else:
        if Players == "Multiplayer":
            recommand("Hearts")
        else:
            recommand("Clok")
    
def recommand(game):
    print("You migth like", game)
    
main()