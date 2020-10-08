flag = 1
while flag:
    print("Enter any : STONE , PAPER , SCISSORS, EXIT")
    player = input().upper()
#    if player!= "STONE" or player!= "PAPER" or player!= "SCISSORS":
#       print("Dont act smart ..run again")
#       break
    if player == "EXIT":
        flag = 0
        break
    print()
    print("You entered : {}".format(player))
    import random
    game = ["STONE", "PAPER", "SCISSORS"]
    comp_player = random.choice(game)
    print("comp_player entered : {}".format(comp_player))


    if player == "STONE":
        if comp_player =="PAPER":
            print("Comp_player won")
            print()
        elif comp_player == "SCISSORS":
            print("You won it")
            print()
        else:
            print("Match Draw")
            print()

    elif player == "PAPER":
        if comp_player == "SCISSORS":
            print("Comp_player won")
            print()
        elif comp_player == "STONE":
            print("You won it")
            print()
        else:
            print("Match Draw")
            print()

    else:
        if comp_player == "STONE":
            print("Comp_player won")
            print()
        elif comp_player == "PAPER":
            print("You won it")
            print()
        else:
            print("Match Draw")
            print()
            
