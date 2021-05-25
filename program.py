import tkinter as tk
from tkinter.constants import BOTH, LEFT, RIGHT, TRUE

def format_time(time):
    minutes = time // 60
    seconds = time % 60
    return f"{minutes}:{seconds}"

def update():
    if root.running:
        root.current_time -= 1
    time_lb.config(text=format_time(root.current_time))
    time_lb.after(1000,update)

def start():
    root.running = True

def pause():
    root.running = False

def reset():
    root.running = False
    root.current_time = root.time

def set_time():
    top = tk.Toplevel()
    top.title("Set Time")
    top.geometry("200x150")
    
    time = tk.StringVar(top,root.time)

    def ok():
        root.time = int(time.get())
        root.current_time = root.time
        top.destroy()

    tk.Label(top,text="Enter time in seconds").grid(row=0,column=0,columnspan=2)
    
    new_time_ent = tk.Entry(top,textvariable=time)
    new_time_ent.grid(row=1,column=0,columnspan=2)
    
    ok_btn = tk.Button(top,text="Ok",command=ok)
    ok_btn.grid(row=2,column=0)

    cancel_btn = tk.Button(top,text="Cancel",command=top.destroy)
    cancel_btn.grid(row=2,column=1)



# --- Main Program ---
# Create Window
root = tk.Tk()
root.title("Scoreboard Program")
root.geometry("1920x1080")
root.resizable = (False,False)

root.time = 330
root.current_time = root.time
root.running = False

# Configure
root.config(bg = '#545f66')

# Create elements

photo_1 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_play_3923854.png")
photo_1_image = photo_1.subsample(3, 3)

time_lb = tk.Label(root,text=format_time(root.current_time),font=("Rockwell",150))
time_lb.grid(row=0,column=0)

start_btn = tk.Button(root,text="Start",font=("Rockwell",30),command=start)
start_btn.grid(row=1,column=0, pady=10, padx=30, )

pause_btn = tk.Button(root,text="Pause",font=("Rockwell",30),command=pause)
pause_btn.grid(row=2,column=0, columnspan=4, pady=10, padx=30)

reset_btn = tk.Button(root,text="Reset",font=("Rockwell",30),command=reset)
reset_btn.grid(row=3,column=0,columnspan=10, pady=10, padx=30)

set_btn = tk.Button(root,text="Set",font=("Rockwell",30),command=set_time)
set_btn.grid(row=4,column=0,columnspan=4, pady=10, padx=30)

# Actual Scoreboard Numbers

# Global Variables

time_lb.after(1000,update())
root.mainloop()