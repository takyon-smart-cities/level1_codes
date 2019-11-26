import tkinter
import os
import json #It provides to convert python dict into strings(reversed is also possible)
from shutil import copyfile, copytree
from re import search #For searching files

main_path = os.getcwd()
global bg_colour
global fg_colour
global del_backup
class MainWindow(tkinter.Tk) :

    def __init__(self, x_coor, y_coor, title):




        bg_colour = '#cccccc'
        fg_colour = '#FFFFFF'
        """
        Initialises a GUI window.
        Keyword Arguments:
            xsize -- Window size in horizontal direction
            ysize -- Window size in vertical direction
            title -- Window name to be displayed
        """
        self.buttons = dict()
        self.labels = dict()
        self.checkbuttons = dict()
        self.entries = dict()
        self.listboxes = dict()
        self.textboxes = dict()
        super().__init__()
        self.minsize(x_coor, y_coor)
        self.maxsize(x_coor, y_coor)
        self.title(title)
        self.configure(background=bg_colour)

    def button(self,name,row = 1 , column = 0 , rowspan = 1 , columnspan = 1 , **kwargs ):

        self.buttons[name] = tkinter.Button(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour, **kwargs)

        self.buttons[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan)

    def label(self,name,row = 1 , column = 0 , rowspan = 1 , columnspan = 1 , **kwargs ):

        self.labels[name] = tkinter.Label(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour, **kwargs)

        self.labels[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan,sticky = tkinter.W)

    def checkbutton(self,name,row = 1 , column = 0 , rowspan = 1 , columnspan = 1 , **kwargs ):

        self.checkbuttons[name] = tkinter.Checkbutton(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour, **kwargs)

        self.checkbuttons[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan, **kwargs)

    def entry(self,name,row = 1 , column = 0 , rowspan = 1 , columnspan = 1 , **kwargs ):

        self.entries[name] = tkinter.Entry(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour, **kwargs)

        self.entries[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan, **kwargs)

    def listbox(self,name, width, height, row = 1, column = 0, rowspan = 1 ,columnspan = 1, **kwargs):

        self.listboxes[name] = tkinter.Listbox(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour,width = width ,height = height **kwargs)

        self.listboxes[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan, **kwargs)

    def textbox(self,name, width, height, row = 1, column = 0, rowspan = 1 ,columnspan = 1, **kwargs) :

        self.textboxes[name] = tkinter.Text(self,bg = bg_colour,fg = fg_colour, highlightbackground = bg_colour,width = width ,height = height **kwargs)

        self.textboxes[name].grid(row = row,column = column , rowspan = rowspan , columnspan = columnspan, **kwargs)

class Main_Window(MainWindow) :

    def __init__(self,label_text,window_name,function):

        super().__init__(350,60,window_name)
        self.function = function
        self.label('description',text = label_text)
        self.entry('input field',width = 40 , column_ = 1 , columnspan_ = 5)
        self.entries['input field'].bind('<Return>',self.__check)
        self.button('confirm', text='Confirm', command=self.__check, row_=3, column_=1,columnspan_=6)
        self.mainloop()
