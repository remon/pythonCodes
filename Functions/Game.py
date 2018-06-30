#Example about function and if .. elif statment

def Game():
    playerOne_points = 0
    playerTwo_points = 0
    while True:
        print "Choose one of this choices: \n1- Rock \n2- Paper \n3- Scissor"
        first_player = raw_input("Player one enter your choice: ")
        ch_list=[1,2,3]
        while (int(first_player) not in ch_list):
            print "incorrect choice , Try again "
            first_player = raw_input("Player one enter your choice: ")
        second_player = raw_input("Player two enter your choice: ")
        while (int(second_player) not in ch_list):
            print "incorrect choice , Try again "
            second_player = raw_input("Player two enter your choice: ")
        
        if (int(first_player) == 1 and int(second_player) == 3):
            playerOne_points += 1
        elif (int(second_player) == 1 and int(first_player) == 3):
            playerTwo_points += 1
        elif (int(first_player)==3 and int(second_player)==2):
            playerOne_points += 1
        elif (int(second_player)==3 and int(first_player)==2):
            playerTwo_points += 1
        elif (int(first_player)==2 and int(second_player)==1):
            playerOne_points += 1
        elif (int(second_player)==2 and int(first_player)==1):
            playerTwo_points += 1
        if playerOne_points > playerTwo_points:
            print "Player one won: " + str(playerOne_points)+ " VS "+ str(playerTwo_points)
        else:
            print "Player two won: " + str(playerTwo_points)+ " VS "+ str(playerOne_points)
        answer = raw_input("Do you want to continue? Y/N ")
        if answer == "N" or answer == "n":
            break
        elif answer == "Y" or answer == "y":
            continue

Game()
    




    


    
    


    


