#!/usr/bin/python
"""(dot)Desktop File Creator - generates linux .desktop files from a template.

Copyright (C) 2013 Addie MacGruer

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.
"""

from Tkinter import *
import tkFileDialog

class Counter:
    value = 0;
    def next(self):
        rval = self.value
        self.value += 1
        return rval
    def current(self):
        return self.value
    def reset(self):
        self.value = 0
        
values = {}

def addLabel(text):
    global top,rowCount, colCount
    l = Label(top,text=text)
    l.grid(row=rowCount.current(),column=colCount.next())

def generate():
    global target, Name, filename, values
    filename = values["Name"].get().replace(" ", "") + ".desktop"
    from os.path import expanduser
    output = "[Desktop Entry]\n"
    for k,v in values.iteritems():
        if v.get()=="":
            continue
        output += k+"="+v.get()+"\n"
        
    home = expanduser("~")
    filedir = home+"/.local/share/applications/"
    print filedir, filename
    userchoice = tkFileDialog.asksaveasfilename(initialfile = filename, initialdir = filedir)
    with open(userchoice,"w") as f:
        f.write(output)
            
def finishRow():
    colCount.reset()
    rowCount.next()

def addTextField(key):
    addLabel(key)
    values[key]=StringVar()
    tf = Entry(top,textvariable=values[key])
    tf.grid(row = rowCount.current(),column = colCount.next())
    finishRow()
    
def addTextFieldWithValue(key,value):
    addTextField(key)
    values[key].set(value)
    
def addFileChooser(key):
    addLabel(key)
    b = Button(top)
    values[key]=StringVar()
    def localChooseFile():
        choice = tkFileDialog.askopenfilename()
        b.config(text=choice)
        values[key].set(choice)
    b.config(command=localChooseFile)
    b.grid(row=rowCount.current(),column=colCount.next())
    finishRow()
    
def addPathField(key):
    addLabel(key)
    b = Button(top)
    values[key]=StringVar()
    def localChoosePath():
        choice = tkFileDialog.askdirectory()
        b.config(text=choice)
        values[key].set(choice)
    b.config(command=localChoosePath)
    b.grid(row=rowCount.current(),column=colCount.next())
    finishRow()

class TrueFalseSpinbox(Spinbox):
    def __init__(self,master=None,cnf={},**kw):
        kw["values"]=("","true","false")
        Spinbox.__init__(self,master,cnf,**kw)
    def get(self):
        rval = super.get()
        print "TFS:"+rval
        return rval

def addBooleanField(key):
    addLabel(key)
    values[key]=StringVar()
    tf = TrueFalseSpinbox(top,textvariable=values[key])
    tf.grid(row = rowCount.current(),column = colCount.next())
    finishRow()
    
def addGenerateButton():
    addLabel("")
    button = Button(top,text="generate",command = generate)
    button.grid(row = rowCount.current(),column = colCount.next())
    finishRow()
    
class Categories(Listbox):
    all = ["AudioVideo","Audio","Video","Development","Education",
           "Game","Graphics","Network","Office","Science",
           "Settings","System","Utility"]
    def __init__(self,master=None,cnf={},**kw):
        kw["selectmode"]=MULTIPLE
        kw["height"]=len(self.all)
        Listbox.__init__(self,master,cnf,**kw)
        for k,v in zip(range(len(self.all)),self.all):
            self.insert(k,v)
    def get(self):
        chosen = self.curselection()
        rval = [self.all[int(x)] for x in chosen]
        return ";".join(rval)
        
def addCategoriesButton():
    addLabel("Categories")
    cat = Categories()
    values["Categories"] = cat
    cat.grid(row=rowCount.next(),column=colCount.next())
    finishRow()
    
    
top = Tk()

top.wm_title("Desktop File Generator")
rowCount = Counter()
colCount = Counter()

addTextFieldWithValue("Type","Application")
addTextFieldWithValue("Version","1.0")
addTextField("Name")
addTextField("GenericName")
addTextField("Comment")
addFileChooser("Icon")
addBooleanField("Hidden")
addTextField("OnlyShowIn")
addTextField("NotShowIn")
addBooleanField("DBusActivable")
addFileChooser("TryExec")

class ExecContainer:
    def __init__(self):
        addLabel("Exec")
        execcontainer = Frame(top)
        execcontainer.grid(row = rowCount.current(),column = colCount.next())
        self.pre = StringVar()
        preEntry = Entry(execcontainer,textvariable = self.pre)
        preEntry.pack(side=LEFT)
        path = Button(execcontainer)
        def localChooseFile():
            self.choice = tkFileDialog.askopenfilename()
            path.config(text=self.choice)
        path.config(command = localChooseFile)
        path.pack(side=LEFT)
        self.post = StringVar()
        postEntry = Entry(execcontainer,textvariable=self.post)
        postEntry.pack(side=LEFT)
        finishRow()
    def get(self):
        rval = ""
        if self.pre.get() != "":
            rval += self.pre.get() + " "
        rval += self.choice
        if (self.post.get() != ""):
            rval += " " + self.post.get()
        return rval

values["Exec"] = ExecContainer()

addPathField("Path")
addBooleanField("Terminal")
addTextField("Actions")
addTextField("MimeType")
addCategoriesButton()
addTextField("Keywords")
addBooleanField("StartupNotify")
addTextField("StartupWMClass")
addGenerateButton()

top.mainloop()
