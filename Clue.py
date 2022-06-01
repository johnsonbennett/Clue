#This is the base file for the base rule for the board game
#Written by Bennett Johnson
import random

suspect_list = ["Mrs Peacock","Rev Green","Colonel Mustard","Prof Plum","Miss Scarlet","Nurse White"]
weapon_list = ["Revolver","Candlestick","Knife","Wrench","Crowbar","Hammer"]
room_list = ["Ballroom","Main hall","Lounge","Kitchen","Bedroom","Living Room"]

choice_list = []
#This function is used to determine the solution for the game
def gameGoal(main_list,list1,list2,list3):
    
    
    choice_suspect = random.choice(list1)  #Choose a random element from the first list parameter
    main_list.append(choice_suspect)        #Add the chosen element to the main list
    list1.remove(choice_suspect)            #Removing the chosen element from list1 to take that from the rest of the game

    choice_weapon = random.choice(list2)
    main_list.append(choice_weapon)
    list2.remove(choice_weapon)

    choice_room = random.choice(list3)
    main_list.append(choice_room)
    list3.remove(choice_room)

gameGoal(choice_list,suspect_list,weapon_list,room_list)

total_list = suspect_list + weapon_list + room_list # Combining all the catagories into one list
random.shuffle(total_list)#Shuffling the list which is used for the game
print(total_list)
condition=True

while(condition==True):
    num_players = int(input("Enter no of players (2-7): "))
    if(num_players > 7 or num_players<2):                   #Check statement to make sure that the user enter the correct input
        print("Invalid Selection, try again!")
    else:
        condition=False


#This function is used to create a deck for the players
def deck_creation():
    deck = {} 
    for i in range(num_players):
         deck[i] = []                                       #Creating a dictionary were we can store each player list as elements
    counter = 0
    i=0
    while(counter < len(total_list)):
        if(i>=num_players):
            i=0
        deck[i].append(total_list[counter])
        counter=counter+1
        i=i+1
        
    return deck

final_deck_list = deck_creation()
print(final_deck_list)


 


    















