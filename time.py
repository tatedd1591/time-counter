import tkinter as tk
from tkinter import Button
from PIL import Image, ImageTk
from tkinter import font as tkFont
import serial
import time


# ser = serial.Serial('COM8', 9600)
global ser
global t1
global t3
reset_time=0
t3 = 0
t1 = time.time()
key = True
key2 = False
key3 = False
check = 0
def set_label():
    global key
    global check
    global key3
    global reset_time
    global t1
    try:
        x = ser.readline()
        x = x.decode('utf-8')
        x = int(x)
    except:
        x = 0
    if x > 400:
        key = False
        label4['text'] = "Finish"
    #waiting (False: cho, True: bat dau)
    if key2 == False:
        label['text'] = "Time: " + format(0,'.1f')
        label2['text'] = "Time wait: " + format(0, '.1f')
        label3['text'] = "Reset: " + format(reset_time, 'd')
        root.after(1, set_label)
        return 0
    # Tinh thoi gian (True: tinh thoi gian, False: tam dung)
    if key == True:
        global time_end
        time_end = time.time() - t1
        label['text'] = "Time: " + format(time_end,'.1f')
        label2['text'] = "Time wait: " + format(0,'.1f')
        label4['text'] = "Ongoing"
    # Tinh thoi gian dung quyen reset (True: dung quyen)
    if key3 == True:
        time_end_2 = time.time() - t3
        # Toi da 5 phut reset
        if time_end_2 > 300:
            key3 = not key3
            key = not key
            t1 = t1 + 3
        label2['text'] = "Time wait: " + format(time_end_2,'.1f')
        label4['text'] = "Reset time"
    # Qua 2 phut
    if time_end > 120:
        key = False
        label4['text'] = "Finish"
    label3['text'] = "Reset: " + format(reset_time, 'd')
    root.after(1, set_label)

# Sự cố cảm biến
def stop():
    global key
    global key3
    global t1
    t1 = time.time() - time_end
    key = not key
    label4['text'] = "Fixing"
# Reset dữ liệu
def restart():
    global key2
    global reset_time
    reset_time=0
    key2 = False
    label4['text'] = "Ready"
# Dùng quyền reset
def reset():
    global t3
    global t1
    global key3
    global key
    global reset_time
    # Tối đa 2 luot reset
    if reset_time<2 or key3==True:
        if key3 == False:
            reset_time = reset_time + 1
        key3 = not key3
        key = not key
    t3 = time.time()
    t1 = time.time() - time_end

# Bat dau dem
def start():
    global key
    global key2
    global key3
    global t1
    global reset_time
    reset_time = 0
    t1 = time.time()
    key2 = not key2
    key = True
    key3 = False

root = tk.Tk()
root.geometry("1920x1080")
label = tk.Label(root, text="placeholder")
label.pack()
label.configure(font=("Times New Roman", 70, "italic"))
label.place(x = 200, y = 250 )

label2 = tk.Label(root, text="placeholder")
label2.pack()
label2.configure(font=("Times New Roman", 70, "italic"))
label2.place(x = 200, y = 400 )

label3 = tk.Label(root, text="placeholder")
label3.pack()
label3.configure(font=("Times New Roman", 70, "italic"))
label3.place(x = 1000, y = 400 )

label4 = tk.Label(root, text="placeholder")
label4['text'] = "Ready"
label4.pack()
label4.configure(font=("Times New Roman", 70, "italic"))
label4.place(x = 1000, y = 250 )

label5 = tk.Label(root, text="placeholder")
label5['text'] = "Vòng loại"
label5.pack()
label5.configure(font=("Times New Roman", 70, "italic"))
label5.place(x = 600, y = 65 )

# img = PhotoImage(file="111.jpg")
img_path = "logo.jpg"
img = Image.open(img_path)
img = img.resize((300,200))
photo = ImageTk.PhotoImage(img)
img_label = tk.Label(root,image=photo)
img_label.pack()
img_label.place(x = 200, y = 25)

btn = Button(root, text = 'START',height= 10, width=20, command = start, bg='#33618b')
btn.place(x=175, y=550)
btn2 = Button(root, text = 'STOP',height= 10, width=20, command = stop , bg='#aa262c')
btn2.place(x=525, y=550)
btn3 = Button(root, text = 'RESET',height= 10, width=20, command = reset , bg='#15ebe0')
btn3.place(x=875, y=550)
btn4 = Button(root, text = 'RESTART',height= 10, width=20, command = restart, bg='#f2e41f')
btn4.place(x=1225, y=550)
set_label()

root.mainloop()