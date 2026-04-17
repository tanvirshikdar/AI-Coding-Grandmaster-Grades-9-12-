from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title('Denomination Counter')
root.configure(bg='light blue')
root.geometry('650x400')

image_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 6 (Denomination Calculator using Tkinter)\app_img.jpg"

try:
    upload = Image.open(image_path)
    upload = upload.resize((300, 300))
    image = ImageTk.PhotoImage(upload)
    label = Label(root, image=image, bg='light blue')
    label.place(x=180, y=20)
except FileNotFoundError:
    # Adding a backup label just in case the path changes again!
    label = Label(root, text="[Image Not Found]", bg='light blue', fg='red')
    label.place(x=250, y=150)

label1 = Label(root, text="Hey User! Welcome to Denomination Counter Application.", bg='light blue')
label1.place(relx=0.5, y=340, anchor=CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel(root)
    top.title("Currency Denomination Counter")
    top.configure(bg='grey')
    top.geometry('600x400')

    label = Label(top, text="Enter total amount", bg='grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='grey')

    l1 = Label(top, text="2000", bg='grey')
    l2 = Label(top, text="500", bg='grey')
    l3 = Label(top, text="100", bg='grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculator():
        try:
            total_amount = int(entry.get())
            
            note2000 = total_amount // 2000
            remaining = total_amount % 2000
            
            note500 = remaining // 500
            remaining %= 500
            
            note100 = remaining // 100
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)

            t1.insert(0, str(note2000))
            t2.insert(0, str(note500))
            t3.insert(0, str(note100))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid whole number")

    btn = Button(top, text='Calculate', command=calculator, bg='brown', fg='white')

    label.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=170)

    l1.place(x=180, y=200)
    l2.place(x=180, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

root.mainloop()