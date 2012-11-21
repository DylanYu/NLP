# coding=utf-8

import wx
from segmentation import Segmentation

class Gui:
    seg = None    

    app = wx.App()
    win = wx.Frame(None, title = "Chinese words segmentation", size = (600, 300))
    panel = wx.Panel(win)
    btnSegment = wx.Button(panel, label = "Segment")
    txtSentence = wx.TextCtrl(panel)
    txtResult = wx.TextCtrl(panel, style = wx.TE_MULTILINE | wx.VSCROLL)
    
    def __init__(self):
        self.seg = Segmentation(self)
        #load the dict
        self.load()
        #LOOP
        self.init_gui()

    def load(self):
        self.seg.read_file()

    def segment(self, event):
        self.txtResult.Clear()
        sentence = self.txtSentence.GetValue()
        result = self.seg.get_segmentation(sentence)
        self.txtResult.SetValue(result)

    def onKeyPressed(self, event):
        keycode = event.GetKeyCode()
        #if ENTER pressed
        if keycode == 13:
            self.segment(event)

    def init_gui(self):
        self.btnSegment.Bind(wx.EVT_BUTTON, self.segment)
        self.txtSentence.Bind(wx.EVT_KEY_UP, self.onKeyPressed)

        hbox = wx.BoxSizer()
        hbox.Add(self.txtSentence, proportion = 1, flag = wx.EXPAND)
        hbox.Add(self.btnSegment, proportion = 0, flag = wx.LEFT, border = 5)

        vbox = wx.BoxSizer(wx.VERTICAL)
        vbox.Add(hbox, proportion = 0, flag = wx.EXPAND | wx.ALL, border = 5)
        vbox.Add(self.txtResult, proportion = 1, flag = wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT, border = 5)

        self.panel.SetSizer(vbox)

        self.win.Center()
        self.win.Show()
        self.app.MainLoop()

g = Gui()
