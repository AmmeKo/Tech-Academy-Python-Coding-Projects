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
import GUIproject3

def center_window(window,w,h): # pass in the tkinter frame (master) reference and the w and h
    # get user's screen width and height
    screen_width = window.master.winfo_screenwidth()
    screen_height = window.master.winfo_screenheight()
    # calculate x and y coordinates to paint the app centered on the user's screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = window.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

#def select1(self): (personal note: keeping this here to remember how it was when outside)
#    from tkinter import filedialog as tk
#    tk.dirName = tk.askdirectory(initialdir = "../",title = "Select Folder")
#    varDir1 = tk.dirName
#    self.varDir1.set(varDir1)

#def select2(self):
#    from tkinter import filedialog as tk
#    tk.dirName = tk.askdirectory(initialdir = "../",title = "Select Folder")
#    varDir2 = tk.dirName
#    self.varDir2.set(varDir2)

def transfer(window):
    from tkinter import messagebox as mb
    import os
    import sqlite3
    import shutil
    from os import path
    import datetime
    from datetime import date, time, timedelta
    import time

    #create database
    conn = sqlite3.connect('txt_files.db')
    cur = conn.cursor()
    commit = conn.commit()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            file_name TEXT, \
            mod_time DATE)")

    #list all source and destination paths
    varDir1 = window.varDir1.get()
    listDir1 = os.listdir('{}'.format(varDir1))
    destPathList = []
    srcPathList = []
    txtFileList = []
    modTimeList = []
    for i in listDir1:
        if '.txt' in i:
            src = window.varDir1.get()
            srcPath = os.path.join(src,i)
            srcPathList.append(srcPath)
            dest = window.varDir2.get()
            destPath = os.path.join(dest,i)
            destPathList.append(destPath)
            txtFileList.append(i)
            modTime = time.ctime(os.path.getmtime(srcPath))
            modTimeList.append(modTime)

    #move the files
    for i, pathString in enumerate(destPathList):
        shutil.move(srcPathList[i],pathString)

    #insert into database
    for i, nameData in enumerate(txtFileList):
        cur.execute("""INSERT INTO tbl_files (file_name,mod_time) VALUES (?,?)""", (nameData,modTimeList[i]))
    conn.commit()
    conn.close()

    #display message showing what was moved
    msgList = []
    for i, nameData in enumerate(txtFileList):
        submsg = "File Name: {}\nLast Modified: {}\n".format(nameData,modTimeList[i])
        msgList.append(submsg)
    msg = ''.join(msgList)
    print('Files Moved: \n{}'.format(msg))
    mb.showinfo('Files Moved', msg)

def close(window):
    window.master.destroy() #destroy is command to close the window


if __name__ == "__main__":
    pass
