from tkinter import *
import pygame
from tkinter import filedialog
import time
import os 

root = Tk()
root.title('MUSIC PLAYER')
root.geometry("500x300")

#Tạo Pygame Mixer
pygame.mixer.init()

#Lệnh Thêm 1 Nhạc
def them_nhac():
    nhac = filedialog.askopenfilename(initialdir='D:/DuAnMp3/audios/',title="Chọn Một Bài", filetypes=(("File mp3", "*.mp3"), ))
    #Xóa một số thông tin, vị trí file
    nhac = nhac.replace("D:/DuAnMp3/audios/", "")
    nhac = nhac.replace(".mp3", "")
    #Thêm nhạc vào hộp nhạc
    hop_nhac.insert(END, nhac)

#Lệnh Thêm Nhiều Nhạc
def themnhieu_nhac():
    nhacs = filedialog.askopenfilenames(initialdir='D:/DuAnMp3/audios/',title="Chọn Một Bài", filetypes=(("File mp3", "*.mp3"), ))
    for nhac in nhacs:
        #Xóa một số thông tin, vị trí file
        nhac = nhac.replace("D:/DuAnMp3/audios/", "")
        nhac = nhac.replace(".mp3", "")
        #Thêm nhạc vào hộp nhạc
        hop_nhac.insert(END, nhac)

#Chơi Nhạc
def bat_nhac():
    nhac = hop_nhac.get(ACTIVE)
    nhac = f'D:/DuAnMp3/audios/{nhac}.mp3'

    pygame.mixer.music.load(nhac)
    pygame.mixer.music.play(loops=0)


#Dừng Nhạc
def dung_nhac():
    pygame.mixer.music.stop()
    hop_nhac.selection_clear(ACTIVE)

#Nhạc Kế
def tiep_nhac():
    tiep = hop_nhac.curselection()
    tiep = tiep[0]+1
    nhac = hop_nhac.get(tiep)
    nhac = f'D:/DuAnMp3/audios/{nhac}.mp3'
    pygame.mixer.music.load(nhac)
    pygame.mixer.music.play(loops=0)

    hop_nhac.selection_clear(0, END)
    hop_nhac.activate(tiep)
    hop_nhac.selection_set(tiep, last=None)

#Nhạc Trước Đó
def truoc_nhac():
    tiep = hop_nhac.curselection()
    tiep = tiep[0]-1
    nhac = hop_nhac.get(tiep)
    nhac = f'D:/DuAnMp3/audios/{nhac}.mp3'
    pygame.mixer.music.load(nhac)
    pygame.mixer.music.play(loops=0)

    hop_nhac.selection_clear(0, END)
    hop_nhac.activate(tiep)
    hop_nhac.selection_set(tiep, last=None)

#Xóa Nhạc
def xoa_nhac():
    hop_nhac.delete(ANCHOR)
    pygame.mixer.music.stop()

#Xóa Tất Cả Nhạc
def xoanhieu_nhac():
    hop_nhac.delete(0, END)
    pygame.mixer.music.stop()

global dung
dung = False

#Pause Song
def tamdung_nhac(da_dung):
    global dung
    dung = da_dung

    if dung:
        pygame.mixer.music.unpause()
        dung = False
    else:
        pygame.mixer.music.pause()
        dung = True

def open():
	top = Toplevel()
	top.geometry("300x200")
	top.title('SPECIAL')
	my_label = Button(top, text="ẤN VÀO ĐÂY", font=("Helvetica, 15"))
	my_label.pack(pady=50, padx=50)

#Tao Hop Playist
hop_nhac = Listbox(root, bg="pink", fg="black", width=60, selectbackground="gray")
hop_nhac.pack(pady=20)

#Tạo Frame Control
controls_frame = Frame(root)
controls_frame.pack()

#Tạo Nút Điều Khiển
back_button = Button(controls_frame, text="Back", borderwidth=2, command=truoc_nhac)
forward_button = Button(controls_frame, text="Forward", borderwidth=2, command=tiep_nhac)
play_button = Button(controls_frame, text="Play", borderwidth=2, command=bat_nhac)
pause_button = Button(controls_frame, text="Pause", borderwidth=2, command=lambda: tamdung_nhac(dung))
stop_button = Button(controls_frame, text="Stop", borderwidth=2, command=dung_nhac)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

#Tạo Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Tạo Nút Thêm Nhạc
them_nhac_menu = Menu(my_menu)
my_menu.add_cascade(label="Thêm Nhạc", menu=them_nhac_menu)
them_nhac_menu.add_command(label="Thêm Một Bài Nhạc Vào Playlist", command=them_nhac)
them_nhac_menu.add_command(label="Thêm Nhiều Bài Nhạc Vào Playlist", command=themnhieu_nhac)

#Tạo Nút Xóa Nhạc
xoa_nhac_menu = Menu(my_menu)
my_menu.add_cascade(label="Xóa Nhạc", menu=xoa_nhac_menu)
xoa_nhac_menu.add_command(label="Xóa Một Bài Nhạc Từ Playlist", command=xoa_nhac)
xoa_nhac_menu.add_command(label="Xóa Tất Cả Nhạc Từ Playlist", command=xoanhieu_nhac)

#Tạo Nút Xóa Nhạc
special_menu = Menu(my_menu)
my_menu.add_cascade(label="SPECIAL! (OPEN LAST)", menu=special_menu)
special_menu.add_command(label="VIEW IMAGE", command=open)

#Tạo Thanh Tác Giả
zic = Label(root, text='MADE BY VIET HOA & T.L QUYNH NHU 11A5', bd=1, relief=GROOVE, anchor=E)
zic.pack(fill=X, side=BOTTOM, ipady=2)

Tung = Label(root, text='Xin Chào Thầy Tùng FPT!', bd=1, relief=GROOVE, anchor=E)
Tung.pack(fill=X, side=BOTTOM, ipady=2)

root.mainloop()