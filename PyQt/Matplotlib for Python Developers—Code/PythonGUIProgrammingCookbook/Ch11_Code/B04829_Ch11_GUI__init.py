'''
Created on Sep 25, 2015
Chapter 11
@author: Burkhard
'''

#============================================================================
# Required import to set the PYTHONPATH
#============================================================================
import __init__

#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
# from .Folder1.Folder2.Folder3.MessageBox import clickMe
from MessageBox import clickMe


#======================
# Create instance
#======================
win = tk.Tk()   

#======================
# Add a title       
#====================== 
win.title("Python GUI")

#===============================================================================
# Adding a LabelFrame and a Button
#===============================================================================
lFrame = ttk.LabelFrame(win, text="Python GUI Programming Cookbook")
lFrame.grid(column=0, row=0, sticky='WE', padx=10, pady=10)

# def clickMe():
#     from tkinter import messagebox
#     messagebox.showinfo('Message Box', 'Hi from same Level.')
#     
button = ttk.Button(lFrame, text="Click Me ", command=clickMe)
button.grid(column=1, row=0, sticky=tk.S)  

#======================
# Start GUI
#======================
win.mainloop()