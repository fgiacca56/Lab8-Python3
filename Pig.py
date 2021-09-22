import random

def rollDice():
    return random.randint(1,6)




  
#question 1
def oneTurn():
    turn_total = 0
    value = False
    while not value:
        roll = rollDice()
        print("Roll: " + str(roll))
        if roll == 1:
            turn_total = 0
            print("Turn total: " + str(turn_total))
            value = True
        elif turn_total >= 20:
            print("Turn total: " + str(turn_total))
            value = True
        else:
            turn_total += roll
    return turn_total
#oneTurn()






#question 2
def oneTurn2():
    turn_total = 0
    value = False
    while not value:
        roll = rollDice()
        if roll == 1:
            turn_total = 0
            value = True
        elif turn_total >= 20:
            value = True
        else:
            turn_total += roll
    return turn_total




def holdAtTwenty():
    scores = {"0": 0, "20": 0,"21": 0,"22": 0, "23": 0, "24": 0, "25": 0}
    integer = int(input("Hold-at-20 turn simulations?: "))
    for i in range(integer):
        total = str(oneTurn2())
        if total in scores:
            scores[total] += 1
    print("Score" , "Estimated Probability", sep="\t")
    for value in scores:
        probability = scores[value] / integer
        print(value , probability, sep="\t")
    
#holdAtTwenty()






#question 3
def oneTurn3():
    turn_total = 0
    value = False
    while not value:
        roll = rollDice()
        if roll == 1:
            turn_total = 0
            value = True
        elif turn_total >= hold_value:
            value = True
        else:
            turn_total += roll
    return turn_total




def holdAtX():
    scores = {}
    amount_times = int(input("Please enter the number of times you wish to loop: "))
    for i in range(amount_times):
        total = oneTurn3()
        if total not in scores:
            scores[total] = 1
        else:
            scores[total] += 1
    for value in scores:
        probability = scores[value] / amount_times
        print(value , probability, sep="\t")
        
#hold_value = int(input("Please enter the hold value: "))        
#holdAtX()






#question 4
def oneTurn4():
    score = int(input("Score?: "))
    turn_total = 0
    value = False
    while not value:
        roll = rollDice()
        print("Roll: " + str(roll))
        if roll == 1:
            turn_total = 0
            print("Turn total: " + str(turn_total))
            value = True
        elif turn_total >= 20:
            print("Turn total: " + str(turn_total))
            value = True
        else:
            turn_total += roll
    new_score = turn_total + score
    print("New score: " + str(new_score))
   
#oneTurn4()





#question 5
def oneTurn5():
    new_score = 0
    while new_score < 100:
        turn_total = 0
        value = False
        while not value:
            roll = rollDice()
            print("Roll: " + str(roll))
            if roll == 1:
                turn_total = 0
                print("Turn total: " + str(turn_total))
                new_score += turn_total
                print("New score: " + str(new_score))
                value = True
            elif turn_total >= 20:
                print("Turn total: " + str(turn_total))
                new_score += turn_total
                print("New score: " + str(new_score))
                value = True
            else:
                turn_total += roll

        
#oneTurn5()





#question 6
def averagePigTurns():
    games = int(input("Games?: "))
    new_score = 0
    turn = 0
    for i in range(games):
        while new_score < 100:
            turn_total = 0
            value = False
            while not value:
                roll = rollDice()
                if roll == 1:
                    turn_total = 0
                    new_score += turn_total
                    turn += 1
                    value = True
                elif turn_total >= 20:
                    new_score += turn_total
                    turn += 1
                    value = True
                else:
                    turn_total += roll
    average_turns = turn / games
    print("Average turns: " + str(average_turns))


#averagePigTurns()





#question 7
    
                
def twoPlayerPig():
    player_1 = 0
    player_2 = 0
    check_turns = 2  
    while player_1 < 100 and player_2 < 100:
        turn_total = 0
        if check_turns % 2 == 0:
            value = False
            while not value:
                roll = rollDice()
                print("Roll: " + str(roll))
                if roll == 1:
                    turn_total = 0
                    print("Turn total: " + str(turn_total))
                    player_1 += turn_total
                    print("Player 1 score: " + str(player_1))
                    print("Player 2 score: " + str(player_2))
                    check_turns += 1
                    value = True
                elif turn_total >= 20:
                    print("Turn total: " + str(turn_total))
                    player_1 += turn_total
                    print("Player 1 score: " + str(player_1))
                    print("Player 2 score: " + str(player_2))
                    check_turns += 1
                    value = True
                else:
                    turn_total += roll
            
        else:
            value = False
            while not value:
                roll = rollDice()
                print("Roll: " + str(roll))
                if roll == 1:
                    turn_total = 0
                    print("Turn total: " + str(turn_total))
                    player_2 += turn_total
                    print("Player 2 score: " + str(player_2))
                    print("Player 1 score: " + str(player_1))
                    check_turns += 1
                    value = True
                elif turn_total >= 20:
                    print("Turn total: " + str(turn_total))
                    player_2 += turn_total
                    print("Player 2 score: " + str(player_2))
                    print("Player 1 score: " + str(player_1))
                    check_turns += 1
                    value = True
                else:
                    turn_total += roll

            
#twoPlayerPig()




#question 8


    
def pigGame():
    player_1 = 0
    player_2 = 0
    check_turns = 2
    
    player_choice = random.randint(1,2)

    if player_choice == 1:
        print("You are player 1")
    else:
        print("Your are player 2")


    
    print("Enter nothing to roll or enter anything to hold: ")

    
    while player_1 < 100 and player_2 < 100:
        turn_total = 0
        if player_choice == 1:
            if check_turns % 2 == 0:
                print("It is player 1's turn")
                value = False
                while not value:
                    roll = rollDice()
                    print("Roll: " + str(roll))
                    if roll == 1:
                        turn_total = 0
                        print("Turn total: " + str(turn_total))
                        player_1 += turn_total
                        print("Player 1 score: " + str(player_1))
                        print("Player 2 score: " + str(player_2))
                        check_turns += 1
                        value = True
                    else:
                        turn_total += roll
                        roll_hold = input("Turn total: " + str(turn_total) + "\t" + "Roll/Hold?: ")
                        if roll_hold == "roll":
                            if turn_total >= 20:
                                print("Turn total: " + str(turn_total))
                                player_1 += turn_total
                                print("Player 1 score: " + str(player_1))
                                print("Player 2 score: " + str(player_2))
                                check_turns += 1
                                value = True
                            else:
                                continue
                        else:
                            print("Turn total: ", turn_total)
                            player_1 += turn_total
                            print("Player 1 score: ", player_1)
                            print("Player 2 score: ", player_2)
                            check_turns += 1
                            value = True
                            
                
                
            else:
                print("It is player 2's turn")
                value = False
                while not value:
                    roll = rollDice()
                    print("Roll: " + str(roll))
                    if roll == 1:
                        turn_total = 0
                        print("Turn total: " + str(turn_total))
                        player_2 += turn_total
                        print("Player 2 score: " + str(player_2))
                        print("Player 1 score: " + str(player_1))
                        check_turns += 1
                        value = True
                    elif turn_total >= 20:
                        print("Turn total: " + str(turn_total))
                        player_2 += turn_total
                        print("Player 2 score: " + str(player_2))
                        print("Player 1 score: " + str(player_1))
                        check_turns += 1
                        value = True
                    else:
                        turn_total += roll
                
                
            
        if player_choice == 2:
            while player_1 < 100 and player_2 < 100:
                if check_turns % 2 == 0:
                    print("It is player 1's turn")
                    value = False
                    while not value:
                        roll = rollDice()
                        print("Roll: " + str(roll))
                        if roll == 1:
                            turn_total = 0
                            print("Turn total: " + str(turn_total))
                            player_2 += turn_total
                            print("Player 2 score: " + str(player_2))
                            print("Player 1 score: " + str(player_1))
                            check_turns += 1
                            value = True
                        elif turn_total >= 20:
                            print("Turn total: " + str(turn_total))
                            player_2 += turn_total
                            print("Player 2 score: " + str(player_2))
                            print("Player 1 score: " + str(player_1))
                            check_turns += 1
                            value = True
              
                else:
                    print("It is player 2's turn")
                    value = False
                    while not value:
                        roll = rollDice()
                        print("Roll: " + str(roll))
                        if roll == 1:
                            turn_total = 0
                            print("Turn total: " + str(turn_total))
                            player_2 += turn_total
                            print("Player 1 score: " + str(player_1))
                            print("Player 2 score: " + str(player_2))
                            check_turns += 1
                            value = True
                        else:
                            turn_total += roll
                            roll_hold = input("Turn total: " + str(turn_total) + "\t" + "Roll/Hold?: ")
                            if roll_hold == "roll":
                                if turn_total >= 20:
                                    print("Turn total: " + str(turn_total))
                                    player_2 += turn_total
                                    print("Player 1 score: " + str(player_1))
                                    print("Player 2 score: " + str(player_2))
                                    check_turns += 1
                                    value = True
                                else:
                                    continue
                            else:
                                print("Turn total: ", turn_total)
                                print("Player 1 score: ", player_1)
                                player_2 += turn_total
                                print("Player 2 score: ", player_2)
                                check_turns += 1
                                value = True
                            
#pigGame()         











    




        
