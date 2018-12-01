'''
Created on Oct 6, 2015
Chapter 10
@author: Burkhard
'''

import wx.html
class HtmlFrame(wx.Frame):
    def __init__(self, parent, title):
        wx.Frame.__init__(self, parent, -1, title, size=(300,230))
        htmlWin = wx.html.HtmlWindow(self)
        htmlWin.SetPage( 
        '<marquee>HTML <font color=\'blue\'>text in blue</font> and '
        'some <i><u>italic underlined text</u></i> that can also '
        'appear <b>in bold</b>.</marquee>')
        
app = wx.App()
frm = HtmlFrame(None, title='Python HTML GUI using wxPython')
frm.Show()
app.MainLoop()
          









