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


draw()

def check():
    flag_3 = 1
    if flag_3 == 1:
        for i in {0,1,2}:
            if ar[i] == ar[i+3] == ar[i+6]:
                if ar[i] == "X":
                    print("Player 1 wins")
                else:
                    print("Player 2 wins")
                flag_3 = 0
                return 3
        for i in {0,3,6}:
            if ar[i] == ar[i+1] == ar[i+2]:
                if ar[i] == "X":
                    print("Player 1 wins")
                else:
                    print("Player 2 wins")
                flag_3 = 0
                return 3
        
                    
        if ar[0] == ar[4] == ar[8]:
            if ar[0] == "X":
                    print("Player 1 wins")
            else:
                    print("Player 2 wins")
            flag_3 = 0
            return 3
        

        if ar[2] == ar[4] == ar[6]:
            if ar[2] == "X":
                    print("Player 1 wins")
            else:
                    print("Player 2 wins")
            flag_3 = 0
            return 3
        

       # for i in range(0,9):
        #    if all ar[i]!= i+1:
         #       print("Match draw")
          #  return 0
          
        if ar[0] != 1 and ar[1] != 2 and ar[2] != 3 and ar[3] != 4 and ar[4] != 5 and ar[5] != 6 and ar[6] != 7 and ar[7] != 8 and ar[8] != 9 :
                print("Match draw")
                flag_3 = 0
                return 2
    else:
        return 1
 

            
    

flag = 1
while flag:
    flag_1 = 1
    while flag_1:
        player_1 = int(input("Enter player 1 position : "))
        if player_1 not in range(1,10):
            print("Wrong input\nPlease try again\n")
        elif ar[player_1-1] == player_1:
            ar[player_1-1] = "X"
            flag_1 = 0
            draw()
            var = check()
            if var == 3 or var == 2:
                flag = 0
                break
            
        elif ar[player_1-1] in {"X","0"}:
            print("Place occupied already\nTry again\n")
       
        else:
            print("Wrong input\nPlease try again\n")
    flag_2 = 1
    if flag ==0:
        break
    while flag_2:
        player_2 = int(input("Enter player 2 position : "))
        if player_2 not in range(1,10):
            print("Wrong input\nPlease try again\n")
        elif ar[player_2-1] == player_2:
            ar[player_2-1] = "0"
            flag_2 = 0
            draw()
            var = check()
            if var == 3 or var == 2:
                flag = 0
                break
        elif ar[player_2-1] in {"X","0"}:
            print("Place occupied already\nTry again\n")
        else:
            print("Wrong input\nPlease try again\n")



    
            
            
  

   
