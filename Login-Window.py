import sqlite3
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
conn=sqlite3.connect("Project1.db")
print("Database Created")


class login:
    def __init__(self,root):
        root.title("LOGIN WINDOW")
        root.geometry("400x280")
        self.Top = Frame(root, bd=2, relief=RIDGE)
        self.Top.pack(side=TOP, fill=X)
        self.Form = Frame(root, height=200)
        self.Form.pack(side=TOP, pady=20)

        self.lbl_title = Label(self.Top, text="Please Login", font=('times', 15,'bold'), bd=15)
        self.lbl_title.pack(fill=X)
        self.lbl_username = Label(self.Form, text="Username", font=('arial', 14), bd=15)
        self.lbl_username.grid(row=0, sticky='e')
        self.lbl_password = Label(self.Form, text='Password', font=('arial', 14), bd=15)
        self.lbl_password.grid(row=1, sticky='e')
        self.lbl_text = Label(self.Form)
        self.lbl_text.grid(row=2, columnspan=2)

        self.username = Entry(self.Form, font=14)
        self.username.grid(row=0, column=1)
        self.password = Entry(self.Form, font=14, show="*")
        self.password.grid(row=1, column=1)

        self.btn_login = Button(self.Form, text="Login", width=45,command=self.InterfaceForNoteApp)
        self.btn_login.grid(row=3, pady=25, columnspan=2)


    def InterfaceForNoteApp(self):
        self.root = Tk()
        self.root.title("Note Taking App")
        self.root.geometry("600x500")
        self.TopFrame = Frame(self.root, width=500, height=250)
        self.BottomFrame = Frame(self.root, width=500, height=250)
        self.btnAddNewNotes = Button(self.TopFrame, text="Add New Notes>>", fg="white", bg="red", font="dark", bd=7,command=self.AddNewNotes)
        self.btnListAllNotes = Button(self.TopFrame, text="List All Notes", fg="white", bg="red", font="dark", bd=7)
        self.lblSearchNotes = Label(self.TopFrame, text="Search Notes", font="dark")
        self.EntrySearchNotes = Entry(self.TopFrame, width=60)
        self.btnSearch = Button(self.TopFrame, text="Search", width=10, fg="white", bg="red", font="dark", bd=5)
        self.lblNotes = Label(self.TopFrame, text="--Notes--", font="bold")

        self.scrollbar = Scrollbar(self.BottomFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.myList = Listbox(self.BottomFrame, yscrollcommand=self.scrollbar.set, width=500, height=250)
        for line in range(100):
            self.myList.insert(END, "This is line number " + str(line))
        self.myList.pack(side=LEFT, fill=X)
        self.scrollbar.config(command=self.myList.yview)

        self.TopFrame.pack(side=TOP)
        self.BottomFrame.pack(side=BOTTOM)
        self.btnAddNewNotes.grid(row=0, column=0, padx=30, pady=20)
        self.btnListAllNotes.grid(row=0, column=1)
        self.lblSearchNotes.grid(row=1, column=0)
        self.EntrySearchNotes.grid(row=2, column=0, ipady=8)
        self.btnSearch.grid(row=2, column=1)
        self.lblNotes.grid(row=3)
        self.root.mainloop()

    def AddNewNotes(self):
        self.root1 = Tk()
        self.root1.geometry("750x750")
        self.root1.title("ADD NEW NOTES")
        self.top1frame = Frame(self.root1)
        self.lblAddNewNotes = Label(self.top1frame, text="ADD NEW NOTES", height=3, width=20, font=('times',20,'bold'), fg="blue")
        self.lblTitle = Label(self.top1frame, text="TITLE", font="bold")
        self.entryTitle = Entry(self.top1frame, width=80)
        self.labelContent = Label(self.top1frame, text="CONTENT", font=('times',15,'bold'), height=3, width=20)

        self.btnBack = Button(self.top1frame, text="BACK", bd=7, bg='yellow', font='bold',command=self.Back)
        self.btnSave = Button(self.top1frame, text="SAVE", bd=7, bg='light green', font='bold')
        self.btnExit = Button(self.top1frame, text="CANCEL", bd=7, bg='red', font='bold',command=self.Ext)
        self.editArea = tkst.ScrolledText(self.top1frame, wrap='word', bg='beige')

        # for line in range(10000):
        #   editArea.insert('insert',"abc")

        self.top1frame.pack(side=TOP)
        self.lblAddNewNotes.grid(row=0, columnspan=2)
        self.lblTitle.grid(row=1, column=0)
        self.entryTitle.grid(row=1, column=1, ipady=8)
        self.labelContent.grid(row=2, columnspan=2, pady=10)
        self.editArea.grid(row=5, columnspan=3)
        self.btnExit.grid(row=6, column=1, pady=40)
        self.btnSave.grid(row=6, column=2, pady=40)
        self.btnBack.grid(row=6, column=0, pady=40)

        self.root1.mainloop()

    def Ext(self):
        messagebox.showwarning("Confirmation", "Clicking on ok will exit the current Gui")
        self.root1.destroy()

    def Back(self):
        master=Tk()
        self.__init__(master)




master=Tk()
b=login(master)
master.mainloop()
