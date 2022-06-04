#This is the base file for the base rule for the board game
#Written by Bennett Johnson
import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox


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
def deck_creation(startupPlayers,playerNum):
    player_choice = int(startupPlayers)
    playerNo = int(playerNum)
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
    player_deck = deck[playerNo-1]  
    playerDeck=Listbox(clue_game,height=8,width=5)
    for i in range(len(player_deck)):
        playerDeck.insert(i,f'{player_deck[i]}')
    return player_deck



#This is the start up GUI for the game
clue_start = tk.Tk()
clue_start.title("Clue Start up Page")
img = PhotoImage(file = "C:/Users/johns/OneDrive/Pictures/Saved Pictures/clue-logo-7.png")     #Attached an image which is used in the welcome screen 
tk.Label(clue_start,image = img).pack()
startup_message = tk.Label(clue_start, text="Welcome to Clue!!",font=("Ariel",25)).pack(pady=15)
clue_start.resizable(False,False)
clue_start.geometry('600x550+60+50')
player_label = tk.Label(clue_start,text = "Enter number of players").pack(pady = 10)
startup_players = tk.Entry(clue_start,width = 10)

startupPlayers=startup_players.get()
startup_players.pack()
player_num_label = tk.Label(clue_start, text = "Enter player number").pack(pady=10)
player_num = tk.Entry(clue_start,width =10)
player_num.pack(pady=5)

playerNum=player_num.get()
exit = tk.Button(clue_start, text ="Exit",command = lambda:clue_start.quit()) 
display_label = tk.Label(clue_start, text = "Your deck will show up in the space above").pack()

#The following code is for the game play window and so should be done on a different window
#I am creating another frame were the game play occurs
def gamePlay():
        #Configuring the board grid pattern
        clue_game = tk.Tk()
        clue_game.title("Clue")
        clue_game.configure(bg="lightgrey")
        clue_game.geometry('800x700+50+50')
        clue_game.columnconfigure(0,weight=2)
        clue_game.columnconfigure(2,weight=2)
        clue_game.columnconfigure(4,weight=2)
        clue_game.rowconfigure(0,weight=1)
        clue_game.rowconfigure(1,weight=1)
        clue_game.rowconfigure(2,weight=1)
        clue_game.rowconfigure(3,weight=1)
        clue_game.rowconfigure(4,weight=1)
        
        #Setting room box in the game board
        room1_label = tk.Button(clue_game, text = "Ballroom",font=("Ariel",14),bg="pink",borderwidth=3,relief="groove",height=5,width=20,state="disabled")
        room1_label.grid(column=0,row=0,sticky=tk.W,padx=10,pady=13)
        room2_label = tk.Button(clue_game,text = "Main Hall", font=("Ariel",14),bg="orange",borderwidth=3,relief="groove",height=5,width=20,state="disabled")
        room2_label.grid(column=0,row=1,sticky=tk.NW,padx=10,pady=13)
        room3_label = tk.Button(clue_game,text = "Lounge",font=("Ariel", 14),bg="green",borderwidth=3,relief="groove",height=5,width=20,state="disabled",fg="white")
        room3_label.grid(column=0,row=2,sticky=tk.NW,padx=10,pady=13)
        room4_label = tk.Button(clue_game,text ="Kitchen",font=("Ariel",14),bg="violet",borderwidth=3,relief="groove",height=5,width=20,state="disabled")
        room4_label.grid(column=4,row=0,sticky=tk.E,padx=15,pady=13)
        room5_label = tk.Button(clue_game, text ="Bedroom",font=("Ariel",14),bg="indigo",borderwidth=3,relief="groove",height=5,width=20,state="disabled")
        room5_label.grid(column=4,row=1,sticky=tk.NE,padx=10,pady=13)
        room6_label = tk.Button(clue_game,text="Living Room",font=("Ariel",14),bg="lightblue",borderwidth=3,relief="groove",height=5,width=20,state="disabled")
        room6_label.grid(column=4,row=2,sticky=tk.NE,padx=10,pady=13)

        mainClue_label = tk.Label(clue_game,text="Clue",font=("Ariel",16),bg="white",borderwidth=3,relief="groove",height=8,width=15)
        mainClue_label.grid(column=1,row=1,sticky=tk.E,padx=10,pady=13)

        def generate_die():
            die_num=random.randint(1,6)
            dieNum=die_num
            dice_display=messagebox.showinfo(title="Dice",message="The rolled value is " f'{dieNum}')

        die_generator=Button(clue_game,text="Roll dice",command=generate_die,borderwidth=3,relief="groove")
        die_generator.grid(column=1,row=0)
        display_deck = tk.Button(clue_game, text="Show your deck list",height=3,width=15)
        display_deck.grid(column=1,row=2)

        
        
        
        
        
        
        
        
start_game = tk.Button(clue_start,text = "PLAY",command=gamePlay,height =3,width= 10).pack(pady=10)
exit.pack(side = tk.BOTTOM)


clue_start.mainloop()

 


    















