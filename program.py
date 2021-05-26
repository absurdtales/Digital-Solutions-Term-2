import tkinter as tk
from tkinter.constants import ANCHOR, BOTH, LEFT, N, RIGHT, TRUE

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
#root.config(bg = '#545f66')

# Create elements
# Frames
left_frame = tk.Frame(root)
left_frame.grid(row = 0, column = 0)

middle_frame = tk.Frame(root)
middle_frame.grid(row=0, column=1, sticky="n")

right_frame = tk.Frame(root)
right_frame.grid(row=0, column=2, sticky = "n")

# Corner left of screen
save_button_frame = tk.Frame(left_frame)
save_button_frame.config(bg = '#545f66')
save_button_frame.grid(row=0, column=0, sticky="NW")

# Left screen frames
blue_team_frame = tk.Frame(left_frame, padx=50, pady=50, bg = "#00aeef", highlightbackground="black", highlightthickness=5)
blue_team_frame.grid(row=0, column=1)

blue_config_frame = tk.Frame(left_frame, padx=50, pady=20)
blue_config_frame.grid(row=1, column=1)

# Right screen frames
red_team_frame = tk.Frame(right_frame, padx=50, pady=50, bg="#ba014e", highlightbackground="black", highlightthickness=5)
red_team_frame.grid(row=0, column=0)

red_config_frame = tk.Frame(right_frame, padx=50, pady=20)
red_config_frame.grid(row=1, column=0)

# Image files/Resizing
photo_1 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_play_3923854.png")
photo_1_image = photo_1.subsample(20, 20)

photo_2 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_pause_2935827 (1).png")
photo_2_image = photo_2.subsample(23, 23)

photo_3 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_reset_2283376 (1).png")
photo_3_image = photo_3.subsample(20, 20)

photo_4 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_Save_9016 (1).png")
photo_4_image = photo_4.subsample(15, 15)

# Middle of the Screen
time_lb = tk.Label(middle_frame,text=format_time(root.current_time),font=("Rockwell",200))
time_lb.grid(row=0,column=0)

start_btn = tk.Button(middle_frame,text="Start",font=("Rockwell",50),command=start, image = photo_1_image, compound=RIGHT)
start_btn.grid(row=1,column=0, sticky="WE", pady=10, padx=30)

pause_btn = tk.Button(middle_frame,text="Pause",font=("Rockwell",50),command=pause, image = photo_2_image, compound = RIGHT)
pause_btn.grid(row=2,column=0, sticky="WE", pady=10, padx=30)

reset_btn = tk.Button(middle_frame,text="Reset",font=("Rockwell",50),command=reset, image = photo_3_image, compound = RIGHT)
reset_btn.grid(row=3,column=0, sticky="WE", pady=10, padx=30)

set_btn = tk.Button(middle_frame,text="Set",font=("Rockwell",50),command=set_time)
set_btn.grid(row=4,column=0,sticky="WE", pady=10, padx=30)

# Corner Left of the Screen
save_btn = tk.Button(save_button_frame, image = photo_4_image, padx=10, pady=10)
save_btn.grid(row=0, column=0)

load_btn = tk.Button(save_button_frame, text="Load", font=("Rockwell",12), padx=15, pady=20)
load_btn.grid(row=1, column=0)

# Left of the Screen
score_blue_lb = tk.Label(blue_team_frame, text="0", font=("Rockwell",450), bg="#00aeef", fg="white")
score_blue_lb.grid(row=0, column=0,sticky = "w")

blue_config_btn_1 = tk.Button(blue_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
blue_config_btn_1.grid(row=0, column=0)

blue_config_btn_2 = tk.Button(blue_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
blue_config_btn_2.grid(row=0, column=1)

blue_config_btn_3 = tk.Button(blue_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
blue_config_btn_3.grid(row=0, column=2)

blue_config_btn_4 = tk.Button(blue_config_frame, text="Reset Score", font=("Rockwell", 20), padx=10, pady=10)
blue_config_btn_4.grid(row=0, column=3)

# Right of the Screen
score_red_lb = tk.Label(red_team_frame, text="0", font =("Rockwell",450), bg="#ba014e", fg="white")
score_red_lb.grid(row=0, column=0, sticky="e")

red_config_btn_1 = tk.Button(red_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
red_config_btn_1.grid(row=0, column=0)

red_config_btn_2 = tk.Button(red_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
red_config_btn_2.grid(row=0, column=1)

red_config_btn_3 = tk.Button(red_config_frame, text="+1", font=("Rockwell", 20), padx=10, pady=10)
red_config_btn_3.grid(row=0, column=2)

red_config_btn_4 = tk.Button(red_config_frame, text="Reset Score", font=("Rockwell", 20), padx=10, pady=10)
red_config_btn_4.grid(row=0, column=3)


# Actual Scoreboard Numbers

# Global Variables

time_lb.after(1000,update())
root.mainloop()