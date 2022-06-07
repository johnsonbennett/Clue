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

clue_start=tk.Tk()
clue_start.geometry('600x550')
clue_start.title('Clue Start up page')
img = PhotoImage(file = "C:/Users/johns/OneDrive/Pictures/Saved Pictures/clue-logo-7.png")     #Attached an image which is used in the welcome screen 
tk.Label(clue_start,image = img).pack()
startup_message = tk.Label(clue_start, text="Welcome to Clue!!",font=("Ariel",25)).pack(pady=15)
clue_start.resizable(False,False)


def gamePlay():
    counter=6
    clue_game = tk.Tk()
    clue_game.title("Clue")
    clue_game.configure(bg="lightgrey")
    clue_game.geometry('800x700')
    
    random_deck=[]                                                                  #Choosing this empty list to store the initial clue list
    random_weapon=random.choice(weapon_list)
    random_deck.append(random_weapon)
    total_list.remove(random_weapon)                            
    random_room=random.choice(room_list)                                             #These set of statements choose 1 card from each catagory as clue
    random_deck.append(random_room)
    total_list.remove(random_room)
    random_suspect=random.choice(suspect_list)
    random_deck.append(random_suspect)
    total_list.remove(random_suspect)
    
    #Configuring board grid layout
    clue_game.columnconfigure(0,weight=2)
    clue_game.columnconfigure(2,weight=2)
    clue_game.columnconfigure(4,weight=2)
    clue_game.rowconfigure(0,weight=1)
    clue_game.rowconfigure(1,weight=1)
    clue_game.rowconfigure(2,weight=1)
    clue_game.rowconfigure(4,weight=1)

    #This function delivers clues for the player by sacrificing a chance
    def clue_delivery(counter):
        random_clue=random.choice(total_list)
        answer=messagebox.askyesno(title='Validation',message='Are you sure, one of your chance will be deducted')
        if answer:
             counter=counter-1
             messagebox.showinfo(title='Clue',message=random_clue)

    def display_counter(counter):
         if(counter<2):
              messagebox.showwarning(title='Warning',message='Reaching limit you have % chances ' %(counter))
         else:
              messagebox.showinfo(title='Chance',message='You have % chances left' %(counter))


    
        
    #Setting room box in the game board
    #Clicking room buttons should reveal a random clue for the player and the counter should go down by 1
    room1_label = tk.Button(clue_game, text = "Ballroom",font=("Ariel",14),bg="pink",command=lambda:clue_delivery(counter),borderwidth=3,relief="groove",height=5,width=20,state="normal")
    room1_label.grid(column=0,row=0,sticky=tk.W,padx=10,pady=13)
    room2_label = tk.Button(clue_game,text = "Main Hall", font=("Ariel",14),bg="orange",borderwidth=3,command=lambda:clue_delivery(counter),relief="groove",height=5,width=20,state="normal")
    room2_label.grid(column=0,row=1,sticky=tk.NW,padx=10,pady=13)
    room3_label = tk.Button(clue_game,text = "Lounge",font=("Ariel", 14),bg="green",borderwidth=3,command=lambda:clue_delivery(counter),relief="groove",height=5,width=20,state="normal",fg="white")
    room3_label.grid(column=0,row=2,sticky=tk.NW,padx=10,pady=13)
    room4_label = tk.Button(clue_game,text ="Kitchen",font=("Ariel",14),bg="violet",borderwidth=3,command=lambda:clue_delivery(counter),relief="groove",height=5,width=20,state="normal")
    room4_label.grid(column=4,row=0,sticky=tk.E,padx=15,pady=13)
    room5_label = tk.Button(clue_game, text ="Bedroom",font=("Ariel",14),bg="indigo",borderwidth=3,command=lambda:clue_delivery(counter),relief="groove",height=5,width=20,state="normal")
    room5_label.grid(column=4,row=1,sticky=tk.NE,padx=10,pady=13)
    room6_label = tk.Button(clue_game,text="Living Room",font=("Ariel",14),bg="lightblue",borderwidth=3,command=lambda:clue_delivery(counter),relief="groove",height=5,width=20,state="normal")
    room6_label.grid(column=4,row=2,sticky=tk.NE,padx=10,pady=13)
    mainClue_label = tk.Label(clue_game,text="Clue",font=("Ariel",16),bg="white",borderwidth=3,relief="groove",height=8,width=15)
    mainClue_label.grid(column=1,row=1,padx=10,pady=13)
    starting_deck=tk.Label(clue_game,text=f'{random_deck}',bg="lightgreen",borderwidth=3,relief="groove",height=3,width=50).grid(column=1,row=3)
    clue_choice=Button(clue_game,text='Click to receive a clue',command=lambda:clue_delivery(counter),width=30,borderwidth=3,relief='groove').grid(column=2,row=1)
    display_counter=Button(clue_game,text='Show no of chances',command=lambda:display_counter(counter)).grid(column=2,row=2,sticky=tk.W)


    final_suspect=Label(clue_game,text="Suspect Selection: ").grid(column=1,row=0,sticky=tk.W)
    final_weapon=Label(clue_game,text="Weapon Selection: ").grid(column=1,row=0)
    final_room=Label(clue_game,text="Room selection: ").grid(column=1,row=0,sticky=tk.E)
    suspect_entry=tk.Entry(clue_game).grid(column=1,row=0,sticky=tk.SW)
    weapon_entry=tk.Entry(clue_game).grid(column=1,row=0,sticky=tk.S)
    room_entry=tk.Entry(clue_game).grid(column=1,row=0,sticky=tk.SE)

        #This is the function that checks whether the player selection is the correct combination
    def searchAlgorithm(choice_list,counter):
              entry_1=suspect_entry.get()            
              entry_2=weapon_entry.get()
              entry_3=room_entry.get()
              correct=0
              for i in range(3):
                 if(choice_list[i]==entry_1):
                      correct=correct+1               #Using the search algorithm were each index of the list is checked with the target variable
                 if(choice_list[i]==entry_2):
                      correct=correct+1
                 if(choice_list[i]==entry_3):
                      correct=correct+1
                 if(correct==3):
                    messagebox.showinfo(title='Winner',message='Congragulation,you figured it out!!!')
                    counter=counter-1
                 if(correct==2):
                    messagebox.showwarning(title='Feedback',message="Almost there, 1 wrong selection. Try again")
                    counter=counter-1
                 if(correct==1):
                    messagebox.showwarning(title='Feedback',message="2 wrong selection.Try again")
                    counter=counter-1
                 if(correct==0):
                    messagebox.showwarning(title='Feedback',message="Wrong answer Try again")
                    counter=counter-1                                                           
        

    check_selection=Button(clue_game,text="Check Answer",command=lambda:searchAlgorithm(choice_list,counter),borderwidth=3,relief="groove",bg="pink").grid(column=1,row=2,sticky=tk.N)
  


start_game = tk.Button(clue_start,text = "PLAY",command=gamePlay,height =5,width= 20,borderwidth=3,relief='groove').pack(pady=10)

clue_start.mainloop()

 


    















