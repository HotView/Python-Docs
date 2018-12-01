'''
Created on Aug 30, 2015
Chapter 09
@author: Burkhard
'''


import wx               # Import wxPython GUI toolkit
class GUI(wx.Panel):    # Subclass wxPython Panel
    def __init__(self, parent):

        # Initialize super class
        wx.Panel.__init__(self, parent)

        # Create Status Bar
        parent.CreateStatusBar() 
        
        # Create the Menu
        menu= wx.Menu()

        # Add Menu Items to the Menu
        menu.Append(wx.ID_ABOUT, "About", "wxPython GUI")
        menu.AppendSeparator()
        menu.Append(wx.ID_EXIT, "Exit"," Exit the GUI")

        # Create the MenuBar
        menuBar = wx.MenuBar()
        
        # Give the Menu a Title
        menuBar.Append(menu, "File") 
        
        # Connect the MenuBar to the frame
        parent.SetMenuBar(menuBar)  
        
        # Create a Print Button
        button = wx.Button(self, label="Print", pos=(0,60))
        
        # Connect Button to Click Event method 
        self.Bind(wx.EVT_BUTTON, self.writeToSharedQueue, button)

        # Create a Text Control widget 
        self.textBox = wx.TextCtrl(self, size=(280,50), style=wx.TE_MULTILINE)
        
    def writeToSharedQueue(self, event):
        # Click Event method
        self.textBox.AppendText("The Print Button has been clicked!") 
                       

app = wx.App()      # Create instance of wxPython application      
frame = wx.Frame(None, title="Python GUI using wxPython", 
    size=(300,180)) # Create frame
GUI(frame)          # Pass frame into GUI
frame.Show()        # Display the frame
app.MainLoop()      # Run the main GUI event loop
