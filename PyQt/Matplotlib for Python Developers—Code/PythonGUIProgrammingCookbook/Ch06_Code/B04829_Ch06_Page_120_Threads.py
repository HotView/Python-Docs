'''
Created on Jul 26, 2015
Recipe:  B04829_06
@author: Burkhard
'''
#======================
# imports
#======================
import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Menu
from tkinter import Spinbox
import B04829_Ch06_ToolTip as tt
import B04829_Ch06_Queues as bq
from B04829_Ch06_TCP_Server import startServer
import B04829_Ch06_URL as url

from threading import Thread
from time import sleep
from queue import Queue

from tkinter import filedialog as fd
from os import path, makedirs
from tkinter import messagebox as mBox

# Module level GLOBALS
GLOBAL_CONST = 42
fDir   = path.dirname(__file__)
netDir = fDir + '\\Backup' 
if not path.exists(netDir):
    makedirs(netDir, exist_ok = True) 


#=================================================================== 
class OOP():
    def __init__(self): 
        # Create instance
        self.win = tk.Tk()           

        # Add a title       
        self.win.title("Python GUI")   
         
        # Disable resizing the window  
        self.win.resizable(0,0)  
        
        # Create a Queue
        self.guiQueue = Queue() 
                              
        self.createWidgets() 
        
        # populate Tab 2 Entries      
        self.defaultFileEntries()
        
        # Start TCP/IP server in its own thread
        svrT = Thread(target=startServer, daemon=True)
        svrT.start()
    

    def defaultFileEntries(self):
        # populate Entry before making it read-only
        #self.fileEntry.config(state='readonly') 
        self.fileEntry.delete(0, tk.END)
        #self.fileEntry.insert(0, fDir) 
        self.fileEntry.insert(0, 'Z:\\')        # bogus path
#         if len(fDir) > self.entryLen:
#             self.fileEntry.config(width=len(fDir) + 3)
        self.fileEntry.config(state='readonly')         

        self.netwEntry.delete(0, tk.END)
        #self.netwEntry.insert(0, netDir) 
        self.netwEntry.insert(0, 'Z:\\Backup')  # bogus path
#         if len(netDir) > self.entryLen:
#             self.netwEntry.config(width=len(netDir) + 3)  
                  
            
    # Button callback
    def clickMe(self):
        self.action.configure(text='Hello ' + self.name.get())        
#         # Non-threaded code with sleep freezes the GUI
#         for idx in range(10):
#             sleep(5)
#             self.scr.insert(tk.INSERT, str(idx) + '\n')

#         # Threaded method does not freeze our GUI
#         self.createThread()
        
        # Passing in the current class instance (self)
        print(self)
        bq.writeToScrol(self)       
        sleep(2)
        htmlData = url.getHtml()
        print(htmlData)
        self.scr.insert(tk.INSERT, htmlData)

    
    # Spinbox callback 
    def _spin(self):
        value = self.spin.get()
        #print(value)
        self.scr.insert(tk.INSERT, value + '\n')
        
    # Checkbox callback  
    def checkCallback(self, *ignoredArgs):
        # only enable one checkbutton
        if self.chVarUn.get(): self.check3.configure(state='disabled')
        else:             self.check3.configure(state='normal')
        if self.chVarEn.get(): self.check2.configure(state='disabled')
        else:             self.check2.configure(state='normal') 
        
    # Radiobutton callback function
    def radCall(self):
        radSel=self.radVar.get()
        if   radSel == 0: self.monty2.configure(text='Blue')
        elif radSel == 1: self.monty2.configure(text='Gold')
        elif radSel == 2: self.monty2.configure(text='Red')        

    # Exit GUI cleanly
    def _quit(self):
        self.win.quit()
        self.win.destroy()
        exit() 
        
#     def methodInAThread(self):
#         print('Hi, how are you?')
#         for idx in range(10):
#             sleep(5)
#             self.scr.insert(tk.INSERT, str(idx) + '\n')        

    def methodInAThread(self, numOfLoops=10):
        for idx in range(numOfLoops):
            sleep(1)
            self.scr.insert(tk.INSERT, str(idx) + '\n') 
        sleep(1)
        print('methodInAThread():', self.runT.isAlive())
            
    # Running methods in Threads
    def createThread(self, num):
        self.runT = Thread(target=self.methodInAThread, args=[num])
        self.runT.setDaemon(True)    
        self.runT.start()
        print(self.runT)
        print('createThread():', self.runT.isAlive())

        # textBoxes are the Consumers of Queue data
        writeT = Thread(target=self.useQueues, daemon=True)
        writeT.start()
    
    # Create Queue instance  
    def useQueues(self):
#         guiQueue = Queue()     
#         print(guiQueue)
#         for idx in range(10):
#             guiQueue.put('Message from a queue: ' + str(idx))          
#         while True: 
#             print(guiQueue.get())
    
        # Now using a class member Queue        
        while True: 
            qItem = self.guiQueue.get()
            print(qItem)
            self.scr.insert(tk.INSERT, qItem + '\n') 
        
          
    #####################################################################################    
    def createWidgets(self):    
        # Tab Control introduced here --------------------------------------
        tabControl = ttk.Notebook(self.win)     # Create Tab Control
        
        tab1 = ttk.Frame(tabControl)            # Create a tab 
        tabControl.add(tab1, text='Tab 1')      # Add the tab
        
        tab2 = ttk.Frame(tabControl)            # Add a second tab
        tabControl.add(tab2, text='Tab 2')      # Make second tab visible
        
        tabControl.pack(expand=1, fill="both")  # Pack to make visible
        # ~ Tab Control introduced here -----------------------------------------
        
        # We are creating a container frame to hold all other widgets
        self.monty = ttk.LabelFrame(tab1, text=' Monty Python ')
        self.monty.grid(column=0, row=0, padx=8, pady=4)        
        
        # Changing our Label
        ttk.Label(self.monty, text="Enter a name:").grid(column=0, row=0, sticky='W')
   
        # Adding a Textbox Entry widget
        self.name = tk.StringVar()
        nameEntered = ttk.Entry(self.monty, width=24, textvariable=self.name)
        nameEntered.grid(column=0, row=1, sticky='W')     
        nameEntered.delete(0, tk.END)
        nameEntered.insert(0, '< default name >') 
        
        # Adding a Button
        self.action = ttk.Button(self.monty, text="Click Me!", command=self.clickMe)   
        self.action.grid(column=2, row=1)
        
        ttk.Label(self.monty, text="Choose a number:").grid(column=1, row=0)
        number = tk.StringVar()
        numberChosen = ttk.Combobox(self.monty, width=14, textvariable=number)
        numberChosen['values'] = (1, 2, 4, 42, 100)
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)
             
        # Adding a Spinbox widget using a set of values
        self.spin = Spinbox(self.monty, values=(1, 2, 4, 42, 100), width=5, bd=8, command=self._spin) 
        self.spin.grid(column=0, row=2, sticky='W')
                  
        # Using a scrolled Text control    
        scrolW  = 40; scrolH  =  10
        self.scr = scrolledtext.ScrolledText(self.monty, width=scrolW, height=scrolH, wrap=tk.WORD)
        self.scr.grid(column=0, row=3, sticky='WE', columnspan=3)
               
        # Tab Control 2 refactoring  ---------------------------------------------------
        # We are creating a container frame to hold all other widgets -- Tab2
        self.monty2 = ttk.LabelFrame(tab2, text=' The Snake ')
        self.monty2.grid(column=0, row=0, padx=8, pady=4)
        
        # Creating three checkbuttons
        chVarDis = tk.IntVar()
        check1 = tk.Checkbutton(self.monty2, text="Disabled", variable=chVarDis, state='disabled')
        check1.select()
        check1.grid(column=0, row=0, sticky=tk.W)                 
        
        self.chVarUn = tk.IntVar()
        self.check2 = tk.Checkbutton(self.monty2, text="UnChecked", variable=self.chVarUn)
        self.check2.deselect()
        self.check2.grid(column=1, row=0, sticky=tk.W )                  
         
        self.chVarEn = tk.IntVar()
        self.check3 = tk.Checkbutton(self.monty2, text="Toggle", variable=self.chVarEn)
        self.check3.deselect()
        self.check3.grid(column=2, row=0, sticky=tk.W)                 
     
        # trace the state of the two checkbuttons
        self.chVarUn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())    
        self.chVarEn.trace('w', lambda unused0, unused1, unused2 : self.checkCallback())   
        # ~ Tab Control 2 refactoring  -----------------------------------------
        
        # Radiobutton list
        colors = ["Blue", "Gold", "Red"]
        
        self.radVar = tk.IntVar()
        
        # Selecting a non-existing index value for radVar
        self.radVar.set(99)    
        
        # Creating all three Radiobutton widgets within one loop
        for col in range(3):
            curRad = 'rad' + str(col)  
            curRad = tk.Radiobutton(self.monty2, text=colors[col], variable=self.radVar, value=col, command=self.radCall)
            curRad.grid(column=col, row=6, sticky=tk.W, columnspan=3)
            # And now adding tooltips
            tt.createToolTip(curRad, 'This is a Radiobutton control.')
            
        # Create a container to hold labels
        labelsFrame = ttk.LabelFrame(self.monty2, text=' Labels in a Frame ')
        labelsFrame.grid(column=0, row=7)
         
        # Place labels into the container element - vertically
        ttk.Label(labelsFrame, text="Label1").grid(column=0, row=0)
        ttk.Label(labelsFrame, text="Label2").grid(column=0, row=1)
        
        # Add some space around each label
        for child in labelsFrame.winfo_children(): 
            child.grid_configure(padx=8)
        
        # Create Manage Files Frame ------------------------------------------------
        mngFilesFrame = ttk.LabelFrame(tab2, text=' Manage Files: ')
        mngFilesFrame.grid(column=0, row=1, sticky='WE', padx=10, pady=5)
        
        # Button Callback
        def getFileName():
            print('hello from getFileName')
            fDir  = path.dirname(__file__)
            fName = fd.askopenfilename(parent=self.win, initialdir=fDir)
            print(fName)
            self.fileEntry.config(state='enabled')
            self.fileEntry.delete(0, tk.END)
            self.fileEntry.insert(0, fName)
            
            if len(fName) > self.entryLen:
                self.fileEntry.config(width=len(fName) + 3)
                        
        # Add Widgets to Manage Files Frame
        lb = ttk.Button(mngFilesFrame, text="Browse to File...", command=getFileName)     
        lb.grid(column=0, row=0, sticky=tk.W) 
        
        #-----------------------------------------------------        
        file = tk.StringVar()
        self.entryLen = scrolW - 4
        self.fileEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=file)
        self.fileEntry.grid(column=1, row=0, sticky=tk.W)
              
        #-----------------------------------------------------
        logDir = tk.StringVar()
        self.netwEntry = ttk.Entry(mngFilesFrame, width=self.entryLen, textvariable=logDir)
        self.netwEntry.grid(column=1, row=1, sticky=tk.W) 

        
        def copyFile():
            import shutil   
            src = self.fileEntry.get()
            file = src.split('/')[-1]  
            dst = self.netwEntry.get() + '\\'+ file
            try:
                shutil.copy(src, dst)   
                mBox.showinfo('Copy File to Network', 'Succes: File copied.')     
            except FileNotFoundError as err:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(err))
            except Exception as ex:
                mBox.showerror('Copy File to Network', '*** Failed to copy file! ***\n\n' + str(ex))   
        
        cb = ttk.Button(mngFilesFrame, text="Copy File To :   ", command=copyFile)     
        cb.grid(column=0, row=1, sticky=tk.E) 
                
        # Add some space around each label
        for child in mngFilesFrame.winfo_children(): 
            child.grid_configure(padx=6, pady=6)
                    

        # Creating a Menu Bar ==========================================================
        menuBar = Menu(tab1)
        self.win.config(menu=menuBar)
        
        # Add menu items
        fileMenu = Menu(menuBar, tearoff=0)
        fileMenu.add_command(label="New")
        fileMenu.add_separator()
        fileMenu.add_command(label="Exit", command=self._quit)
        menuBar.add_cascade(label="File", menu=fileMenu)
        
        # Add another Menu to the Menu Bar and an item
        helpMenu = Menu(menuBar, tearoff=0)
        helpMenu.add_command(label="About")
        menuBar.add_cascade(label="Help", menu=helpMenu)
        
        # Change the main windows icon
        self.win.iconbitmap(r'C:\Python34\DLLs\pyc.ico')
        
        # Using tkinter Variable Classes
        strData = tk.StringVar()
        strData.set('Hello StringVar')
        
        # It is not necessary to create a tk.StringVar() 
        strData = tk.StringVar()
        strData = self.spin.get()
        
        # Place cursor into name Entry
#         nameEntered.focus()  
        # Set focus to Tab 2           
#         tabControl.select(1)      
      
        # Add a Tooltip to the Spinbox
        tt.createToolTip(self.spin, 'This is a Spin control.')         
        
        # Add Tooltips to more widgets
        tt.createToolTip(nameEntered, 'This is an Entry control.')  
        tt.createToolTip(self.action, 'This is a Button control.')                      
        tt.createToolTip(self.scr,    'This is a ScrolledText control.')   
          
#======================
# Start GUI
#======================
oop = OOP()
# Running methods in Threads
# runT = Thread(target=oop.methodInAThread)

# oop.useQueues()
oop.win.mainloop()

