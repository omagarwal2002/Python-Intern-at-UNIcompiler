# Youtube Downloader
#importing the required modules
from tkinter import *
from pytube import YouTube
import os

#defining the window and its components
root = Tk()
root.geometry('700x500')
root.configure(bg='lemon chiffon')
root.resizable(0,0)
bg = PhotoImage(file = "C:/Users/dell/Downloads/giphy.gif")
p1 = PhotoImage(file = 'C:/Users/dell/Downloads/Subscribe Youtube.gif')
root.iconphoto(False, p1)
Label( root, image = bg).place(x = 120,y = 220)
root.title("YOUTUBE DOWNLOADER")
Label(root,text = 'Youtube Downloader', font ='Courier 20 bold').pack()
link = StringVar()
Label(root, text = 'Paste Link Here:', font = 'arial 15 bold').place(x= 280 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 130, y = 90)

#defining command functions
def Downloader():     
    url =YouTube(str(link.get()))
    destination = 'F:/VS Code/UNIcompiler/'
    if var.get() == 1:
        if res.get() == 720:
            video = url.streams.filter(res="720p").first()
            video.download(output_path=destination)
            Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 285 , y = 420)
        elif res.get() == 1080:
            video = url.streams.filter(res="1080p").first()
            video.download(output_path=destination)
            Label(root, text = 'DOWNLOADED', font = 'Times 15').place(x= 285 , y = 420)
    elif var.get() == 2:
        video = url.streams.filter(only_audio=True).first()
        out_file= video.download(output_path=destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 285 , y = 420)


def sel():
       selection1 = "You selected the option " + str(var.get())
       print(selection1)
       if(var.get() == 1):
        select_resolution()

def select_resolution():
    Label(root, text = 'Select the resolution of video: ', font = 'arial 10').place(x= 400 , y = 130)

    R3 = Radiobutton(root, text="720p", variable=res, value=720, command=radio)
    R3.place(x = 400, y = 150)

    R4 = Radiobutton(root, text="1080p", variable=res, value=1080, command=radio)
    R4.place(x = 400, y = 180)

def radio():
    selection2 = "You selected the option " + str(res.get()) +"p"
    print(selection2)
    pass


#defining the checkbutton
Label(root, text = 'Select the required format of video: ', font = 'arial 10').place(x= 80 , y = 130)
var = IntVar()
res = IntVar()
R1 = Radiobutton(root, text="MP-4", variable=var, value=1, command=sel)
R1.place(x = 80, y = 150)

R2 = Radiobutton(root, text="MP-3", variable=var, value=2, command=sel)
R2.place(x = 80, y = 180)


#defining the download button  
Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'cyan', padx = 2, command = Downloader).place(x=290 ,y = 250)
root.mainloop()
