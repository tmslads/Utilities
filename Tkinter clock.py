# Tkinter clock
# Need to learn classes to do this properly
# Will do that soon

import tkinter
import time

clock = tkinter.Tk()


def get_time():
    currenttime = time.localtime()
    hrs = currenttime.tm_hour
    mins = currenttime.tm_min
    secs = currenttime.tm_sec
    print(hrs, mins, secs)
    display.config(text=f"{hrs}:{mins}:{secs}")


display = tkinter.Label(clock, font=("Helvetica", 69, "bold"), bg="black", fg="red")
display.grid(row=0, column=0, sticky="NSEW")
clock.after(1000, get_time)
clock.mainloop()
