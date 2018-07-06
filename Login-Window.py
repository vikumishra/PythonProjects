import sqlite3
from tkinter import *
import tkinter.scrolledtext as tkst
from tkinter import messagebox
conn=sqlite3.connect("Project1.db")
print("Database Created")
#conn.execute("create table Notes(Id INTEGER PRIMARY KEY ,Title TEXT,Content TEXT,Priority INTEGER)")



cur=conn.cursor()

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
        self.root.geometry("650x700")
        self.TopFrame = Frame(self.root, width=500, height=250)

        self.MiddleFrame=Frame(self.root,width=650,height=200,bg="yellow")

        self.BottomFrame = Frame(self.root, width=500, height=250)
        self.btnAddNewNotes = Button(self.TopFrame, text="Add New Notes>>", fg="white", bg="red", font="dark", bd=7,command=self.AddNewNotes)
        self.btnListAllNotes = Button(self.TopFrame, text="List All Notes", fg="white", bg="red", font="dark", bd=7,command=self.ListAllNotes)
        self.lblSearchNotes = Label(self.TopFrame, text="Search Notes", font="dark")
        self.EntrySearchNotes = Entry(self.TopFrame, width=60)
        self.btnSearch = Button(self.TopFrame, text="Search", width=10, fg="white", bg="red", font="dark", bd=5,command=self.Search)
        self.lblNotes = Label(self.TopFrame, text="--Notes--", font="bold")

        self.btnUpdate = Button(self.MiddleFrame, text="UPDATE", bd=7, bg='yellow', font='bold',command=self.UpdateYourNotes)
        self.btnView = Button(self.MiddleFrame, text="VIEW", bd=7, bg='orange', font='bold',command=self.ViewNoteContent)
        self.btnDelete = Button(self.MiddleFrame, text="DELETE", bd=7, bg='red', font='bold',command=self.DeleteNote)
        self.btnSort = Button(self.MiddleFrame, text="SORT", bd=7, bg='sky blue', font='bold',command=self.PrioritySort)
        self.btnUpdate.pack(side=LEFT, padx=90)
        self.btnDelete.pack(side=RIGHT, padx=90)
        self.btnView.pack(side=TOP, pady=10)
        self.btnSort.pack(side=BOTTOM, pady=10)

        self.scrollbar = Scrollbar(self.BottomFrame)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.myList = Listbox(self.BottomFrame, yscrollcommand=self.scrollbar.set, width=500, height=250,selectmode='single',bg="pink")
        #for line in range(100):
         #   self.myList.insert(END, "This is line number " + str(line))
        self.myList.pack(side=LEFT, fill=X)
        self.scrollbar.config(command=self.myList.yview)

        self.TopFrame.pack(side=TOP)
        self.MiddleFrame.pack()
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
        self.root1.geometry("750x800")
        self.root1.title("ADD NEW NOTES")
        self.top1frame = Frame(self.root1)
        self.lblAddNewNotes = Label(self.top1frame, text="ADD NEW NOTES", height=3, width=20, font=('times',20,'bold'), fg="blue")
        self.lblId=Label(self.top1frame,text="ID",font="bold")
        self.EntryId=Entry(self.top1frame,width=80)
        self.lblTitle = Label(self.top1frame, text="TITLE", font="bold")
        self.entryTitle = Entry(self.top1frame, width=80)
        self.labelContent = Label(self.top1frame, text="CONTENT", font=('times',15,'bold'), height=3, width=20)
        self.lblpriority=Label(self.top1frame,text="PRIORITY",font=('times',15,'bold'))
        self.EntryPriority=Entry(self.top1frame,width=80)


        self.btnBack = Button(self.top1frame, text="BACK", bd=7, bg='yellow', font='bold',command=self.BackFromAddNewNotes)
        self.btnSave = Button(self.top1frame, text="SAVE", bd=7, bg='light green', font='bold',command=self.Add)
        self.btnExit = Button(self.top1frame, text="CANCEL", bd=7, bg='red', font='bold',command=self.ExitAddNewNotes)
        self.editArea = tkst.ScrolledText(self.top1frame, wrap='word', bg='beige')

        # for line in range(10000):
        #   editArea.insert('insert',"abc")

        self.top1frame.pack(side=TOP)
        self.lblAddNewNotes.grid(row=0, columnspan=2)
        self.lblId.grid(row=1,column=0,pady=8)
        self.EntryId.grid(row=1,column=1,pady=8,ipady=4)
        self.lblTitle.grid(row=2, column=0)
        self.lblpriority.grid(row=3,column=0,pady=8)
        self.EntryPriority.grid(row=3,column=1,pady=8,ipady=4)

        self.entryTitle.grid(row=2, column=1, ipady=4)
        self.labelContent.grid(row=4, columnspan=2, pady=10)
        self.editArea.grid(row=5, columnspan=3)
        self.btnExit.grid(row=6, column=1, pady=10)
        self.btnSave.grid(row=6, column=2, pady=10)
        self.btnBack.grid(row=6, column=0, pady=10)

        self.root1.mainloop()

    def ViewNoteContent(self):

        self.root4 = Tk()
        self.root4.geometry("600x350")
        self.root4.title("YOUR NOTES")
        self.frame1 = Frame(self.root4, width=600, height=100)
        self.frame2 = Frame(self.root4, width=600, height=400, bg="yellow")
        self.frame3 = Frame(self.root4, width=600, height=100)

        self.lblNoteContent = Label(self.frame1, text="NOTE CONTENT", height=3, width=600, font=('times', 20, 'bold'),
                                    fg="black", bg="yellow")

        self.scrollbar1 = Scrollbar(self.frame2)
        self.scrollbar1.pack(side=RIGHT, fill=Y)
        self.myList1 = Listbox(self.frame2, yscrollcommand=self.scrollbar1.set, width=600, selectmode='single', bg="pink")
        self.myList1.pack(side=LEFT, fill=X)
        self.scrollbar1.config(command=self.myList1.yview)

        self.btnBack1 = Button(self.frame3, text="BACK", bd=7, bg='light green', font='bold',command=self.BackFromNoteContent)
        self.btnExit1 = Button(self.frame3, text="EXIT", bd=7, bg='red', font='bold',command=self.ExitNoteContent)

        self.frame1.pack(side=TOP)
        self.frame2.pack()
        self.frame3.pack(side=BOTTOM)
        self.lblNoteContent.pack()
        self.btnBack1.pack(side=LEFT, padx=120, pady=20)
        self.btnExit1.pack(side=RIGHT, padx=100, pady=20)

        #Getting Note content of Selected Item
        current_selection1 = self.myList.curselection()
        k = self.myList.get(current_selection1)
        id1 = k[5:6]
        cntnt=cur.execute("Select Content from Notes where Id=?",(id1))
        j=0
        for rows in cntnt:
            self.myList1.insert(j,rows[j])

        self.root4.mainloop()

    def UpdateYourNotes(self):
        self.root5 = Tk()
        self.root5.geometry("750x800")
        self.root5.title("UPDATE NOTES")
        self.top1frames = Frame(self.root5)
        self.lblAddNewNotess = Label(self.top1frames, text="UPDATE YOUR NOTES", height=3, width=20, font=('times', 20, 'bold'),fg="blue")
        self.lblIds = Label(self.top1frames, text="ID", font="bold")
        self.EntryIds = Entry(self.top1frames, width=80)
        self.lblTitles = Label(self.top1frames, text="TITLE", font="bold")
        self.entryTitles = Entry(self.top1frames, width=80)
        self.labelContents = Label(self.top1frames, text="CONTENT", font=('times', 15, 'bold'), height=3, width=20)
        self.lblprioritys = Label(self.top1frames, text="PRIORITY", font=('times', 15, 'bold'))
        self.EntryPrioritys = Entry(self.top1frames, width=80)

        self.btnBacks = Button(self.top1frames, text="BACK", bd=7, bg='yellow', font='bold',command=self.BackFromUpdateYourNotes)
        self.btnSaves = Button(self.top1frames, text="SAVE", bd=7, bg='light green', font='bold',command=self.UpdateNote)
        self.btnExits = Button(self.top1frames, text="CANCEL", bd=7, bg='red', font='bold',command=self.ExitUpdateYourNotes)
        self.editAreas = tkst.ScrolledText(self.top1frames, wrap='word', bg='beige')

        # for line in range(10000):
        #   editArea.insert('insert',"abc")

        self.top1frames.pack(side=TOP)
        self.lblAddNewNotess.grid(row=0, columnspan=2)
        self.lblIds.grid(row=1, column=0, pady=8)
        self.EntryIds.grid(row=1, column=1, pady=8, ipady=4)
        self.lblTitles.grid(row=2, column=0)
        self.lblprioritys.grid(row=3, column=0, pady=8)
        self.EntryPrioritys.grid(row=3, column=1, pady=8, ipady=4)

        self.entryTitles.grid(row=2, column=1, ipady=4)
        self.labelContents.grid(row=4, columnspan=2, pady=10)
        self.editAreas.grid(row=5, columnspan=3)
        self.btnExits.grid(row=6, column=1, pady=10)
        self.btnSaves.grid(row=6, column=2, pady=10)
        self.btnBacks.grid(row=6, column=0, pady=10)

        #Fetching Id from selected item in listbox
        current_selection2 = self.myList.curselection()
        k = self.myList.get(current_selection2)
        id2 = k[5:6]


        self.EntryIds.insert(0,id2)
        self.EntryIds.config(state=DISABLED)
        #Fetching The old data and Showing it on gui
        obj1=cur.execute("Select * from Notes where id=?",(id2))
        for rowss in obj1:
            oldtitle=rowss[1]
            oldcontent=rowss[2]
            oldpriority=rowss[3]

        self.entryTitles.insert(0,oldtitle)
        self.EntryPrioritys.insert(0,oldpriority)
        for j in oldcontent:
            self.editAreas.insert(END, j)


        self.root5.mainloop()





    def BackFromAddNewNotes(self):
        self.root1.destroy()
        self.InterfaceForNoteApp()

    def BackFromNoteContent(self):
        self.root4.destroy()
        self.InterfaceForNoteApp()

    def BackFromUpdateYourNotes(self):
        self.root5.destroy()
        self.InterfaceForNoteApp()

    def ExitAddNewNotes(self):
        messagebox.showwarning("Confirmation", "Clicking on ok will exit the current Gui")
        self.root1.destroy()

    def ExitNoteContent(self):
        messagebox.showwarning("Confirmation","Are You Sure You want to Exit???")
        self.root4.destroy()

    def ExitUpdateYourNotes(self):
        messagebox.showwarning("Confirmation", "Clicking on ok will exit the current Gui")
        self.root5.destroy()




    def Add(self):
        id=self.EntryId.get()
        title=self.entryTitle.get()
        priority=int(self.EntryPriority.get())
        content=str(self.editArea.get(1.0,END))
        cur.execute('Insert INTO Notes Values(?,?,?,?);',(id,title,content,priority))

        self.myList.insert(END,"Id = "+str(id)+"-"+"Title = "+title+" "+"Priority"+"="+str(priority))

        self.EntryId.delete(0,END)
        self.entryTitle.delete(0,END)
        self.EntryPriority.delete(0,END)
        self.editArea.delete(1.0,END)
        messagebox.showinfo("Congratulations", "Note Added")
        print("Value Inserted")

    def ListAllNotes(self):
        cur.execute("Select * from Notes")
        i=0
        for row in cur:
            self.myList.insert(i,"Id = "+str(row[0])+"-"+"Title = "+row[1]+" "+"Priority"+"="+str(row[3]))
            i=i+1


    def PrioritySort(self):
        ct=cur.execute('SELECT * from Notes ORDER BY Priority desc')
        self.myList.delete(0, END)
        i=1
        for row in ct:
            self.myList.insert(i,"Id = " + str(row[0]) + " " + "Title = " + row[1] + " " + "Priority" + "=" + str(row[3]))
            i=i+1

    def DeleteNote(self):
        current_selection=self.myList.curselection()
        k=self.myList.get(current_selection)
        id=k[5:6]
        cur.execute("DELETE FROM NOTES WHERE Id=?;",(id))
        self.myList.delete(current_selection)

    def UpdateNote(self):
        current_selection2 = self.myList.curselection()
        k = self.myList.get(current_selection2)
        id2 = k[5:6]
        obj1 = cur.execute("Select * from Notes where id=?", (id2))
        # Fetching The updated data and updating in database
        newtitle = self.entryTitles.get()
        newpriority = self.EntryPrioritys.get()
        newcontent = self.editAreas.get(1.0, END)
        cur.execute("UPDATE NOTES SET Title=? , Content=? , Priority=? where Id=?",(newtitle, newcontent, newpriority, id2))
        self.myList.delete(0, END)
        cur.execute("Select * from Notes")
        i = 0
        for row in cur:
            self.myList.insert(i,"Id = " + str(row[0]) + "-" + "Title = " + row[1] + " " + "Priority" + "=" + str(row[3]))
            i = i + 1
        self.root5.destroy()
        messagebox.showinfo("Congratulations ","Data Updated")

    def Search(self):
        titls=self.EntrySearchNotes.get()
        print(titls)

        obj1=conn.execute('Select * from Notes where Title=?', (titls,))
        i = 0
        for row in obj1:
            self.myList.insert(i, "Id = " + str(row[0]) + " " + "Title = " + row[1] + " " + "Priority" + "=" + str(row[3]))
            i = i + 1



master=Tk()
b=login(master)
master.mainloop()
conn.commit()
