import tkinter
import playsound
import threading
from tkinter.constants import DISABLED, NORMAL


class AppEntry:
    def __init__(self, root):
        self.st_min = tkinter.StringVar(value="01")
        self.st_sec = tkinter.StringVar(value="00")
        self.ent_min = tkinter.Entry(root, textvariable=self.st_min)
        self.ent_sec = tkinter.Entry(root, textvariable=self.st_sec)
        self.ent_min.config(width=10)
        self.ent_sec.config(width=10)
        self.st_min.trace("w", lambda *args: self.max_chars())
        self.st_sec.trace("w", lambda *args: self.max_chars())


    def max_chars(self):
        if len(self.st_min.get()) > 2:
            self.st_min.set(self.st_min.get()[-1])
        
        elif len(self.st_sec.get()) > 2:
            self.st_sec.set(self.st_sec.get()[-1])

class AppTimer:
    def __init__(self, root, frame):
        self.min = 0
        self.sec = 0
        self.on = 0
        self.sound = False
        self.ent = AppEntry(frame)
        self.b_start = tkinter.Button(frame, text="start", fg="black", bd=3, command=self.timer)
        self.b_reset = tkinter.Button(frame, text="stop", fg="black", bd=3, command=self.reset)
        self.lbl = tkinter.Label(frame, text="00:00", font=("", 30))
        self.err = tkinter.Label(frame, text="")
        
    def reset(self):
        if self.on != 0:
            self.on = 2
        
        self.sound = False
    
    def check_in_err(self, min, sec):
        if min > 59 or sec > 59:
            return -1
        
        if min < 0 or sec < 0:
            return -1

        return 0
    

    def in_user(self):
        if self.on == 1:
            return 0
        
        min = self.ent.ent_min.get()
        sec = self.ent.ent_sec.get()
        if len(min) == 0 or len(sec) == 0:
            return -1
        

        if not min.isdigit() or not sec.isdigit():
            return -1
        
        min = int(min)
        sec = int(sec)
        
        if self.check_in_err(min, sec) != 0:
            self.err.config(text="minutes and seconds should be in 0-59")
            return -1
        
        self.min = int(min)
        self.sec = int(sec)
        self.on = True
        return 0

    def text_format(self, min, sec):
        st = ""
        if min < 10:
            st += "0{0}:".format(min)
        else:
            st += "{0}:".format(min)

        if sec < 10:
            st += "0{0}".format(sec)
        else:
            st += "{0}".format(sec)
        
        return st
    
    def alarm_on(self):
        while self.sound:
            playsound.playsound("libs/Alarm-clock-bell-ringing-sound-effect.mp3")
        self.b_start["state"] = NORMAL

    def timer(self):
        if self.on == 2:
            self.on = 0
            self.b_start["state"] = NORMAL
            return 1
        
        if self.in_user() != 0:
            return -1
        
        self.b_start["state"] = DISABLED
        self.lbl.config(text=self.text_format(self.min, self.sec))
        
        if self.min != -1 and self.on == 1:
            if self.sec == 0:
                self.min -= 1
                self.sec = 59
                self.lbl.after(1000, self.timer)
            else:
                self.sec -= 1
                self.lbl.after(1000, self.timer)
        else:
            self.on = 0
            self.sound = True
            self.lbl.config(text="00:00")
            th = threading.Thread(target=self.alarm_on)
            th.start()

        return 0
