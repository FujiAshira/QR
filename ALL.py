from tkinter import *
from tkinter.filedialog import askopenfilename as AskFile
import pyqrcode
import png
import os
from PIL import ImageTk, Image
import cv2
from pyzbar import pyzbar


def GenerateQRCODENoImage():
    Link = Link_entry.get()
    LinkName = Name_entry.get()
    FileName = LinkName+".png"
    URL = pyqrcode.create(Link,version=5,error="H")
    URL.png(FileName,scale=5)
    image = ImageTk.PhotoImage(Image.open(FileName))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,350,window=image_label)
    os.remove(FileName)


def GenerateQRCODEWithImage():
    Link = Link_entry.get()
    LinkName = Name_entry.get()
    FileName = LinkName+".png"
    URL = pyqrcode.create(Link,version=5,error="H")
    URL.png(FileName,scale=5)
    image = ImageTk.PhotoImage(Image.open(FileName))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(200,350,window=image_label)


def ReadQRCode():
    FileName = AskFile().replace("/","\\")
    file_entry = Label(root,text=f"{FileName}")
    canvas.create_window(600,120,window=file_entry)
    image = ImageTk.PhotoImage(Image.open(FileName))
    imageSend = Image.open(FileName)
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(600,350,window=image_label)
    data = pyzbar.decode(imageSend)[0].data.decode("utf-8")
    url_label = Label(root,text="Data",font=("Arial",15,"bold"))
    canvas.create_window(600,180,window=url_label)
    data_label = Label(root,text=f"{data}")
    canvas.create_window(600,200,window=data_label)


def Camera():
    video = cv2.VideoCapture(0)
    Cam_Button.place_forget()
    returndata = ""
    while True:
        _, frame = video.read()
        try:
            detector = cv2.QRCodeDetector()
            data, bbox, straight_qrcode = detector.detectAndDecode(frame)
            if (data == "") or (data == " ") or (data == None): pass
            else:
                returndata = data
                ScanWord = Label(root,text=f"Scan word: {returndata}")
                canvas.create_window(400,550,window=ScanWord)
        except:
            pass
        cv2.putText(frame,text=f"{returndata}",org=(0, 60),color=(255,0,0),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1,thickness=3)
        cv2.putText(frame,text="Press Q to exit",org=(0, 30),color=(0,255,0),fontFace=cv2.FONT_HERSHEY_SIMPLEX,fontScale=1.2,thickness=3)
        cv2.imshow("cam",frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video.release()
    cv2.destroyAllWindows()
    canvas.create_window(400,500,window=Cam_Button)

root = Tk()
root.title("QR code generator")
canvas = Canvas(root,width=800,height=600)
canvas.pack()


app_label = Label(root,text="QR code generator",font=("Arial", 20, "bold"))
canvas.create_window(200,50,window=app_label)
# Link insert
link_label = Label(root,text="Link")
canvas.create_window(200,100,window=link_label)

Name_label = Label(root,text="Name")
canvas.create_window(200,160,window=Name_label)

Link_entry = Entry(root)
canvas.create_window(200,120,window=Link_entry)

Name_entry = Entry(root)
canvas.create_window(200,180,window=Name_entry)

Create_qrcode_No_Image = Button(text="Generate QR CODE no image",command=GenerateQRCODENoImage)
canvas.create_window(100,220,window=Create_qrcode_No_Image)

Create_qrcode_Have_Image = Button(text="Generate QR CODE have image",command=GenerateQRCODEWithImage)
canvas.create_window(300,220,window=Create_qrcode_Have_Image)

#Read

app_label = Label(root,text="QR code reader",font=("Arial", 20, "bold"))
canvas.create_window(600,50,window=app_label)

file_label = Label(root,text="File path")
canvas.create_window(600,100,window=file_label)

ReadQRCode_button = Button(text="Read QR CODE",command=ReadQRCode)
canvas.create_window(600,150,window=ReadQRCode_button)

Cam_Button = Button(text="Open Camera",command=Camera)
canvas.create_window(400,500,window=Cam_Button)


root.mainloop()
