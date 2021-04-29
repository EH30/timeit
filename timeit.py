import tkinter
from libs import app_timer

def main():
    root = tkinter.Tk()
    mframe = tkinter.Frame(root)

    root.title("TimeIt")
    root.geometry("500x300")
    root.iconbitmap("icon.ico")
    
    app = app_timer.AppTimer(root, mframe)
    ver = tkinter.Label(root, text="v1.0")
    ver.place(x=0, y=0)

    mframe.pack(ipadx=100, ipady=70)
    app.lbl.pack()
    app.ent.ent_min.place(x=90, y=70)
    app.ent.ent_sec.place(x=159, y=70)
    app.b_start.place(x=110, y=110)
    app.b_reset.place(x=155, y=110)
    app.err.place(x=50, y=159)
    root.mainloop()

if __name__ == "__main__":
    main()
