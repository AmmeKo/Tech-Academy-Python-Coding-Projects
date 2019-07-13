#
# Python Ver:   3.7.3
#
# Author:       Amme Kolovos
#
# Purpose:      Python Course Exercise
#               Tkinter GUI demo
#
# Tested OS:  This code was written and tested on Mac OS 10.14.3.

import tkinter
from tkinter import *
from tkinter import filedialog as tk
import GUIfunction3

class ParentWindow(Frame):

    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 250))
        self.master.title('Check for Files')
        self.master.config(bg='lightgrey')
        
        self.varDir1 = StringVar()
        self.varDir1.set("Select a source directory")
        self.varDir2 = StringVar()
        self.varDir2.set("Select a destination directory")

        self.txtDir1 = Entry(self.master,textvariable=self.varDir1, font=("Helvetica",16), fg='black', bg='white', bd=0, relief=SUNKEN)
        self.txtDir1.grid(row = 0, column = 1, columnspan=2, rowspan=1, sticky = W+E, padx=(10,0), pady=(50,0))
        self.txtDir2 = Entry(self.master,textvariable=self.varDir2, font=("Helvetica",16), fg='black', bg='white', bd=0, relief=SUNKEN)
        self.txtDir2.grid(row = 1, column = 1, columnspan=2, rowspan=1, sticky = W+E, padx=(10,0), pady=(20,0))

        self.btnSelect1 = Button(self.master, text="Select", width=15, height=2, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=self.select1)
        self.btnSelect1.grid(row = 0, column = 0, padx=(25,10),pady=(50,0), sticky=NE)
        self.btnSelect2 = Button(self.master, text="Select", width=15, height=2, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=self.select2)
        self.btnSelect2.grid(row = 1, column = 0, padx=(25,10),pady=(20,0), sticky=NE)

        self.btnMove = Button(
            self.master, text="Move all text files", width=15, height=3, bg='lightgrey',
            highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction3.transfer(self)
        )
        self.btnMove.grid(row = 2, column = 0, padx=(25,10),pady=(20,0), sticky=NE)

        self.btnClose = Button(
            self.master, text="Close Program", width=15, height=3, bg='lightgrey',
            highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction3.close(self)
        )
        self.btnClose.grid(row = 2, column = 2, padx=(350,0),pady=(20,0), sticky=NE)

    def select1(self):
        tk.dirName = tk.askdirectory(initialdir = "../",title = "Select Folder")
        varDir1 = tk.dirName
        self.varDir1.set(varDir1)

    def select2(self):
        tk.dirName = tk.askdirectory(initialdir = "../",title = "Select Folder")
        varDir2 = tk.dirName
        self.varDir2.set(varDir2)



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    GUIfunction3.center_window(App,700,250)
    root.mainloop() #without this, the window will just pop open and then close
