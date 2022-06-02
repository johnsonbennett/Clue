#This is the base file for the base rule for the board game
#Written by Bennett Johnson
import random
import tkinter as tk
from tkinter import ttk


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
#print(total_list)

#def player_choice():
 #   condition=True
  #  while(condition==True):
   #     num_players = int(input("Enter no of players (2-7): "))
    #    if(num_players > 7 or num_players<2):                   #Check statement to make sure that the user enter the correct input
     #       print("Invalid Selection, try again!")
      ##     condition=False
    #return num_players
#players = player_choice()

#This function is used to create a deck for the players
def deck_creation():
    player_choice = int(startup_players.get())
    playerNo = int(player_num.get())
    deck = {} 
    for i in range(player_choice):
         deck[i] = []                                       #Creating a dictionary were we can store each player list as elements
    counter = 0
    i=0
    while(counter < len(total_list)):
        if(i>=player_choice):
            i=0
        deck[i].append(total_list[counter])
        counter=counter+1
        i=i+1
    player_deck = deck[playerNo-1]
    display_deck.insert(0,f'{player_deck}')
    
    return deck[playerNo-1]

#final_deck_list = deck_creation(players)

#This is the start up GUI for the game
clue = tk.Tk()
clue.title("Clue Start up Page")
startup_message = ttk.Label(clue, text="Welcome to Clues!!").pack()

clue.geometry('600x400+50+50')
player_label = ttk.Label(clue,text = "Enter number of players").pack()
startup_players = ttk.Entry(clue,width = 35)
startup_players.pack()
player_num_label = ttk.Label(clue, text = "Enter player number").pack()
player_num = ttk.Entry(clue,width =35)
player_num.pack()
startup_deck = ttk.Button(clue,text="Show starting deck",command = deck_creation)
display_deck = ttk.Entry(clue,width = 42)
exit = ttk.Button(clue, text ="Exit",command = lambda:clue.quit())
startup_players.pack()
startup_deck.pack()
display_deck.pack()
display_label = ttk.Label(clue, text = "Your deck will show up in the space above").pack()
exit.pack(side = tk.BOTTOM)
clue.mainloop()



 


    















