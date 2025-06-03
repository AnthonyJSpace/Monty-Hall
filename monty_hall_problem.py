# the monty hall problem
# play the monty hall quiz max_turns times and show the % success rate

import random

max_turns = 10
correct_choices = 0

def door_choice(input_prompt):
    while True:
        player_in = input(input_prompt)

        if player_in.isdecimal():
            choice = int(player_in)
            if 1 <= choice <= 3:
                break

    return choice - 1
    
def quiz():
    global correct_choices

    doors = ['goat', 'goat', 'goat']
    show_doors = ['1', '2', '3']

    car_door = random.randint(0, 2)
    doors[car_door] = 'car'

    print("Pick a door to win a car!")

    print(f'\n[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]\n')
    door_val = door_choice('Pick a door 1, 2, or 3? ')

    # use list comprehension to select the 2 doors the player didn't enter, leaving a list in other_doors
    other_doors = [i for i in range(3) if i != door_val]

    # using next() to iterate the i value, select the fisrt one that is a goat to show the player
    show_doors[next(i for i in other_doors if doors[i] == 'goat')] = 'goat'
            
    print(f'\n[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]\n')
    
    print('Would you like to pick a different door?')
    new_door = input('y or n?: ')

    if new_door.lower() == 'y':
        while True:
            second_in = door_choice('New Choice: ')

            if second_in != door_val:
                break
        
        door_val = second_in
            
    show_doors[door_val] = doors[door_val]
    print(f'\n[{show_doors[0]}] [{show_doors[1]}] [{show_doors[2]}]\n')

    if doors[door_val] == 'car':
        print('Winner!\n')
        correct_choices += 1
    else:
        print('Bad luck, thanks for playing!\n')

    print('=============\n')

for n in range(max_turns) :      
    quiz()

print(f"You won {correct_choices} of {max_turns} games ({int((correct_choices/max_turns)*100)}%)\n")
