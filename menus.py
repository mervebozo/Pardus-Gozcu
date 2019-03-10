#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
import tkFont
import subprocess

def showHelp():
    f = open("hlp.txt", 'r')
    out = f.readlines()
    f.close()
    root = Tk()
    root.title("Pardus Gözcü Yardım Konuları")
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_reqheight()) / 2
    root.geometry("+%d+%d" % (x, y))
    root.resizable(0,0)
    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)
    _font = tkFont.Font(family="Helvetica", size=18, weight="bold")    #
    text = Text(root, font=_font)
    text.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=text.yview)
    for o in out:
        text.insert(INSERT, o)
    text.config(state=DISABLED)
    text.pack()
    root.mainloop()

def about():
    cmd = "sudo kdialog --title 'Pardus Gözcü Hakkında' --msgbox '                       Pardus Gözcü Sürüm: 1.0                                    \n\n                                  Geliştiriciler\n\n                                  Merve Bozo\n                           Mustafa Orkun Acar'"
    subprocess.call(cmd, shell=True)

