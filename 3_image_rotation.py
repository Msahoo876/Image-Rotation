from tkinter import *
from tkinter import filedialog
from tkinter import ttk

def cal():
    file1 = filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
    e1.delete(0,END)
    e1.insert(END,file1)
    global a
    a = file1
    

def check():
    if c1.get() == 'Small':
        b = 0.2
    elif c1.get() == 'Medium':
        b = 0.35
    elif c1.get() == 'Large':
        b = 0.5 
    return b

def display():
    import cv2
    b = check()
    c = e3.get()
    deg = cd2.get()
    img = cv2.imread(a,1)
    shapes = img.shape
    rows,cols,frame = shapes
    rot = cv2.getRotationMatrix2D((cols/2,rows/2),int(deg),b)   #  small = 0.2,midum = 0.35, large = 0.5
    image1 = cv2.warpAffine(img,rot,(cols,rows))
    cv2.imshow("Original",img)
    cv2.imshow(c,image1)
    cv2.imwrite(c,image1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

win = Tk()
win.geometry('300x350')
win.title(" Image Rotation ")

l4 = Label(win,text=" Image Rotation ",font=('Arial',18,'bold','italic','underline'))
l4.place(x=50,y=30)

l3 = Label(win,text=" New Image Name :")
l3.place(x=30,y=250)

e3 = Entry(win)
e3.place(x=150,y=250,width=140)

l1 = Label(win,text=" Your Image Name : ")
l1.place(x=30,y=100)

e1 = Entry(win)
e1.place(x=150,y=100,width=140)

ld = Label(win,text=" Select Rotation Degree : ")
ld.place(x=5,y=150)#

cd2 = ttk.Combobox(win)
cd2.place(x=150,y=150)
cd2['value'] = (0,15,30,45,60,75,90,105,120,135,150,165,180,195,210,225,240,255,270,285,300,315,330,345,360)

l2 = Label(win,text=" Select Image Size : ")
l2.place(x=30,y=200)#

c1 = ttk.Combobox(win)
c1.place(x=150,y=200)
c1['values'] = ('Small','Medium','Large')

b1 = Button(win,text="Select Image",command=cal)
b1.place(x=70,y=300)

b2 = Button(win,text="Print Image",command=display)
b2.place(x=160,y=300)



win.mainloop()