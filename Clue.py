#This is the base file for the base rule for the board game
#Written by Bennett Johnson
import random
import tkinter as tk
from tkinter import ttk
from tkinter import *


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

#This function is used to create a deck for the players
def deck_creation():
    player_choice = int(startup_players.get())
    playerNo = int(player_num.get())
    
    deck = {} 
    for i in range(player_choice):
         deck[i] = []                                       #Creating a dictionary were we can store each player list as elements
    counter = 0
    i=0                                                     #using the for and while loop to distribute the cards to all the players
    while(counter < len(total_list)):
        if(i>=player_choice):
            i=0
        deck[i].append(total_list[counter])
        counter=counter+1
        i=i+1
    player_deck = deck[playerNo-1]                          #used to display the deck for the specific player
    display_deck.insert(0,f'{player_deck}')


#This is the start up GUI for the game
clue_start = tk.Tk()
clue_start.title("Clue Start up Page")
img = PhotoImage(file = "C:/Users/johns/OneDrive/Pictures/Saved Pictures/clue-logo-7.png")     #Attached an image which is used in the welcome screen 
ttk.Label(clue_start,image = img).pack()
startup_message = ttk.Label(clue_start, text="Welcome to Clue!!",font=("Ariel",25)).pack(pady=15)

clue_start.geometry('600x550+60+50')
player_label = ttk.Label(clue_start,text = "Enter number of players").pack(pady = 10)
startup_players = ttk.Entry(clue_start,width = 10)
startup_players.pack()
player_num_label = ttk.Label(clue_start, text = "Enter player number").pack(pady=10)
player_num = ttk.Entry(clue_start,width =10)
player_num.pack(pady=5)
startup_deck = ttk.Button(clue_start,text="Show starting deck",command = deck_creation)
display_deck = ttk.Entry(clue_start,width = 42)
exit = ttk.Button(clue_start, text ="Exit",command = lambda:clue_start.quit())
startup_deck.pack(pady=10)
display_deck.pack(pady=10)
display_label = ttk.Label(clue_start, text = "Your deck will show up in the space above").pack()


#The following code is for the game play window and so should be done on a different window
#I am creating another frame were the game play occurs
def gamePlay():
    clue_game = tk.Tk()
    clue_game.title("Clue")
    clue_game.geometry('600x600+50+50')
    clue_game.resizable(False,False)
    clue_game.columnconfigure(0,weight=2)
    clue_game.columnconfigure(2,weight=2)
    clue_game.columnconfigure(4,weight=2)
    clue_game.rowconfigure(0,weight=1)
    clue_game.rowconfigure(1,weight=1)
    clue_game.rowconfigure(2,weight=1)
    clue_game.rowconfigure(3,weight=1)
    clue_game.rowconfigure(4,weight=1)
    room1_label = tk.Label(clue_game, text = "Ballroom",font=("Ariel",14),bg="pink",borderwidth=3,relief="groove",height=5,width=20)
    room1_label.grid(column=0,row=0,sticky=tk.W,padx=10,pady=15)
    room2_label = tk.Label(clue_game,text = "Main Hall", font=("Ariel",14),bg="orange",borderwidth=3,relief="groove",height=5,width=20)
    room2_label.grid(column=0,row=2,sticky=tk.NW,padx=10,pady=3)
    room3_label = tk.Label(clue_game,text = "Lounge",font=("Ariel", 14),bg="green",borderwidth=3,relief="groove",height=5,width=20)
    room3_label.grid(column=0,row=3,sticky=tk.W,padx=10,pady=13)
    room4_label = tk.Label(clue_game,text ="Kitchen",font=("Ariel",14),bg="violet",borderwidth=3,relief="groove",height=5,width=20)
    room4_label.grid(column=4,row=0,sticky=tk.E,padx=15,pady=13)
    exit_game = ttk.Button(clue_game, text = "Exit",command = lambda:clue_game.quit())
    











start_game = tk.Button(clue_start,text = "PLAY",command=gamePlay,height =3,width= 10).pack(pady=10)
exit.pack(side = tk.BOTTOM)


clue_start.mainloop()

 


    















