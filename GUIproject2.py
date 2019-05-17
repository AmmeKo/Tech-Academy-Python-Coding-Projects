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
import GUIfunction2

class ParentWindow(Frame):

    def __init__ (self, master):
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width = False, height = False)
        self.master.geometry('{}x{}'.format(700, 200))
        self.master.title('Select a Directory')
        self.master.config(bg='beige')
        GUIfunction2.center_window(self,700,200)

        self.varDir = StringVar()
        self.varDir.set('Select a directory to open')

        self.txtDir = Entry(self.master,textvariable=self.varDir, font=("Helvetica",16), fg='black', bg='lightgrey', bd=0, relief=SUNKEN)
        self.txtDir.grid(row = 0, column = 1, columnspan=2, rowspan=1, sticky = W+E, padx=(10,0), pady=(50,0))
        
        self.btnSelect = Button(self.master, text="Select...", width=15, height=2, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda:GUIfunction2.select(self))
        self.btnSelect.grid(row = 0, column = 0, padx=(25,10),pady=(50,0), sticky=NE)

        self.btnClose = Button(self.master, text="Close Program", width=15, height=3, bg='lightgrey', highlightbackground="lightgrey", relief=RAISED, command=lambda: GUIfunction2.close(self))
        self.btnClose.grid(row = 2, column = 2, padx=(350,0),pady=(20,0), sticky=NE)


if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop() #without this, the window will just pop open and then close
