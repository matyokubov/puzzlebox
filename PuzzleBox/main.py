import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import PhotoImage
from PIL import ImageTk, Image
from pygame import mixer
import json

main_menu = tk.Tk()
main_menu.title("Puzzle Box")
ww = main_menu.winfo_reqwidth()
wh = main_menu.winfo_reqheight()
pr = int(main_menu.winfo_screenwidth()/2 - ww/2)-135
pd = int(main_menu.winfo_screenheight()/2 - wh/2)-100
main_menu.geometry("+{}+{}".format(pr, pd))
main_menu.maxsize(width=500, height=270)
main_menu.minsize(width=500, height=270)
main_menu.configure(bg="cadetblue")

mixer.init()
mixer.music.load("audio/start-menu.mp3")
mixer.music.set_volume(1)
mixer.music.play()

def play(level):
    try:
        global main_menu
        if level=="Easy":
            json_file = open("backend/level.json", "w")
            json_file.write(r'''{
        "m1": 10,"l1": 2,
        "m2": 15,"l2": 3
    }''')
        elif level=="Normal":
            json_file = open("backend/level.json", "w")
            json_file.write(r'''{
        "m1": 18,"l1": 3,
        "m2": 19,"l2": 4
    }''')
        elif level=="Hard":
            json_file = open("backend/level.json", "w")
            json_file.write(r'''{
        "m1": 30,"l1": 5,
        "m2": 26,"l2": 4
    }''')
            
        json_file.close()
        main_menu.withdraw()
        main_menu.destroy()
        mixer.music.stop()
        import game
        exit()
    except UnboundLocalError:
        messagebox.showerror("Error","Darajani tanlang....")
    
def about():
    author = "Samarqand viloyati, Narpay tumani,\nbeshqazoq qishlog'i 67-maktab o'quvchisi Matyoqubov Firdavs"
    helpp = json.load(open("config/game.json"))["about"]["game"]
    messagebox.showinfo("O'yin haqida", f"{helpp}\n\nDasturchi: {author}")

logo=ImageTk.PhotoImage(Image.open('images/logo.png'))
tk.Label(main_menu, image=logo).place(x=0, y=0)

level = tk.StringVar()
level.set("Darajani tanlang...")
frame = tk.Frame(main_menu, width=142, height=20)
sel_lvl = ttk.Combobox(frame, textvariable=level, values=('Easy', 'Normal', 'Hard'), state='readonly')
sel_lvl.place(x=0, y=0)
frame.place(x=190, y=85)

start = tk.Button(main_menu, text="Play", width=50, relief="ridge", highlightbackground="black", highlightcolor="black", highlightthickness=2, command=lambda: play(level.get()))
start.place(x=75, y=115)

a = tk.Button(main_menu, text="About", width=50, relief="ridge", highlightbackground="black", highlightcolor="black", highlightthickness=2, command=lambda: about())
a.place(x=75, y=165)

exitt = tk.Button(main_menu, text="Exit", width=50, relief="ridge", highlightbackground="black", highlightcolor="black", highlightthickness=2, command=lambda: exit())
exitt.place(x=75, y=215)

main_menu.mainloop()