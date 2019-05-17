#
# Python Ver:   3.7.3
#
# Author:       Amme Kolovos (and Tech Academy)
#
# Purpose:      Python Course Exercise
#               Phonebook Demo. Demonstrating OOP, Tkinter GUI module,
#               using Tkinter Parent and Child relationships.
#
# Tested OS:  This code was written and tested on Mac OS 10.14.3.

from tkinter import *
from tkinter import messagebox
import tkinter as tk

#importing other modules from exercise so we have access to them
import phonebookGUI
import phonebookFunction

#Frame is a Tkinter fram class for our class here to inherit from
class ParentWindow(Frame):
    def __init__(self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        # define our master frame configuration
        self.master = master
        self.master.minsize(550,375) #(Width, Height)
        self.master.resizable(width=True, height=True)
        #could also do self.master.maxsize(500,300) or .resizable(width=False,height=False) to make it not resizable

        # This CenterWindow method will center our app on the user's screen
        phonebookFunction.center_window(self,550,375)
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        
###     # This protocol method is a tkinter built-in method to catch if the user clicks the upper corner, "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebookFunction.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module keeping your code comparmentalized and clutter free
        phonebookGUI.load_gui(self)

               





if __name__ == "__main__":
    root = tk.Tk() #syntax to create window from tkinter module
    App = ParentWindow(root) #calling our class App, attaching the window
    root.mainloop() #keeps the window up and running
        
