import os
import pygame
from tkinter import *
from tkinter import filedialog
from mutagen.id3 import ID3

root =Tk()
root.geometry("400x400")

songs = []
names = []
index = 0

def next_song(event):
    global index
    index += 1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

def previous_song(event):
    global index
    index -= 1
    pygame.mixer.music.load(songs[index])
    pygame.mixer.music.play()

def stop_song(event):
    pygame.mixer.music.stop()

def choose_directory():
    directory = filedialog.askdirectory()
    os.chdir(directory)

    for l in os.listdir(directory):
        if l.endswith(".mp3"):
            songs.append(l)

    pygame.mixer.init()
    #pygame.mixer.music.load(songs[0])
    #pygame.mixer.music.play()

choose_directory()

label = Label(root,text = "Music Player")
label.pack()

listbox = Listbox(root)
listbox.pack()

for items in songs:
    listbox.insert(0,items)
songs.reverse()
    
prev_button = Button(root,text="Previous")
prev_button.pack()

next_button = Button(root,text="Next")
next_button.pack()

stop_button = Button(root,text="Stop")
stop_button.pack()

next_button.bind("<Button-1>",next_song)
prev_button.bind("<Button-1>",previous_song)
stop_button.bind("<Button-1>",stop_song)


root.mainloop()

    
