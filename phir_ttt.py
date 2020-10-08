ar = [1, 2, 3, 4, 5, 6, 7, 8, 9]
def draw():
    print("     |      |     ")
    print("  {}  |  {}   |  {}  ".format(ar[0],ar[1],ar[2]))
    print("     |      |     ")
    print("------------------")
    print("     |      |     ")
    print("  {}  |  {}   |  {}  ".format(ar[3],ar[4],ar[5]))
    print("     |      |     ")
    print("------------------")
    print("     |      |     ")
    print("  {}  |  {}   |  {}  ".format(ar[6],ar[7],ar[8]))
    print("     |      |     ")

def check():
    for i in {0,1,2,3,6}:
        if ar[i] == ar[i+3] == ar[i+6]:
            if ar[i] == "X":
                print("Player 1 wins")
            else:
                print("Player 2 wins")
    
                
    if ar[0] == ar[4] == ar[8]:
        if ar[0] == "X":
                print("Player 1 wins")
        else:
                print("Player 2 wins")
    

    if ar[2] == ar[4] == ar[6]:
        if ar[2] == "X":
                print("Player 1 wins")
        else:
                print("Player 2 wins")
    

   # for i in range(0,9):
    #    if all ar[i]!= i+1:
     #       print("Match draw")
      #  return 0

flag = 1
draw()
while flag:
    player_1 = int(input("Enter the position of player 1 : "))
    if ar[player_1-1] != player_1:
        ar[player_1-1] = "X"
        draw()
        
    else:
        print("Wrong input")

    player_2 = int(input("Enter the position of player 2 : "))
    if ar[player_2-1] != player_2:
        ar[player_2-1] = "0"
    else:
        print("Wrong input")

    
            




    
        
