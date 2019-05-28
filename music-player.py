import os
from tkinter.filedialog import askdirectory
import pygame
from tkinter import *
import time
from mutagen.mp3 import MP3


def raise_frame(frame):
    frame.tkraise()

pygame.mixer.init()

root = Tk()
root.minsize(200, 200)
first = Frame(root)
second = Frame(root)
third = Frame(root)

list_of_songs = []
#time = []
index = 0
mode = ['Happy', 'Sad', 'Motivational', 'Relegious']
final_mode = ""
v = StringVar()
u = StringVar()
w = StringVar()

for frame in (first, second, third):
    frame.grid(row=0, column=0, sticky='news')

"""def countdown():
    global index
    audio = MP3(list_of_songs[index])
    t = audio.info.length* 1
    for t in range(120,-1,-1):
        minutes = t / 60
        seconds = t % 60
        var = "%d:%2d" % (minutes, seconds)
        w.set(var)
        time.sleep(1.0)"""

def next():
    global index
    index += 1
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()
    #countdown()
    update_song_name()

def previous():
    global index
    index -= 1
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()
    #countdown()
    update_song_name()


def play():
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()
    #countdown()
    update_song_name()

def stop():
    pygame.mixer.music.stop()
    v.set("")
    return list_of_songs


def choose():
    directorychooser()
    list_of_songs.reverse()
    list_box.delete(0, 'end')
    for items in list_of_songs:
        list_box.insert(0, items)
    list_of_songs.reverse()


def directorychooser():
    list_of_songs.clear()
    directory = askdirectory()
    os.chdir(directory)
    for files in os.listdir(directory):
        #realdir = os.path.realpath(files)
        #audio = ID3(realdir)
        if files.endswith('.mp3'):
            list_of_songs.append(files)
            #list_of_songs.append(audio['TIT2'])

    #pygame.mixer.init()
    pygame.mixer.music.load(list_of_songs[0])
    pygame.mixer.music.play()
    #countdown()
    update_song_name()


def update_song_name():
    global index
    global list_of_songs
    v.set(list_of_songs[index])
    return list_of_songs

def onselect(evt):
    # Note here that Tkinter passes an event object to onselect()
    global index
    u = evt.widget
    index = int(u.curselection()[0])
    #list_of_songs[index] = u.get(index)
    pygame.mixer.music.load(list_of_songs[index])
    pygame.mixer.music.play()
    update_song_name()
    #print 'You selected item %d: "%s"' % (index, value)

def mode_select(evt):
    global final_mode
    w = evt.widget
    index = int(w.curselection()[0])
    value = w.get(index)
    final_mode = value
    set(value)

def set(val):
    w.set("MODE:---"+val)

#   FIRST FRAME
label = Label(first, text="MUSIC PLAYER").pack()
label1 = Label(first, text="Press Next to PLAY MUSIC").pack(padx = 50)
#choose_dir = Button(first, text="Choose Directory", command=choose).pack(side=LEFT, padx=10)
next1 = Button(first, text="NEXT", command=lambda: raise_frame(second), height = 7, width = 30).pack(side=LEFT, padx=220)

#  SECOND FRAME
label2 = Label(second, text="MUSIC PLAYER").pack()
lb = Listbox(second, height=5)
lb.pack()
lb.insert(END, "Happy")
lb.insert(END, "Sad")
lb.insert(END, "Motivational")
lb.insert(END, "Relegious")
lb.bind('<<ListboxSelect>>', mode_select)
b = Button(second, text="GO", command= lambda:raise_frame(third)).pack( padx=120)


#   THIRD FRAME
label3 = Label(third, text="MUSIC PLAYER").pack()
mode_name = Label(third, textvariable = w).pack()
song_name = Label(third, textvariable = v).pack()
timer = Label(third, text = "0:00").pack()
choose_dir = Button(third, text="Choose Directory", command=choose).pack(side=LEFT, padx=10)
play_song = Button(third, text="PLAY", command=play).pack(side=LEFT, padx=10)
stop_song = Button(third, text="STOP", command=stop).pack(side=LEFT, padx=10)
previous_song = Button(third, text="PREVIOUS", command=previous).pack(side=LEFT, padx=10)
next_song = Button(third, text="NEXT", command=next).pack(side=LEFT, padx=10)
list_box = Listbox(third, width=50)
list_box.pack()
list_box.bind('<<ListboxSelect>>', onselect)

raise_frame(first)
root.mainloop()
