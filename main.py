import random 


def get_nprize_door(prize_door,n_doors,playerChoice):
    i = 1

    while(i == prize_door or i == playerChoice): 
        i = (i+1)%(n_doors) 

    return i

def switch_choice(shown_door, n_doors, playerChoice):
    i = 1

    while(i == shown_door or i == playerChoice):
        i = (i+1)%(n_doors)
    
    return i


def game(switch,nTests):
    switch_win_counter = 0
    nswitch_win_counter = 0
    switch_lose_counter = 0
    nswitch_lose_counter = 0


    n_doors = 3


    for i in range(0,nTests+1):
        prize_door = random.randint(0,n_doors-1)
        player_choice = random.randint(0,n_doors-1)

        shown_door = get_nprize_door(prize_door,n_doors, player_choice)

        if switch == True:
            player_choice = switch_choice(shown_door, n_doors, player_choice)
        
        if player_choice == prize_door and switch == False:
            nswitch_win_counter += 1
        elif player_choice == prize_door and switch == True:
            switch_win_counter += 1
        elif player_choice != prize_door and switch == False:
            nswitch_lose_counter += 1
        elif player_choice != prize_door and switch == True:
            switch_lose_counter += 1
        else:
            print("Something went wrong")


    return nswitch_win_counter,switch_win_counter,nswitch_lose_counter,switch_lose_counter, nTests



x = game(True,1000000)
y = game(False,1000000)

print("Win switch %: ", x[1]/x[4])
print("Lose switch %: ", x[3]/x[4])
print("Win no switch %: ", y[0]/x[4])
print("Lose no switch %: ", y[2]/x[4])
