import cv2


# def ReadQRCode():
#     FileName = file_entry.get()
#     image = ImageTk.PhotoImage(Image.open(FileName))
#     imageSend = Image.open(FileName)
#     image_label = Label(image=image)
#     image_label.image = image
#     canvas.create_window(200,350,window=image_label)
#     data = pyzbar.decode(imageSend)[0].data.decode("utf-8")
#     url_label = Label(root,text="Data",font=("Arial",15,"bold"))
#     canvas.create_window(200,180,window=url_label)
#     data_label = Label(root,text=f"{data}")
#     canvas.create_window(200,200,window=data_label)


video = cv2.VideoCapture(0)

while True:

    _, frame = video.read()
    try:
        detector = cv2.QRCodeDetector()
        data, bbox, straight_qrcode = detector.detectAndDecode(frame)
        if (data == "") or (data == " ") or (data == None): pass
        else:
            print(data)
    except:
        pass

    cv2.imshow("cam",frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()

