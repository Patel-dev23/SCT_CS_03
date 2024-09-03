import tkinter as tk 
import re

# this is a function to check strength of password
def check_password_strength():
    password  = password_entry.get()
    
    lower_case = re.compile(r'[a-z]')
    upper_case = re.compile(r'[A-Z]')
    numbers = re.compile(r'[0-9]')
    special_characters = re.compile(r'[^a-zA-Z0-9]')
    
    # minimum length of password should be 8
    min_length = 8 
    
    if len(password) < min_length:
        strength_label.config(text="Password is Less than 8 character. Min length should be {} characters.".format(min_length))
        return
    if not lower_case.search(password):
        strength_label.config(text="Password must contain at least one Lowercase letter.", fg='red')
        return
    if not upper_case.search(password):
        strength_label.config(text="Password must contain at least one Uppercase letter.", fg='red')
        return
    if not numbers.search(password):
        strength_label.config(text="Password must contain at least one digit.", fg='red')
        return
    if not special_characters.search(password):
        strength_label.config(text="Password must contain at least one Special character.", fg='red')
        return
    strength_label.config(text="Password is strong.", fg="green")
# basic gui Window     
task3_root = tk.Tk()
task3_root.title("Password Strength Checker")

task3_root.geometry("300x250")


#Password Entry Field 

password_label = tk.Label(task3_root, text="Enter Password:")
password_label.pack()
password_entry = tk.Entry(task3_root,show="#")
password_entry.pack()

#button creation 

check_button = tk.Button(task3_root, text="Check Strength", command= check_password_strength)
check_button.pack()


strength_label = tk.Label(task3_root, text="", fg="black")
strength_label.pack()

task3_root.mainloop()