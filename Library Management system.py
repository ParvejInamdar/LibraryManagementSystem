from tkinter import *
from tkinter import ttk
import random
from datetime import datetime
import tkinter.messagebox
class Library:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Library Management Sysyem")
        self.root.configure(background='LightCyan2')

        MType=StringVar()
        Ref=StringVar()
        Title=StringVar()
        FirstName=StringVar()
        LastName=StringVar()
        Address=StringVar()
        MobileNo=StringVar()
        BookID=StringVar()
        BookTitle=StringVar()
        Author=StringVar()
        DateBorrowed=StringVar()
        DateDue=StringVar()
        LateReturnFine=StringVar()
        DaysOnLoan=StringVar()

        def reset():
            MType.set("")
            Ref.set("")
            Title.set("")
            FirstName.set("")
            LastName.set("")
            Address.set("")
            MobileNo.set("")
            BookID.set("")
            BookTitle.set("")
            Author.set("")
            DateBorrowed.set("")
            DateDue.set("")
            LateReturnFine.set("")
            DaysOnLoan.set("")
            self.txtFramedetail.delete('1.0',END)

        def delete():
            reset()
            self.txtDisplayr.delete("1.0",END)

        def Display():
            self.txtDisplayr.insert(END,MType.get()+"\t"+Title.get()+"\t"+FirstName.get()+"\t"+LastName.get()+"\t"+Address.get()+"\t"+BookTitle.get()+"\t"+DateBorrowed.get()+"\t"+DaysOnLoan.get()+"\n")
            

        def Exit():
            iExit=tkinter.messagebox.askyesno("Library Management System",'Confrim if you want to exit')
            if iExit>0:
                root.destroy()
                return


        def receipt():
            self.txtDisplayr.insert(END,MType.get())
            #self.txtDisplayr.insert(END,'\t'+Ref.get())
            self.txtDisplayr.insert(END,'\t'+Title.get())
            self.txtDisplayr.insert(END,'\t'+FirstName.get())
            self.txtDisplayr.insert(END,'\t'+LastName.get())
            self.txtDisplayr.insert(END,'\t'+Address.get())
           # self.txtDisplayr.insert(END,'\t'+MobileNo.get())
            #self.txtDisplayr.insert(END,'\t'+BookID.get())
            self.txtDisplayr.insert(END,'\t'+BookTitle.get())
            #self.txtDisplayr.insert(END,'\t'+Author.get())
            self.txtDisplayr.insert(END,'\t'+DateBorrowed.get())
            #self.txtDisplayr.insert(END,'\t'+DateDue.get())
            self.txtDisplayr.insert(END,'\t'+LateReturnFine.get())
        
        Mainframe = Frame(self.root)
        Mainframe.grid()

        #Title of the window
        Titleframe = Frame(Mainframe,width=1350,padx=20,bd=20,relief=RIDGE)
        Titleframe.pack(side=TOP)
        self.lblTitle = Label(Titleframe,width=39,font=('arial',40,'bold'),text='Library Management System',padx=12)
        self.lblTitle.grid()

        #Creating Frames
        Buttonframe = Frame(Mainframe,bd=20,width=1350,height=50,padx=20,relief=RIDGE)
        Buttonframe.pack(side=BOTTOM)
        
        Framedetail = Frame(Mainframe,bd=20,width=1350,height=100,padx=20,relief=RIDGE)
        Framedetail.pack(side=BOTTOM)

        
        

        Dataframe = Frame(Mainframe,bd=20,width=1300,height=400,padx=20,relief=RIDGE)
        Dataframe.pack(side=BOTTOM)

        #Library membership information frame
        Dataframel=LabelFrame(Dataframe,bd=10,width=800,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text='Library Membership Info : ')
        Dataframel.pack(side=LEFT)
        
        #Book details inforamtion frame
        Dataframer=LabelFrame(Dataframe,bd=10,width=450,height=300,padx=20,relief=RIDGE,font=('arial',12,'bold'),text='Book Details : ')
        Dataframer.pack(side=RIGHT)

        #Widget
        self.lblMemberType = Label(Dataframel,font=('arial',12,'bold'),text="Member Type : ",padx=2,pady=2)
        self.lblMemberType.grid(row=0,column=0,sticky=W)
        self.cboMemberType = ttk.Combobox(Dataframel,font=('arial',12,'bold'),state='readonly',textvariable=MType,width=23)
        self.cboMemberType['value']=('','Student','Teacher','Admin')
        self.cboMemberType.current(0)
        self.cboMemberType.grid(row=0,column=1,sticky=W)

        self.lblBookid = Label(Dataframel,font=('arial',12,'bold'),text="Book ID : ",padx=2,pady=2)
        self.lblBookid.grid(row=1,column=0,sticky=W)
        self.lblBookid = Entry(Dataframel,font=('arial',12,'bold'),textvariable=BookID,width=25)
        self.lblBookid.grid(row=1,column=1)

        self.lblref = Label(Dataframel,font=('arial',12,'bold'),text="Reference No : ",padx=2,pady=2)
        self.lblref.grid(row=2,column=0,sticky=W)
        self.lblref = Entry(Dataframel,font=('arial',12,'bold'),textvariable=Ref,width=25)
        self.lblref.grid(row=2,column=1)

        self.lblBooktitle = Label(Dataframel,font=('arial',12,'bold'),text="Book Title : ",padx=2,pady=2)
        self.lblBooktitle.grid(row=3,column=0,sticky=W)
        self.lblBooktitle = Entry(Dataframel,font=('arial',12,'bold'),textvariable=BookTitle,width=25)
        self.lblBooktitle.grid(row=3,column=1)

        self.lblTitle = Label(Dataframel,font=('arial',12,'bold'),text="Title : ",padx=2,pady=2)
        self.lblTitle.grid(row=4,column=0,sticky=W)
        self.cboTitle=ttk.Combobox(Dataframel,state='readonly',font=('arial',12,'bold'),textvariable=Title,width=23)
        self.cboTitle['value']=('','Mr.','Mrs.','Dr.')
        self.cboTitle.current(0)
        self.cboTitle.grid(row=4,column=1)

        self.lblAuthor = Label(Dataframel,font=('arial',12,'bold'),text="Author : ",padx=2,pady=2)
        self.lblAuthor.grid(row=5,column=0,sticky=W)
        self.lblAuthor = Entry(Dataframel,font=('arial',12,'bold'),textvariable=Author,width=25)
        self.lblAuthor.grid(row=5,column=1)

        self.lblFirstname = Label(Dataframel,font=('arial',12,'bold'),text="First Name : ",padx=2,pady=2)
        self.lblFirstname.grid(row=6,column=0,sticky=W)
        self.lblFirstname = Entry(Dataframel,font=('arial',12,'bold'),textvariable=FirstName,width=25)
        self.lblFirstname.grid(row=6,column=1)

        self.lblLastname = Label(Dataframel,font=('arial',12,'bold'),text="Last Name : ",padx=2,pady=2)
        self.lblLastname.grid(row=0,column=3,sticky=W)
        self.lblLastname = Entry(Dataframel,font=('arial',12,'bold'),textvariable=LastName,width=25)
        self.lblLastname.grid(row=0,column=4)

        self.lblDateborrow = Label(Dataframel,font=('arial',12,'bold'),text="Borrow Date : ",padx=2,pady=2)
        self.lblDateborrow.grid(row=1,column=3,sticky=W)
        self.lblDateborrow = Entry(Dataframel,font=('arial',12,'bold'),textvariable=DateBorrowed,width=25)
        self.lblDateborrow.grid(row=1,column=4)

        self.lblDatedue = Label(Dataframel,font=('arial',12,'bold'),text="Due Date : ",padx=2,pady=2)
        self.lblDatedue.grid(row=2,column=3,sticky=W)
        self.lblDatedue = Entry(Dataframel,font=('arial',12,'bold'),textvariable=DateDue,width=25)
        self.lblDatedue.grid(row=2,column=4)

        self.lblAddress = Label(Dataframel,font=('arial',12,'bold'),text="Address : ",padx=2,pady=2)
        self.lblAddress.grid(row=3,column=3,sticky=W)
        self.lblAddress = Entry(Dataframel,font=('arial',12,'bold'),textvariable=Address,width=25)
        self.lblAddress.grid(row=3,column=4)

        self.lblDaysonloan = Label(Dataframel,font=('arial',12,'bold'),text="Days on Loan : ",padx=2,pady=2)
        self.lblDaysonloan.grid(row=4,column=3,sticky=W)
        self.lblDaysonloan = Entry(Dataframel,font=('arial',12,'bold'),textvariable=DaysOnLoan,width=25)
        self.lblDaysonloan.grid(row=4,column=4)

        self.lblFine = Label(Dataframel,font=('arial',12,'bold'),text="Late Return Fine : ",padx=2,pady=2)
        self.lblFine.grid(row=5,column=3,sticky=W)
        self.lblFine = Entry(Dataframel,font=('arial',12,'bold'),textvariable=LateReturnFine,width=25)
        self.lblFine.grid(row=5,column=4)

        self.lblMobile = Label(Dataframel,font=('arial',12,'bold'),text="Mobile No : ",padx=2,pady=2)
        self.lblMobile.grid(row=6,column=3,sticky=W)
        self.lblMobile = Entry(Dataframel,font=('arial',12,'bold'),textvariable=MobileNo,width=25)
        self.lblMobile.grid(row=6,column=4)

        #Right frame
        scrollbar = Scrollbar(Dataframer)
        scrollbar.grid(row=0,column=1,sticky='ns')
        
        self.txtDisplayr = Text(Dataframer,font=('arial',12,'bold'),width = 32,height=13,padx=8,pady=20)
        self.txtDisplayr.grid(row=0,column=2,sticky=W)

        Listofbooks=['Data Structures','Harry Potter Series','The Lord of the Rings','The Alchemist','The Da Vinci Code','The Twilight Saga','Gone With the Wind','Think and Grow Rich']

        def Selectedbook(evt):
            value=str(booklist.get(booklist.curselection()))
            w=value

            if(w=="Data Structures"):
                BookID.set("ISBN 1")
                BookTitle.set("Data Structure")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=="Harry Potter Series"):
                BookID.set("ISBN 2")
                BookTitle.set("Harry Potter")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=='The Lord of the Rings'):
                BookID.set("ISBN 3")
                BookTitle.set("The Lord of the Rings")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=='The Alchemist'):
                BookID.set("ISBN 4")
                BookTitle.set("The Alchemist")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=='The Da Vinci Code'):
                BookID.set("ISBN 5")
                BookTitle.set("The Da Vinci Code")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=='The Twilight Saga'):
                BookID.set("ISBN 6")
                BookTitle.set("The Twilight Saga")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            elif(w=='Gone With the Wind'):
                BookID.set("ISBN 7")
                BookTitle.set("Gone With the Wind")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")

            else:
                BookID.set("ISBN 9")
                BookTitle.set("Think and Grow Rich")
                Author.set("ABCD")
                LateReturnFine.set("Rs.3/-")
                DaysOnLoan.set(14)
                receipt()

                d1=datetime.date.today()
                d2=datetime.timedelta(days=14)
                d3=(d1+d2)
                DateDue.set(d3)
                DateOverDue.set("No")
        
        booklist = Listbox(Dataframer,width=20,height=12,font=('arial',12,'bold'))
        booklist.bind("<<ListboxSelect>>",Selectedbook)
        booklist.grid(row=0,column=0,padx=8)
        scrollbar.config(command=booklist.yview)
        for items in Listofbooks:
            booklist.insert(END,items)

        #Display the data in down
        self.lblLabel=Label(Framedetail,font=('arial',10,'bold'),pady=8,text="Member Type\tTitle\tFirstName\tLastname\tAddress\tBook Title\tDate Borrowed\tDays on Loan")
        self.lblLabel.grid(row=0,column=0)

        self.txtDisplayr = Text(Framedetail,font=('arial',12,'bold'),width = 141,height=5,padx=2,pady=4)
        self.txtDisplayr.grid(row=1,column=0,sticky=W)

        

        #Buttons for operations
        self.btndisplaydata=Button(Buttonframe,text='Display Data',font=('arial',12,'bold'),width=25,bd=4,command=Display)
        self.btndisplaydata.grid(row=0,column=0)

        self.btndelete=Button(Buttonframe,text='Delete',font=('arial',12,'bold'),width=25,bd=4,command=delete)
        self.btndelete.grid(row=0,column=1)

        self.btnreset=Button(Buttonframe,text='Reset',font=('arial',12,'bold'),width=25,bd=4,command=reset)
        self.btnreset.grid(row=0,column=2)

        self.btnexit=Button(Buttonframe,text='Exit',font=('arial',12,'bold'),width=25,bd=4,command=Exit)
        self.btnexit.grid(row=0,column=3)
        
if __name__=='__main__':
    root = Tk()
    app = Library(root)
    root.mainloop()
