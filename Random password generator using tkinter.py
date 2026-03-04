import tkinter as tk 

def generate_password():
    import random,string
    password = ''.join(random.choice(string.ascii_letters + string.digits)for _ in range(12))
    password_entry.delete(0,tk.END)
    password_entry.insert(0,password)
    print(password)


window = tk.Tk()
window.title( "Password Generator")
window.geometry('400x200')

label = tk.Label(text = "Random password generator", fg="black")
label.pack(pady=10)

password_entry = tk.Entry(width=30) 
password_entry.pack(pady=10)

generate_button = tk.Button(text="Generate random password", command=generate_password) 
generate_button.pack(pady=10)

tk.mainloop()