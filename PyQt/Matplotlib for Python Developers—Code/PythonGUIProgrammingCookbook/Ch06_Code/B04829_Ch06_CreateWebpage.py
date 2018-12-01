from os import path, listdir
import tkinter as tk
from tkinter import filedialog as fd

class CreateWebpage():
    #-----------------------------------------------------
    def __init__(self):
        self.fileDir  = path.dirname(__file__)
        self.imgList  = []
        self.htmlFile = ''
        self.selectPngFiles()
        if self.imgList:
            self.writePage()
            
    #-----------------------------------------------------
    def selectPngFiles(self):
        # Browse to any file to add all png files to webpage
        def _destroyWindow():
            root.quit()
            root.destroy() 
        #-----------------------------------------------------
        root = tk.Tk() 
        root.withdraw()
        root.protocol('WM_DELETE_WINDOW', _destroyWindow)   
        #-----------------------------------------------------
        fName = fd.askopenfilename(initialdir=self.fileDir)     
        if not fName:
            return
        folderPath = path.split(fName)[0]
        #-----------------------------------------------------
        for png in listdir(folderPath):
            if path.splitext(png)[1] == '.png':
                image = '<img src= "file:///' + folderPath + '//' + png + '"/>'   # Firefox requires 5 /s
                self.imgList.append(image)
        #-----------------------------------------------------
        print(self.imgList)
        self.htmlFile = folderPath + '.html'
    
    #-----------------------------------------------------
    def writePage(self):
        page = '''<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
        <html>
        <head>
          <meta content="text/html; charset=ISO-8859-1"
         http-equiv="content-type">
          <title>Python GUI Programming Cookbook</title>
        </head>
            <body>
                {}
            </body>
        </html>
        '''.format( ''.join(img for img in self.imgList) )
        #-----------------------------------------------------
        with open(self.htmlFile, 'w') as f:
            f.write(page)
        f.close()
#============================================================
if __name__ == '__main__':
    CreateWebpage()

