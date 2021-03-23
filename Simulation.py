from tkinter import *
from PIL import Image, ImageTk
from random import *


root =Tk()
root.geometry('1920x1080+0+0')
root.title('  Simulation  ')
root.configure(background='white')

#globally declared image
image4= Image.open("pseudocode.jpg")
image4 = image4.resize((1200,840), Image.ANTIALIAS)
photo4 = ImageTk.PhotoImage(image4)

image5= Image.open("information.png")
image5 = image5.resize((1500,620), Image.ANTIALIAS)
photo5 = ImageTk.PhotoImage(image5)





def info():
    window4 = Toplevel()
    window4.title("Info")
    window4.geometry("1920x1080")
    window4.configure(background='white')
    #scrollbar = Scrollbar(window4)
    #scrollbar.pack(side=RIGHT, fill=Y)

    linfo = Label(window4, text='hello',fg="black", bg='white', image=photo5, highlightthickness=40)
    linfo.pack()



def psu():
    window3 = Toplevel()
    window3.title("Join")
    window3.geometry("1920x1080")
    window3.configure(background='white')
    labp = Label(window3, text='hello', fg="black", bg='white', image=photo4, highlightthickness=40)
    labp.pack()
    # Start the GUI

#Start button window here
def startwin():
    win = Toplevel()
    win.title("project")
    win.configure(background="snow")
    win.geometry('1920x1080')

    #sorting algorithm
    def ssort(win,l):
        n=len(l)
        for i in range(0,n):
            minn=i
            passb = Label(win, text="pass {}".format(i), fg='black', bg='cyan', width=7, height=1, font=20)
            passb.place(x=8, y=190+(60*(i+1)))

            for k in range(0,i):
                b = Label(win, text=l[k], fg='black', bg='yellow', width=7, height=1, font=20)
                b.place(x=100 + (70 * (k)), y=190 + (60 * (i + 1)))

            for j in range(i+1,n):
                if(l[j]<l[minn]):
                    minn=j

                b= Label(win, text=l[j-1], fg='black', bg='orange', width=7, height=1, font=20)
                b.place(x=50+(70*(j)), y=190 + (60 * (i + 1)))

            bg = Label(win, text=l[j], fg='black', bg='orange', width=7, height=1, font=20)
            bg.place(x=120 + (70 * (j)), y=190 + (60 * (i + 1)))

            bmin= Label(win, text=l[minn], fg='black', bg='LightBlue', width=5, height=1, font=20)
            bmin.place(x=50 + (70 * (minn+1)), y=190 + (60 * (i + 1)))
            temp=l[i]
            l[i]=l[minn]
            l[minn]=temp

            #alternate logic for swapping not correctly working

            '''sw1= Label(win, text=l[i], fg='black', bg='red', width=7, height=1, font=20)
            sw1.place(x=50 + (70 * (j-1)), y=190 + (60 * (i + 1)))

            sw2= Label(win, text=temp, fg='black', bg='orange', width=7, height=1, font=20)
            sw2.place(x=50 + (70 * (minn-1)), y=190 + (60 * (i + 1)))'''


        print(l)



    #function for making manually inputted array
    def make(win,e2,l):
        i=int(e2)
        l.append(i)
        print(l)
        arr = Label(win, text=l, fg='dark blue', bg='orange',width=40,height=1 ,font=20)
        arr.place(x=8,y=190)
        run = Button(canvas, text='RUN', width=12,bg="azure", font=20, command=lambda: ssort(win, l))
        run.grid(row=2, column=8, padx=100, pady=1, )



    #function for displaying entry for entering elements manually
    def manual(canvas):

        l=[]
        text2 = Label(canvas, text='Enter Element  :',bg="azure", font=20)
        text2.grid(row=1, column=4, padx=10, pady=20)
        e2 = Entry(canvas, bg='white', width=30)
        e2.grid(row=1, column=5)
        append=Button(canvas, text='Append',width=12, font=20,bg="azure",command=lambda:make(win,e2.get(),l))
        append.grid(row=2, column=5, padx=1, pady=1,)


    #function for making assending array
    def assend(win,e):

        l=[]
        n=int(e)
        for i in range (0,n):
            l.append(i+1)
            print(l)
        arr = Label(win,text=l, fg='dark blue', bg='orange',width=40,height=1 , font=20)
        arr.place(x=8, y=190)

        run = Button(canvas, text='RUN', width=12, font=20,bg="azure",command=lambda:ssort(win,l))
        run.grid(row=2, column=8, padx=100, pady=1, )


    # function for making assending array
    def dessend(win, e):
        global l
        l = []
        n = int(e)
        k=n
        for i in range(0, n):
            l.append(k)
            k=k-1
            print(l)
        arr = Label(win, text=l, fg='dark blue', bg='orange', width=40, height=1, font=20)
        arr.place(x=8, y=190)

        run = Button(canvas, text='RUN', width=12, font=20,bg="azure", command=lambda: ssort(win, l))
        run.grid(row=2, column=8, padx=100, pady=1, )

    def random1(win, e):
        l = []
        n = int(e)
        for i in range(0, n):
            a = int((random()*100))
            l.append(a)
            print(l)
        arr = Label(win, text=l, fg='black', bg='MediumPurple1', width=40, height=1, font=20)
        arr.place(x=8, y=190)
        run = Button(canvas, text='RUN', width=12, font=20,bg="azure", command=lambda: ssort(win, l))
        run.grid(row=2, column=8, padx=100, pady=1, )

    def reset(win):
        win.destroy()
        startwin()




    #Decoration of start window

    canvas =Frame(win,width=1920,height=300,bg="spring green",highlightthickness=10)
    canvas.pack(fill=X)
    text1 = Label(canvas, text='Number of Elements  :',bg="azure", font=20)
    text1.grid(row=1, column=1,padx=10,pady=20)
    e1 = Entry(canvas, bg='azure', width=30)
    e1.grid(row=1, column=2)

    ascend=Button(canvas, text='Ascending', font=30,bg="azure",command=lambda:assend(win,e1.get()))
    ascend.grid(row=2,column=0,padx=10,pady=30)

    descend = Button(canvas, text='Descending', font=30,bg="azure",command=lambda:dessend(win,e1.get()))
    descend.grid(row=2, column=1, padx=5, pady=30)

    randm = Button(canvas, text='Random', font=30,bg="azure",command=lambda:random1(win,e1.get()))
    randm.grid(row=2, column=2, padx=5, pady=30)

    manul = Button(canvas, text='Manually input Array',bg="azure",width=20, font=30,command=lambda:manual(canvas))
    manul.grid(row=2, column=3, padx=5, pady=30,)

    clear = Button(canvas, text='CLEAR', width=12, font=20, bg="azure",command=lambda:reset(win))
    clear.grid(row=1, column=8, padx=100, pady=1, )








#main window front page decor

image= Image.open("Ramdeobaba-Logo.png")
image = image.resize((300,345), Image.ANTIALIAS)
photo1 = ImageTk.PhotoImage(image)
l1 = Button(root, text='hello', bg='white', image=photo1, highlightthickness=40,relief=FLAT)
l1.place(x=570,y=275)

label1=Label(root,bg='lightslategray',text="Welcome",fg="darkblue",width=1920 ,height=2,font="helvetic 22 bold")
label1.pack(side=TOP)

label2=Label(root,bg='lightslategray',text="Selection Sort Simulation",fg="khaki" ,width=1920,height=3,font="helvetic 35 bold")
label2.pack(side =TOP)

#Start button
image2= Image.open("start.png")
image2 = image2.resize((86,86), Image.ANTIALIAS)
photo2 = ImageTk.PhotoImage(image2)
button1=Button(root,bg='white',activebackground="grey90",image=photo2,cursor="hand2",relief=FLAT,command=startwin)
button1.place(x=1300,y=300)

#Pseudocode Button
button2=Button(root,bg='cyan',text="Pseudocode",fg="black",activeforeground="black",activebackground="green",cursor="hand2",width=20 ,height=2,command=psu,font="helvetic 14")
button2.place(x=50,y=450)

#info button
image3= Image.open("info.png")
image3 = image3.resize((75,75), Image.ANTIALIAS)
photo3 = ImageTk.PhotoImage(image3)

button3=Button(root,bg='snow',text="i",image=photo3,cursor="hand2",width=55 ,height=70,relief=FLAT,command=info)
button3.place(x=45,y=290)

ourmess="Made by:\n  Nikhil Likhar"
message=Message(root,bg="lightgreen",text=ourmess,bd=20,font=30)
message.place(x=1300,y=550)



root.mainloop()

