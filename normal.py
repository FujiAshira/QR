from tkinter import *
import pyqrcode
import png
import os
from PIL import ImageTk, Image

def GenerateQRCODENoImage():
    Link = Link_entry.get()
    LinkName = Name_entry.get()
    FileName = LinkName+".png"
    URL = pyqrcode.create(Link,version=2,error="L")
    print(URL.text())
    URL.png(FileName,scale=5)
    image = ImageTk.PhotoImage(Image.open(FileName))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,370,window=image_label)
    os.remove(FileName)

def GenerateQRCODEWithImage():
    Link = Link_entry.get()
    LinkName = Name_entry.get()
    FileName = LinkName+".png"
    URL = pyqrcode.create(Link,version=2,error="L")
    print(URL.text())
    URL.png(FileName,scale=5)
    image = ImageTk.PhotoImage(Image.open(FileName))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,370,window=image_label)

root = Tk()
root.title("QR code generator")
canvas = Canvas(root,width=400,height=500)
canvas.pack()


app_label = Label(root,text="QR code generator",font=("Arial", 20, "bold"))
canvas.create_window(200,50,window=app_label)
# Link insert
link_label = Label(root,text="Link")
canvas.create_window(200,100,window=link_label)

Name_label = Label(root,text="Name")
canvas.create_window(200,160,window=Name_label)

Link_entry = Entry(root)
canvas.create_window(200,130,window=Link_entry)

Name_entry = Entry(root)
canvas.create_window(200,180,window=Name_entry)

Create_qrcode_No_Image = Button(text="Generate QR CODE no image",command=GenerateQRCODENoImage)
canvas.create_window(100,230,window=Create_qrcode_No_Image)

Create_qrcode_Have_Image = Button(text="Generate QR CODE have image",command=GenerateQRCODEWithImage)
canvas.create_window(300,230,window=Create_qrcode_Have_Image)

root.mainloop()
