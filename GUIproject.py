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
import GUIfunction

class ParentWindow(Frame):

    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 250))
        self.master.title('Check Files')
        self.master.config(bg='lightgrey')
        GUIfunction.center_window(self,700,250)

        self.varFile1 = StringVar()
        self.varFile1.set("Enter full file path or click \"Browse\" to select")
        self.varFile2 = StringVar()
        self.varFile2.set("Enter full file path or click \"Browse\" to select")

        self.txtFile1 = Entry(self.master,textvariable=self.varFile1, font=("Helvetica",16), fg='black', bg='white', bd=0, relief=SUNKEN)
        self.txtFile1.grid(row = 0, column = 1, columnspan=2, rowspan=1, sticky = W+E, padx=(10,0), pady=(50,0))
        self.txtFile2 = Entry(self.master,textvariable=self.varFile2, font=("Helvetica",16), fg='black', bg='white', bd=0, relief=SUNKEN)
        self.txtFile2.grid(row = 1, column = 1, columnspan=2, rowspan=1, sticky = W+E, padx=(10,0),pady=(20,0))

        self.btnBrowse1 = Button(self.master, text="Browse...", width=15, height=2, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction.browse1(self))
        self.btnBrowse1.grid(row = 0, column = 0, padx=(25,10),pady=(50,0), sticky=NE)

        self.btnBrowse2 = Button(self.master, text="Browse...", width=15, height=2, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction.browse2(self))
        self.btnBrowse2.grid(row = 1, column = 0, padx=(25,10),pady=(20,0), sticky=NE)

        self.btnCheck = Button(self.master, text="Check for files...", width=15, height=3, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction.check(self))
        self.btnCheck.grid(row = 2, column = 0, padx=(25,10),pady=(20,0), sticky=NE)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda: GUIfunction.close(self))
        self.btnClose.grid(row = 2, column = 2, padx=(350,0),pady=(20,0), sticky=NE)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #without this, the window will just pop open and then close
