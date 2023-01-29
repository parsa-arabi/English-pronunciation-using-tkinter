from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pyttsx3
window = Tk()

photo = PhotoImage(file="icon.ico")
window.iconphoto(False, photo)


file = None
window.title("English pronunciation program")
menubar = Menu(window)
sound = pyttsx3.init()

setting_window = None


window.maxsize(600, 400)
window.minsize(600, 400)
def speed():
    setting_window = Toplevel()
    setting_window.title("setting")
    setting_window.maxsize(200, 300)
    setting_window.minsize(200, 300)
    def push():
        sound.setProperty('rate', w.get())
        messagebox.showinfo("Show info", "Changes are saved, you can exit the window")

    Label(setting_window, text="Specify the speed", font=("Segoe UI Light", 20)).pack()
    w = Scale(setting_window, from_=1, to=250, orient=HORIZONTAL, font=("Segoe UI Light", 20), width=10)
    w.pack(pady=10)
    Button(setting_window, text="ok", command=push, font=("Segoe UI Light", 20)).pack()
    she = Label(setting_window, text="", font=("Segoe UI Light", 20))
    she.pack()

def openfile():
    path = filedialog.askopenfile(initialdir="/", title="open file", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    file = open(path.name, "r")
    sound.say(file.read())
    sound.runAndWait()
    file.close()

def show():
    if entery.get != "":
        sh.config(text="your text : {}".format(entery.get()), font=("Segoe UI Light", 20))
        sound.say("{}".format(entery.get()))
        sound.runAndWait()
    else:
        messagebox.showwarning("Showwarnning", "You did not enter any text")

Label(window, text="enter your text(English)", font=("Segoe UI Light", 20)).pack()
Label(window).pack()
entery = Entry(window, font=("Segoe UI Light", 20), bd=0, width=50)
entery.pack(padx='20')
Label(window).pack()
Label(window).pack()
sh = Label(window, text="(your text after say it!)", font=("Segoe UI Light", 20))
sh.pack()
Button(window, text="say it", command=show, bd=0, bg='#808080', font=("Segoe UI Light", 20)).pack()
Label(window, text="---------------------------------------", font=("Segoe UI Light", 30)).pack()
Button(window, text="open", command=openfile, bd=0, bg='#808080', font=("Segoe UI Light", 20)).pack(padx=100, pady=20, side='right')
Button(window, text="setting", command=speed, bd=0, bg='#808080', font=("Segoe UI Light", 20)).pack(padx=100, pady=20, side='left')
window.mainloop()
