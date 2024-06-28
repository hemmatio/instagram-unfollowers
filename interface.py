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

# Help bool
helpopen = False

# Output str
output = "Press 'Run' after uploading files!"

# Help text
helptext = ("This app compares your followers list to your \n"
            "following list and returns all accounts who \n you follow that don't follow you back.\n"
            "\nPlease ensure that you are uploading the \n correct files, and they must be in JSON format."
            "\nCheck the README page on the GitHub \n repository for a step-by-step tutorial on how to"
            "\ncorrectly download your Instagram data.\n"
            "\nThis program was built by Omid Hemmati."
            "\ngithub.com/hemmatio/instagram-unfollowers")

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
    global helpopen
    if helpopen:
        return
    helpopen = True
    help_window = customtkinter.CTkToplevel(interface, fg_color='#23272d')
    x = helpbutton.winfo_rootx()
    y = helpbutton.winfo_rooty() + helpbutton.winfo_height()
    help_window.geometry("350x270+%d+%d" % (x-250, y))
    help_window.title("Help")
    help_window.attributes('-topmost', True)
    help_window.overrideredirect(True)

    # Add some help text
    help_text = customtkinter.CTkLabel(help_window, text=helptext, font=("Helvetica", 14),
                                       justify='left', fg_color='#23272d', text_color='white')
    help_text.pack(padx=20, pady=20)

    def close_help_window():
        """
        Close the help window
        :return:
        """
        help_window.destroy()
        global helpopen
        helpopen = False

    close_button = customtkinter.CTkButton(help_window, text="Close", command=close_help_window)
    close_button.pack()


def run_difference():
    """
    Runs the difference method from main if both files are uploaded
    :return:
    """
    try:
        global output
        if followingpath and followerspath:
            data1 = main.load_json_file(followingpath)
            data2 = main.load_json_file(followerspath)
            set1, set2 = main.create_sets(data1, data2)
            unfollowers = main.difference(set1, set2)
            output = 'Unfollowers:\n' + '\n'.join({str(element) for element in unfollowers})
        else:
            output = "Please upload both files first."
        text_insertion()
    except Exception as e:
        output = "An error occurred. Please check your files and try again."
        text_insertion()


def text_insertion():
    """
    Insert text into the output text box
    :return:
    """
    output_text.configure(state='normal')
    output_text.delete('0.0', 'end')
    output_text.insert('0.0', output)
    output_text.configure(state='disabled')

# UI elements
title = customtkinter.CTkLabel(interface, text="Instagram Unfollowers", font=("Helvetica", 50))
title.grid(row=0, column=1, columnspan=1)
helpbutton = customtkinter.CTkButton(interface, text="Help", command=help_menu)
helpbutton.grid(row=0, column=3, sticky='e')

gap = customtkinter.CTkLabel(interface, text="", width = 20)
gap.grid(row=0, column=4)

empty_label = customtkinter.CTkLabel(interface, text="")
empty_label.grid(row=0, column=2, sticky='we')
interface.grid_columnconfigure(0, weight=1)
interface.grid_columnconfigure(1, weight=1)
interface.grid_columnconfigure(2, weight=1000)


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

run = customtkinter.CTkLabel(interface, text="Check unfollowers", font=("Helvetica", 30))
run.grid(row=5, column=0, sticky='w')
run.grid(padx=20, pady=20)
run_button = customtkinter.CTkButton(interface, text="Run", command=run_difference)
run_button.grid(row=5, column=1, pady=20)

# scrollable text box frame
textframe = customtkinter.CTkFrame(interface)
textframe.grid(row=6, column=0, columnspan=5)
output_frame = customtkinter.CTkFrame(textframe, width=1000, height=400)
output_frame.grid(row=0, column=1, columnspan=5, sticky='we')

output_text = customtkinter.CTkTextbox(output_frame, width=1000, height=400)
text_insertion()
output_text.grid(row=0, column=0)

interface.mainloop()
