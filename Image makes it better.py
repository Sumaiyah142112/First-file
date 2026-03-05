from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image")
root.geometry("400x400")

# Open image
upload = Image.open("Python/image.jpeg")
upload = upload.resize((300, 350))
img = ImageTk.PhotoImage(upload)

# Show image
label = Label(root, image=img)
label.image = img  # keep a reference
label.place(x=50, y=0)

# Text label
label2 = Label(root, text="This is how you add an image in Tkinter window")
label2.place(x=40, y=360)

root.mainloop()