from __future__ import print_function
#Example about function and if .. elif statment

try:
    raw_input          # Python 2
except NameError:
    raw_input = input  # Python 3


def Game():
    playerOne_points = 0
    playerTwo_points = 0
    while True:
        print("Choose one of this choices: \n1- Rock \n2- Paper \n3- Scissors")
        first_player = int(raw_input("Player one enter your choice: ").strip())
        ch_list=[1,2,3]
        while first_player not in ch_list:
            print("incorrect choice , Try again ")
            first_player = int(raw_input("Player one enter your choice: ").strip())
        second_player = int(raw_input("Player two enter your choice: ").strip())
        while second_player not in ch_list:
            print("incorrect choice , Try again ")
            second_player = int(raw_input("Player two enter your choice: ").strip())
        
        if first_player == 1 and second_player == 3:    # Rock breaks scissors
            playerOne_points += 1
        elif second_player == 1 and first_player == 3:
            playerTwo_points += 1
        elif first_player == 3 and second_player == 2:  # Scissors cuts paper
            playerOne_points += 1
        elif second_player == 3 and first_player == 2:
            playerTwo_points += 1
        elif first_player == 2 and second_player == 1:  # Paper covers rock
            playerOne_points += 1
        elif second_player == 2 and first_player == 1:
            playerTwo_points += 1
        if playerOne_points > playerTwo_points:
            print("Player one won: " + str(playerOne_points)+ " VS "+ str(playerTwo_points))
        else:
            print("Player two won: " + str(playerTwo_points)+ " VS "+ str(playerOne_points))
        answer = raw_input("Do you want to continue? Y/N ").strip().upper()
        if answer == "N":
            break

Game()
    




    


    
    


    
