#Mp3 Player
#importing required libraries
from tkinter import *
from tkinter import Tk
from tkinter import filedialog
from pygame import mixer
import os

#defining the window and its components
root = Tk()
root.geometry('900x700')
root.configure(bg='powder blue')
root.resizable(0,0)

p1 = PhotoImage(file = 'C:/Users/dell/Downloads/1_IDJ4x4E-bOypnEZdA5TGHQ.gif')
root.iconphoto(False, p1)

root.title("Music Player")

#defining required command functions
def Add_Music():
    #path = filedialog.askdirectory()
    path = "C:/Users/dell/Music/"
    if path:
        os.chdir(path)
        songs = os.listdir(path)
 
        for song in songs:
            if song.endswith(".mp3"):
                Playlist.insert(END, song)
 
def Play_Music():
    mixer.init()
    Music_Name= Playlist.get(ACTIVE)
    print(Music_Name[0:-4])
    mixer.music.load(Playlist.get(ACTIVE))
    mixer.music.play()

# setting the icon
Top_Image = PhotoImage(file="C:/Users/dell/Downloads/0ae6d6b90d8f455ce7f742ff1887d714.gif")
Label(root, image=Top_Image, bg="#0f1a2b").place(x=50,y=20)
 
# setting the buttons
Button(root,text = 'PLAY', font = 'arial 15 bold' ,bg = 'medium spring green', padx = 2, command = Play_Music).place(x=410, y=110)
Button(root,text = 'STOP', font = 'arial 15 bold' ,bg = 'tomato', padx = 2, command = mixer.music.stop).place(x=310, y=180)
Button(root,text = 'RESUME', font = 'arial 15 bold' ,bg = 'yellow', padx = 2, command = mixer.music.unpause).place(x=395, y=180)
Button(root,text = 'PAUSE', font = 'arial 15 bold' ,bg = 'yellow', padx = 2, command = mixer.music.pause).place(x=510, y=180)
 
#music
Frame_Music = Frame(root, bd=2, relief = RIDGE)
Frame_Music.place(x=200, y=420, width=600, height=250)
 
Button(root, text="Add Music", width=15, height=2, font=("times new roman",12,"bold"),fg="Black", bg="#21b3de", command= Add_Music).place(x=150, y=350)
 
Scroll = Scrollbar(Frame_Music)
Playlist = Listbox(Frame_Music, width=100, font=("Times new roman",10), bg="#333333", fg="grey", selectbackground="lightblue", cursor="hand2", bd=0, yscrollcommand=Scroll.set)
Scroll.config(command=Playlist.yview)
Scroll.pack(side=RIGHT, fill=Y)
Playlist.pack(side=LEFT, fill=BOTH)
 
root.mainloop()