"""
This file contains the interface for the Instagram Unfollowers app.
"""
import tkinter
from tkinter import filedialog
import customtkinter
import main


# Theme and appearance
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')

# App frame
interface = customtkinter.CTk()
interface.geometry("1280x768")
interface.title("Instagram Unfollowers")

# File paths
followingpath = ''
followerspath = ''

def upload_file(file: int):
    """
    Upload a file and get the path
    """
    global followingpath
    global followerspath
    if file == 1:
        followingpath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    elif file == 0:
        followerspath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])


def help_menu():
    """
    Display a help menu
    """
    help_window = tkinter.Toplevel(interface)
    help_window.geometry("400x400+500+500")
    help_window.title("Help")
    help_window.overrideredirect(True)

    # Add some help text
    help_text = tkinter.Label(help_window, text="This is the help text.")
    help_text.pack()

    def close_help_window():
        help_window.destroy()

    close_button = customtkinter.CTkButton(help_window, text="Close", command=close_help_window)
    close_button.pack(side='bottom')


# UI elements
title = customtkinter.CTkLabel(interface, text="Instagram Unfollowers", font=("Helvetica", 50))
title.grid(row=0, column=1, columnspan=2)
helpbutton = customtkinter.CTkButton(interface, text="Help", command=help_menu)
helpbutton.grid(row=1, column=1, sticky='e')

upload1 = customtkinter.CTkLabel(interface, text="Upload following.json file", font=("Helvetica", 30))
upload1.grid(row=2, column=0, sticky='w')
upload1.configure(padx=20, pady=20)
upload1_button = customtkinter.CTkButton(interface, text="Upload", command=lambda: upload_file(1))
upload1_button.grid(row=2, column=1)


upload2 = customtkinter.CTkLabel(interface, text="Upload followers_1.json file", font=("Helvetica", 30))
upload2.grid(row=3, column=0, sticky='w')
upload2.configure(padx=20, pady=20)
upload2_button = customtkinter.CTkButton(interface, text="Upload", command=lambda: upload_file(0))
upload2_button.grid(row=3, column=1)

interface.mainloop()
