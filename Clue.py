#This is the base file for the base rule for the board game
#Written by Bennett Johnson
import random
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox



suspect_list = ["Mrs Peacock","Rev Green","Colonel Mustard","Prof Plum","Miss Scarlett","Nurse White"]
weapon_list = ["Revolver","Candlestick","Knife","Wrench","Crowbar","Hammer"]
room_list = ["Ball Room","Main Hall","Lounge","Kitchen","Bed Room","Living Room"]

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

clue_start=tk.Tk()
clue_start.geometry('600x500')
clue_start.title('Clue Start up page')
img = PhotoImage(file = "C:/Users/johns/OneDrive/Pictures/Saved Pictures/clue-logo-7.png")     #Attached an image which is used in the welcome screen 
tk.Label(clue_start,image = img).pack()
startup_message = tk.Label(clue_start, text="Welcome to Clue!!",font=("Ariel",25)).pack(pady=15)
clue_start.resizable(False,False)


def gamePlay():
    counter1=[6]
    counter2=[6]
    count1=[3]
    count2=[3]
    click=[0]

    clue_game = tk.Tk()
    clue_game.title("Clue")
    clue_game.configure(bg="lightgrey")
    clue_game.geometry('800x700')
    
    random_deck_1=[] 
    random_deck_2=[]                                                                        #Choosing  empty lists to store the initial clue list for both players
    random_weapon_1=random.choice(weapon_list)
    random_weapon_2=random.choice(weapon_list)
    random_deck_1.append(random_weapon_1)
    random_deck_2.append(random_weapon_2)
    weapon_list.remove(random_weapon_1)                            
    
    random_room_1=random.choice(room_list)  
    random_room_2=random.choice(room_list)                                                                    #These set of statements choose 1 card from each catagory as clue
    random_deck_1.append(random_room_1)
    random_deck_2.append(random_room_2)
    room_list.remove(random_room_2)
    
    random_suspect_1=random.choice(suspect_list)
    random_suspect_2=random.choice(suspect_list)
    random_deck_1.append(random_suspect_1)
    random_deck_2.append(random_suspect_2)
    suspect_list.remove(random_suspect_1)
    
    #Configuring board grid layout
    clue_game.columnconfigure(0,weight=2)
    clue_game.columnconfigure(2,weight=2)
    clue_game.columnconfigure(4,weight=2)
    clue_game.rowconfigure(0,weight=1)
    clue_game.rowconfigure(1,weight=1)
    clue_game.rowconfigure(2,weight=1)
    clue_game.rowconfigure(4,weight=1)
    
    # This function is used to switch the player information
    def switch_player(count1,count2,click):
        if(counter1[0]<=0):
             messagebox.showwarning(title='Game Over',message='Game Over!! You used up all your chances. The selection was ' f'{choice_list}')
             clue_game.destroy()
        if(counter2[0]<=0):
             messagebox.showwarning(title='Game Over',message='Game Over!! You used up all your chances.')
        

        if(click[0]==0):
            player_label.configure(text='Player 2')
            starting_deck.configure(text=f'{random_deck_2}')    #This if statement switch the game from player 1 to player 2
            count1[0]=count1[0]-1                               #The click list act as a manual booleon and changes between 0 and 1. When 0,1 is added and becomes 1
            click[0]=click[0]+1                                 #When click is 0, count1 and counter1 decrements. Despite the name, these variables control player 2
        else:
            player_label.configure(text='Player 1')
            starting_deck.configure(text=f'{random_deck_1}')    #Vice versa
            count2[0]=count2[0]-1                               #When click is 1, count2 and counter2 decrements. These counters control player 1
            click[0]=click[0]-1                                 #This condition activates when click is 1 and we subtract 1 to change it back to 0
        
    
    
    #This function delivers clues for the player
    def clue_delivery(total_list):
          random_clue=random.choice(total_list)
          answer=messagebox.askyesno(title='Validation',message='Are you sure? One of your clue will be deducted')
          if answer:
               messagebox.showinfo(title='Clue',message=random_clue)
               
          

    def display_counter(click,counter1,counter2,choice_list):
         if(click[0]==0):                                                   #This if statement is used to determine which counter to decrement
            messagebox.showinfo(title='Clue',message='No of chances left ' f'{counter1[0]}')
            if(count1[0]==0):                                               #This if statement tracks when the count becomes 0 and disables the button
                messagebox.showerror(title='Clue',message='You used up all your chances!! The combination was ' f'{choice_list}')
                clue_choice.configure(state=DISABLED)
         else:
            messagebox.showinfo(title='Clue',message='No of chance left ' f'{counter2[0]}')
            if(count2[0]==0):
                 messagebox.showerror(title='Clue',message='You used up all your chance!! The combination is ' f'{choice_list}')
   
    #This function keep track on the number of clues used. The mechanics is same as display_counter function but decrements count
    def clicked(count1,count2,click):
        if(click[0]==0):
            messagebox.showinfo(title='Clue',message='No of clues left ' f'{count1[0]}')    
            if(count1[0]==0):
                messagebox.showerror(title='Clue',message='You used up all your clues!!')
                clue_choice.configure(state=DISABLED)
        else:
            messagebox.showinfo(title='Clue',message='No of clues left ' f'{count2[0]}')
            if(count2[0]==0):
                 messagebox.showerror(title='Clue',message='You used up all your clues!!')
                 
        
    #Setting room box in the game board
    #Clicking room buttons should reveal a random clue for the player and the counter should go down by 1
    room = tk.Label(clue_game, text = "Ball Room",font=("Ariel",14),bg="pink",borderwidth=3,relief="groove",height=5,width=20,)
    room.grid(column=0,row=0,sticky=tk.W,padx=10,pady=13)
    room = tk.Label(clue_game,text = "Main Hall", font=("Ariel",14),bg="orange",borderwidth=3,relief="groove",height=5,width=20)
    room.grid(column=0,row=1,sticky=tk.NW,padx=10,pady=13)
    room = tk.Label(clue_game,text = "Lounge",font=("Ariel", 14),bg="green",borderwidth=3,relief="groove",height=5,width=20,fg="white")
    room.grid(column=0,row=2,sticky=tk.NW,padx=10,pady=13)
    room = tk.Label(clue_game,text ="Kitchen",font=("Ariel",14),bg="violet",borderwidth=3,relief="groove",height=5,width=20)
    room.grid(column=4,row=0,sticky=tk.E,padx=15,pady=13)
    room = tk.Label(clue_game, text ="Bed Room",font=("Ariel",14),bg="indigo",borderwidth=3,relief="groove",height=5,width=20)
    room.grid(column=4,row=1,sticky=tk.NE,padx=10,pady=13)
    room = tk.Label(clue_game,text="Living Room",font=("Ariel",14),bg="lightblue",borderwidth=3,relief="groove",height=5,width=20)
    room.grid(column=4,row=2,sticky=tk.NE,padx=10,pady=13)
    clue_label = tk.Label(clue_game,text="Clue",font=("Ariel",16),bg="white",borderwidth=3,relief="groove",height=8,width=15)
    clue_label.grid(column=1,row=1,padx=10,pady=13)
    starting_deck=tk.Label(clue_game,text=f'{random_deck_1}',bg="lightgreen",borderwidth=3,relief="groove",height=3,width=50)
    starting_deck.grid(column=1,row=3)
    
    clue_choice=Button(clue_game,text='Click to receive a clue',command=lambda:[clue_delivery(total_list),clicked(click,count1,count2),switch_player(count1,count2,click)],width=30,borderwidth=3,relief='groove')
    clue_choice.grid(column=2,row=1)
    
    displayCounter=Button(clue_game,text='Show no of chances',command=lambda:display_counter(click,counter1,counter2,choice_list))
    displayCounter.grid(column=2,row=2,sticky=tk.W)
    
    player_label=Label(clue_game,text='Player 1',bg='lightgreen',font=('Ariel',14))
    player_label.grid(column=1,row=0,sticky=tk.N)

    total_deck_list=  ["No Selection","Mrs Peacock","Rev Green","Colonel Mustard","Prof Plum",
                       "Miss Scarlett","Nurse White","Revolver","Candlestick","Knife","Wrench","Crowbar","Hammer"
                       "Ball Room","Main Hall","Lounge","Kitchen","Bed Room","Living Room"]

    deck_combo=ttk.Combobox(clue_game,values=total_deck_list)
    deck_combo.grid(column=1,row=2,sticky=tk.W)
           
    
    final_suspect=Label(clue_game,text="Suspect Selection: ").grid(column=1,row=0,sticky=tk.W)
    final_weapon=Label(clue_game,text="Weapon Selection: ").grid(column=1,row=0)
    final_room=Label(clue_game,text="Room selection: ").grid(column=1,row=0,sticky=tk.E)
    
    suspect_entry=tk.Entry(clue_game)
    suspect_entry.grid(column=1,row=0,sticky=tk.SW)
    weapon_entry=tk.Entry(clue_game)
    weapon_entry.grid(column=1,row=0,sticky=tk.S)
    room_entry=tk.Entry(clue_game)
    room_entry.grid(column=1,row=0,sticky=tk.SE)
    print(choice_list)
    
    
    #This is the function that checks whether the player selection is the correct combination
    def searchAlgorithm(choice_list):
                  entry_1=suspect_entry.get()
                  entry_2=weapon_entry.get()
                  entry_3=room_entry.get()
                  correct=0
                  for i in range(3):
                     if(choice_list[i]== entry_1):
                         correct=correct+1               #Using the search algorithm were each index of the list is checked with the target variable
                     if(choice_list[i]== entry_2):
                         correct=correct+1
                     if(choice_list[i]== entry_3):
                         correct=correct+1
                  if(correct==3):
                        messagebox.showinfo(title='Winner',message='Congragulation, you figured it out!!!')
                        clue_game.destroy()

                  if(correct==2):
                        messagebox.showwarning(title='Feedback',message="Almost there, 1 wrong selection. Try again")
                        
                  if(correct==1):
                        messagebox.showwarning(title='Feedback',message="2 wrong selection.Try again")
                        
                  if(correct==0):
                        messagebox.showwarning(title='Feedback',message="Wrong answer Try again")

                  
                  
                  
                  
        
    check_selection=Button(clue_game,text="Check Answer",command=lambda:[switch_player(counter1,counter2,click),searchAlgorithm(choice_list)],borderwidth=3,relief="groove",bg="pink").grid(column=1,row=2,sticky=tk.N)



start_game = tk.Button(clue_start,text = "PLAY",command=gamePlay,height =5,width= 20,borderwidth=3,relief='groove').pack(pady=30)

clue_start.mainloop()
 


    















