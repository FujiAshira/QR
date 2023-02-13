from pyzbar import pyzbar
from tkinter import *
from PIL import ImageTk, Image


def ReadQRCode():
    FileName = file_entry.get()
    image = ImageTk.PhotoImage(Image.open(FileName))
    imageSend = Image.open(FileName)
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,350,window=image_label)
    data = pyzbar.decode(imageSend)[0].data.decode("utf-8")
    url_label = Label(root,text="Data",font=("Arial",15,"bold"))
    canvas.create_window(200,180,window=url_label)
    data_label = Label(root,text=f"{data}")
    canvas.create_window(200,200,window=data_label)



root = Tk()
root.title("QR code reader")
canvas = Canvas(root,width=400,height=500)
canvas.pack()

app_label = Label(root,text="QR code reader",font=("Arial", 20, "bold"))
canvas.create_window(200,50,window=app_label)

file_label = Label(root,text="File name")
canvas.create_window(200,100,window=file_label)

file_entry = Entry(root)
canvas.create_window(200,120,window=file_entry)

ReadQRCode_button = Button(text="Read QR CODE",command=ReadQRCode)
canvas.create_window(200,150,window=ReadQRCode_button)

root.mainloop()
