'a test wxPython'
__author__ = 'jerry'
import wx


class sayHello(wx.App):
    def OnInit(self):
        frame = wx.Frame(parent=None, title='Hello wxPython')
        frame.Show()
        return True


app = sayHello()
app.MainLoop()
