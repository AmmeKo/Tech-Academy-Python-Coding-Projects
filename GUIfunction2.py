#
# Python Ver:   3.7.3
#
# Author:       Amme Kolovos
#
# Purpose:      Python Course Exercise
#               Function for Tkinter GUI demo
#
# Tested OS:  This code was written and tested on Mac OS 10.14.3.

from tkinter import *
import GUIproject2

def center_window(self,w,h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def select(self):
    from tkinter import filedialog as tk
    tk.dirName = tk.askdirectory(initialdir = "./",title = "Select Folder")
    varDir = tk.dirName
    print('Folder selection = {}'.format(varDir)) #just double-checking
    self.varDir.set(varDir)

def close(self):
    self.master.destroy() #destroy is command to close the window


if __name__ == "__main__":
    pass
