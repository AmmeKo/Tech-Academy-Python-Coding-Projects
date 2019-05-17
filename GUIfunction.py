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
import GUIproject

def center_window(self,w,h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def browse1(self):
    from tkinter import filedialog as tk
    tk.filename = tk.askopenfilename(initialdir = "/",title = "Select Files")
    varFile1 = tk.filename
    print('File 1 selection = {}'.format(varFile1)) #just double-checking
    self.varFile1.set(varFile1)

def browse2(self):
    from tkinter import filedialog as tk
    tk.filename = tk.askopenfilename(initialdir = "/",title = "Select Files")
    varFile2 = tk.filename
    print('File 2 selection = {}'.format(varFile2)) #just double-checking
    self.varFile2.set(varFile2)

def check(self):
    from tkinter import messagebox as mb
    import glob
    import os
    f1 = self.varFile1.get()
    f2 = self.varFile2.get()
    print(f1)
    print(f2)
    search1 = glob.glob("{}*".format(f1), recursive=False)
    search2 = glob.glob("{}*".format(f2), recursive=False)
    if f1=='':
        search1=[] #needed to make the following if statements work. A blank f1/f2 returns the current directory
    if f2=='':
        search2=[]
    if search1 != [] and search2 != []:
        mb.showinfo('File Match Confirmed', 'File locations:\n{}\n{}'.format(search1[0],search2[0]))
    elif search1 != [] and search2 ==[]:
        mb.showinfo('File Match Confirmed', 'File location:\n{}'.format(search1[0]))
    elif search1 == [] and search2 !=[]:
        mb.showinfo('File Match Confirmed', 'File location:\n{}'.format(search2[0]))
    else:
        mb.showinfo('No File Match Found', 'No matching files were found on this device')

def close(self):
    self.master.destroy() #destroy is command to close the window


if __name__ == "__main__":
    pass
