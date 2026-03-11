from tkinter import *
import random

root = Tk()
root.title("Rock,Paper & Scissor")

choices = ["Rock","Paper","Scissor"]

def rock(user):
    computer = random.choice(choices)

    if user == computer:
        result = "Tie"
    elif user == "Rock"  and computer == "Scissor":
        result = "You Win!"
    elif user =="Paper" and computer == "Rock":
        result ="YOU win!!"
    elif user == "Scissor" and computer == "Paper":
        result = "YOU win!!"
    else:
        result = "Computer wins!"
    label.config(text= "Computer choose "+computer +"\n" + result)
label = Label(root,text="Choose Rock,Paper Or Scissor")
label.pack()

Button(root,text="rock",command= lambda: rock("Rock")).pack()
Button(root,text="paper",command= lambda: rock("Paper")).pack()
Button(root,text="scissor",command= lambda: rock("Scissor")).pack()
 
root.mainloop()

    
    