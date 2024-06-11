from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import database
from ttkthemes import ThemedTk

db = database("employee")

f = 'calibri'

root = Tk()
root.title("Employee Management System")
root.geometry("1920x1080+0+0")
root.config(bg="black")
root.state("zoomed")

entries_frame = Frame(root, bg="black")
entries_frame.pack(side=TOP, fill=X)

name = StringVar()
age = StringVar()
doj = StringVar()
email = StringVar()
gender = StringVar()
contact = StringVar()
address = StringVar()


def clearAll():
    name.set("")
    age.set("")
    doj.set("")
    gender.set("")
    email.set("")
    contact.set("")
    address.set("")

def add_emp():

    new_window = Toplevel(root)
    new_window.title("Add Employee")
    new_window.geometry("500x500+0+0")
    new_window.config(bg="black")
    new_window.state("zoomed")

    # Entry frame
    entry_frame = Frame(new_window, bg="black")
    entry_frame.pack(side=TOP, fill=X, pady=80)

    lname = Label(entry_frame, text="Name", font=(f, 18), bg="black", fg="white")
    lname.grid(row=1, column=0, padx=10, pady=10, sticky='w')  
    tname = Entry(entry_frame, textvariable=name, font=(f, 18), width=30)
    tname.grid(row=1, column=1, padx=10, pady=20, sticky='w')  

    lage = Label(entry_frame, text="Age", font=(f, 18), bg="black", fg="white")
    lage.grid(row=1, column=2, padx=10, pady=10, sticky='w')
    tage = Entry(entry_frame, textvariable=age, font=(f, 18), width=30)
    tage.grid(row=1, column=3, padx=10, pady=10, sticky='w')

    ldoj = Label(entry_frame, text="D.O.J", font=(f, 18), bg="black", fg="white")
    ldoj.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    tdoj = Entry(entry_frame, textvariable=doj, font=(f, 18), width=30)
    tdoj.grid(row=2, column=1, padx=10, pady=10, sticky='w')

    lmail = Label(entry_frame, text="Email", font=(f, 18), bg="black", fg="white")
    lmail.grid(row=2, column=2, padx=10, pady=10, sticky='w')
    tmail = Entry(entry_frame, textvariable=email, font=(f, 18), width=30)
    tmail.grid(row=2, column=3, padx=10, pady=10, sticky='w')

    lgender = Label(entry_frame, text="Gender", font=(f, 18), bg="black", fg="white")
    lgender.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    combo = ttk.Combobox(entry_frame, font=(f, 18), width=28, textvariable=gender, state="readonly")
    combo['values'] = ['Male', 'Female', 'Other']
    combo.grid(row=3, column=1, padx=10, pady=10, sticky='w')

    lcontact = Label(entry_frame, text="Contact", font=(f, 18), bg="black", fg="white")
    lcontact.grid(row=3, column=2, padx=10, pady=10, sticky='w')
    tcontact = Entry(entry_frame, textvariable=contact, font=(f, 18), width=30)
    tcontact.grid(row=3, column=3, padx=10, pady=10, sticky='w')

    laddress = Label(entry_frame, text="Address", font=(f, 18), bg="black", fg="white")
    laddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    global taddress
    taddress = Text(entry_frame, width=130, height=5, font=(f, 18))
    taddress.grid(row=5, column=0, padx=10, pady=10, columnspan=4, sticky='w')

    def addEmp():
        if tname.get() == "" or tage.get() == "" or tdoj.get() == "" or tmail.get() == "" or combo.get() == "" or tcontact.get() == "" or taddress.get(1.0, END) == "":
            messagebox.showerror("Error in Input", "Please Fill All the Details")
            return
        db.insert(tname.get(), tage.get(), tdoj.get(), tmail.get(), combo.get(), tcontact.get(), taddress.get(1.0, END))
        messagebox.showinfo("Success", "Record Inserted")

        clearAll()
        new_window.destroy()

    badd = Button(new_window, text="ADD", bg="lightgreen", width=10, command=addEmp)
    badd.pack(pady=10)

    entry_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

global tv

def displayall(tv):
    for i in db.fetch():
        tv.insert("", END, values=i)

def getData(event):
    selected_row = tv.focus()
    data = tv.item(selected_row)
    global row
    row = data["values"]
    name.set(row[1])
    age.set(row[2])
    doj.set(row[3])
    email.set(row[4])
    gender.set(row[5])
    contact.set(row[6])
    taddress.delete(1.0, END)
    taddress.insert(END, row[7])



def dis_emp():
    new_window = Toplevel(root)
    new_window.title("Employee List")
    new_window.geometry("1000x600+100+100")
    new_window.config(bg="black")

    tree_frame = Frame(new_window, bg="black")
    tree_frame.pack(fill=BOTH, expand="true", padx=20, pady=20)

    style = ttk.Style()
    style.theme_use("classic")
    style.configure("mystyle.Treeview", background="black", foreground="white", fieldbackground="black", rowheight=60)
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 16, 'bold'), background="black", foreground="white")

    global tv
    tv = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "D.O.B", "Email", "Gender", "Contact", "Address"), style="mystyle.Treeview")
    tv.pack(fill=X, expand=True)

    tv.heading("ID", text="ID")
    tv.column("ID", width=50)
    tv.heading("Name", text="Name")
    tv.heading("Age", text="Age")
    tv.column("Age", width=50)
    tv.heading("D.O.B", text="D.O.B")
    tv.heading("Email", text="Email")
    tv.heading("Gender", text="Gender")
    tv.heading("Contact", text="Contact")
    tv.heading("Address", text="Address")
    tv.column("Address", width=100)

    tv['show'] = 'headings'

def show_emp():
    dis_emp()
    displayall(tv)

def update_emp():
    global new_window
    new_window = Toplevel(root)
    new_window.title("Employee List")
    new_window.geometry("1000x600+100+100")
    new_window.config(bg="black")

    tree_frame = Frame(new_window, bg="black")
    tree_frame.pack(fill=BOTH, expand="true", padx=20, pady=20)

    style = ttk.Style()
    style.theme_use("classic")
    style.configure("mystyle.Treeview", background="black", foreground="white", fieldbackground="black", rowheight=60)
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 16, 'bold'), background="black", foreground="white")

    global tv
    tv = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "D.O.B", "Email", "Gender", "Contact", "Address"), style="mystyle.Treeview")
    tv.pack(fill=X, expand=True)

    # Define headings and columns
    tv.heading("ID", text="ID")
    tv.column("ID", width=50, anchor=CENTER)
    tv.heading("Name", text="Name")
    tv.heading("Age", text="Age")
    tv.column("Age", width=50, anchor=CENTER)
    tv.heading("D.O.B", text="D.O.B")
    tv.heading("Email", text="Email")
    tv.heading("Gender", text="Gender")
    tv.heading("Contact", text="Contact")
    tv.heading("Address", text="Address")
    tv.column("Address", width=100)

    tv['show'] = 'headings'

    #tv.bind("<FocusIn>", getData)
    tv.bind("<<TreeviewSelect>>", getData)
    displayall(tv)

    def on_treeview_focus(event):
        selected_item = tv.selection()
        if selected_item:
            item_values = tv.item(selected_item, 'values')
            global row1
            row1 = item_values[0]
            new_window2 = Toplevel(root)  # Create a new Toplevel window
            new_window2.title("Add Employee")
            new_window2.geometry("500x500+0+0")
            new_window2.config(bg="black")
            new_window2.state("zoomed")

    # Entry frame
            entry_frame = Frame(new_window2, bg="black")
            entry_frame.pack(side=TOP, fill=X, pady=80)

            lname = Label(entry_frame, text="Name", font=(f, 18), bg="black", fg="white")
            lname.grid(row=1, column=0, padx=10, pady=10, sticky='w')  # Align label to the right
            tname = Entry(entry_frame, textvariable=name, font=(f, 18), width=30)
            tname.grid(row=1, column=1, padx=10, pady=20, sticky='w')  # Align entry to the left

            lage = Label(entry_frame, text="Age", font=(f, 18), bg="black", fg="white")
            lage.grid(row=1, column=2, padx=10, pady=10, sticky='w')
            tage = Entry(entry_frame, textvariable=age, font=(f, 18), width=30)
            tage.grid(row=1, column=3, padx=10, pady=10, sticky='w')

            ldoj = Label(entry_frame, text="D.O.J", font=(f, 18), bg="black", fg="white")
            ldoj.grid(row=2, column=0, padx=10, pady=10, sticky='w')
            tdoj = Entry(entry_frame, textvariable=doj, font=(f, 18), width=30)
            tdoj.grid(row=2, column=1, padx=10, pady=10, sticky='w')

            lmail = Label(entry_frame, text="Email", font=(f, 18), bg="black", fg="white")
            lmail.grid(row=2, column=2, padx=10, pady=10, sticky='w')
            tmail = Entry(entry_frame, textvariable=email, font=(f, 18), width=30)
            tmail.grid(row=2, column=3, padx=10, pady=10, sticky='w')

            lgender = Label(entry_frame, text="Gender", font=(f, 18), bg="black", fg="white")
            lgender.grid(row=3, column=0, padx=10, pady=10, sticky='w')
            combo = ttk.Combobox(entry_frame, font=(f, 18), width=28, textvariable=gender, state="readonly")
            combo['values'] = ['Male', 'Female', 'Other']
            combo.grid(row=3, column=1, padx=10, pady=10, sticky='w')

            lcontact = Label(entry_frame, text="Contact", font=(f, 18), bg="black", fg="white")
            lcontact.grid(row=3, column=2, padx=10, pady=10, sticky='w')
            tcontact = Entry(entry_frame, textvariable=contact, font=(f, 18), width=30)
            tcontact.grid(row=3, column=3, padx=10, pady=10, sticky='w')

            laddress = Label(entry_frame, text="Address", font=(f, 18), bg="black", fg="white")
            laddress.grid(row=4, column=0, padx=10, pady=10, sticky='w')
            global taddress
            taddress = Text(entry_frame, width=130, height=5, font=(f, 18))
            taddress.grid(row=5, column=0, padx=10, pady=10, columnspan=4, sticky='w')

            def upEmp():
                if tname.get() == "" or tage.get() == "" or tdoj.get() == "" or tmail.get() == "" or combo.get() == "" or tcontact.get() == "" or taddress.get(1.0, END) == "":
                    messagebox.showerror("Error in Input", "Please Fill All the Details")
                    return
                db.update(tname.get(), tage.get(), tdoj.get(), tmail.get(), combo.get(), tcontact.get(), taddress.get(1.0, END),row1)
                messagebox.showinfo("Success", "Record Updated")

                clearAll()
                new_window2.destroy()
                new_window.destroy()

            bup = Button(new_window2, text="UPDATE", bg="lightgreen", width=10, command=upEmp)
            bup.pack(pady=10)

            entry_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

            
            

    tv.bind("<FocusIn>", on_treeview_focus)



'''def dele():
    # Define dele function to delete record and destroy window
    db.delete(row1)
    messagebox.showinfo("Success", "Record Deleted")
    new_window.destroy()'''

def del_emp():
    global new_window  # Declare new_window as global
    new_window = Toplevel(root)
    new_window.title("Employee List")
    new_window.geometry("1000x600+100+100")
    new_window.config(bg="black")

    tree_frame = Frame(new_window, bg="black")
    tree_frame.pack(fill=BOTH, expand="true", padx=20, pady=20)

    style = ttk.Style()
    style.theme_use("classic")
    style.configure("mystyle.Treeview", background="black", foreground="white", fieldbackground="black", rowheight=60)
    style.configure("mystyle.Treeview.Heading", font=('Calibri', 16, 'bold'), background="black", foreground="white")

    global tv
    tv = ttk.Treeview(tree_frame, columns=("ID", "Name", "Age", "D.O.B", "Email", "Gender", "Contact", "Address"), style="mystyle.Treeview")
    tv.pack(fill=X, expand=True)

    # Define headings and columns
    tv.heading("ID", text="ID")
    tv.column("ID", width=50, anchor=CENTER)
    tv.heading("Name", text="Name")
    tv.heading("Age", text="Age")
    tv.column("Age", width=50, anchor=CENTER)
    tv.heading("D.O.B", text="D.O.B")
    tv.heading("Email", text="Email")
    tv.heading("Gender", text="Gender")
    tv.heading("Contact", text="Contact")
    tv.heading("Address", text="Address")
    tv.column("Address", width=100)

    tv['show'] = 'headings'

    tv.bind("<FocusIn>", getData)
    tv.bind("<<TreeviewSelect>>", getData)
    displayall(tv)

    def on_treeview_focus(event):
        selected_item = tv.selection()
        item_values = tv.item(selected_item, 'values')
        global row1
        row1 = item_values[0]
        db.delete(row1)
        messagebox.showinfo("Success", "Record Deleted")
        new_window.destroy()
            

    tv.bind("<FocusIn>", on_treeview_focus)
    #tv.bind("<<TreeviewSelect>>", on_treeview_focus)


    


badd = Button(entries_frame, command=add_emp, text="ADD", bg="lightgreen", width=10).grid(row=0, column=0, padx=50, pady=10)

bdel = Button(entries_frame, command=del_emp, text="DELETE", bg="#f1807e", width=10).grid(row=1, column=0, padx=50, pady=10)

bshow = Button(entries_frame, command=show_emp, text="EMPLOYEES", bg="#ecef6e", width=10).grid(row=2, column=0, padx=50, pady=10)

bupdate = Button(entries_frame, command=update_emp, text="UPDATE", bg="#ecef6e", width=10).grid(row=3, column=0, padx=50, pady=10)


root.mainloop()
