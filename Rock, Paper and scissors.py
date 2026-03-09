from tkinter import*
import random

root = Tk()
root.title("Rock,Paper & Scissors")

choices = ["Rock","Paper","Scissors"]

def play(user):
    computer = random.choice(choices)

    if user == computer:
        result = "TIE"
    elif user == "Rock" and computer == "Scissors":
        result = "YOU win!!"
    elif user =="Paper" and computer == "Rock":
        result ="YOU win!!"
    elif user == "Scissors" and computer == "Paper":
        result = "YOU win!!"
    else:
        result = "Computer wins!"
    label.config(text="Computer choose "+ computer+"\n"+result)
label = Label(root, text = "Choose Rock, Paper, or Scissors")
label.pack()

Button(root , text = "Rock",command = lambda: play("Rock")).pack()
Button(root , text = "Paper",command = lambda: play("Paper")).pack()
Button(root , text = "Scissors",command = lambda: play("Scissors")).pack()


root.mainloop()


