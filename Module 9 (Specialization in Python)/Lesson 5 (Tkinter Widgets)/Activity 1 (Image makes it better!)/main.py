from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title('image')
root.geometry('400x400')

image_path = r"C:\Users\tanvi\OneDrive\Documents\Codingal\Courses\AI & Coding Grandmaster (Grades 9-12)\Module 9 (Specialization in Python)\Lesson 5 (Tkinter Widgets)\Activity 1 (Image makes it better!)\image.jpg"

try:
    upload = Image.open(image_path)
    image = ImageTk.PhotoImage(upload)

    label = Label(root, image=image, height=350, width=300)
    label.place(x=50, y=0)
    
    label.image = image 
    
except FileNotFoundError:
    print(f"Error: Could not find the image at {image_path}")
    label = Label(root, text="Image not found!")
    label.place(x=150, y=150)

label2 = Label(root, text="This is how you add image in Tkinter Window")
label2.place(x=40, y=360)

root.mainloop()