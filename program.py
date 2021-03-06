import tkinter as tk
from tkinter.constants import ANCHOR, BOTH, CENTER, LEFT, N, RIGHT, TOP, TRUE
import time
pygame.mixer.init()

def format_time(time):
    # This function formats the time into minutes and seconds
    minutes = time // 60
    seconds = time % 60
    return f"{minutes}:{seconds}"

def update():
    # This function updates the time by subtracting one second from the current time, 
    # when the timer hits zero, a sound is played and the timer stops then resets
    if root.running:
        root.current_time -= 1
    if root.current_time <=0:
        root.running=False
        pygame.mixer.music.load("/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/FIA2 Resources/sound effects/Wrong Buzzer Sound Effect.mp3")
        pygame.mixer.music.play(1)
        pygame.mixer.music.stop
        reset()
    time_lb.config(text=format_time(root.current_time))
    time_lb.after(1000,update)
     
def start():
    # This function starts the timer as well as activate the three second countdown
    pygame.mixer.music.load("/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/FIA2 Resources/sound effects/Free 3 second intro countdown with tunnel effect sound and AI robot voice.mp3")
    pygame.mixer.music.play(0)
    time.sleep(3)
    root.running = True


def pause():
    # This function pauses the timer
    root.running = False

def reset():
    # This function resets the timer to the user input seconds value
    root.running = False
    root.current_time = root.time

def set_time():
    # This function opens a new window and allows the user to input the desired amount of seconds. 
    # It makes the current time variable the desired amount of seconds that the user put in.
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

def SaveValues():
    # This function gathers all the program values, and puts them into a .txt file for later retrieval
    with open("string.txt","w") as data_file:
        data_file.write(blue_team_ent_str.get() + "\n")
        data_file.write(red_team_ent_str.get() + "\n")
        data_file.write(str(root.time) + "\n")
        data_file.write(str(root.set_score_1a) + "\n")
        data_file.write(str(root.set_score_2a) + "\n")
        data_file.write(str(root.set_score_3a) + "\n")
        data_file.write(str(root.set_score_1b) + "\n")
        data_file.write(str(root.set_score_2b) + "\n")
        data_file.write(str(root.set_score_3b) + "\n")
        data_file.write(score_blue_lb_str.get() + "\n")
        data_file.write(score_red_lb_str.get())

def OpenValues():
    # This function reads the .txt file, and reassigns all the values to the program.
    with open("string.txt", "r") as data_file:
        all_lines = data_file.readlines()
        line_to_read_1 = all_lines[0]
        line_to_read_2 = all_lines[1]
        line_to_read_3 = all_lines[2]
        line_to_read_4 = all_lines[3]
        line_to_read_5 = all_lines[4]
        line_to_read_6 = all_lines[5]
        line_to_read_7 = all_lines[6]
        line_to_read_8 = all_lines[7]
        line_to_read_9 = all_lines[8]
        line_to_read_10 = all_lines[9]
        line_to_read_11 = all_lines[10]

        blue_team_ent_str.set(line_to_read_1)
        red_team_ent_str.set(line_to_read_2)

        root.time = int(line_to_read_3)
        root.current_time = root.time

        root.set_score_1a = int(line_to_read_4)
        root.current_score_1a = root.set_score_1a
        blue_config_btn_1.config(text=(root.current_score_1a))

        root.set_score_2a = int(line_to_read_5)
        root.current_score_2a = root.set_score_2a
        blue_config_btn_2.config(text=(root.current_score_2a))

        root.set_score_3a = int(line_to_read_6)
        root.current_score_3a = root.set_score_3a
        blue_config_btn_3.config(text=(root.current_score_3a))

        root.set_score_1b = int(line_to_read_7)
        root.current_score_1b = root.set_score_1b
        red_config_btn_1.config(text=(root.current_score_1b))

        root.set_score_2b = int(line_to_read_8)
        root.current_score_2b = root.set_score_2b
        red_config_btn_2.config(text=(root.current_score_2b))

        root.set_score_3b = int(line_to_read_9)
        root.current_score_3b = root.set_score_3b
        red_config_btn_3.config(text=(root.current_score_3b))
        
        root.current_final_score_blue = int(line_to_read_10)
        root.current_final_score_red = int(line_to_read_11)
        score_blue_lb_str.set(root.current_final_score_blue)
        score_red_lb_str.set(root.current_final_score_red)


def apply_1a():
    # This function adds or subtracts the score value depending on what the user put in
    root.sum_blue = root.current_score_1a + root.current_final_score_blue
    score_blue_lb_str.set(root.sum_blue)
    root.current_final_score_blue = root.sum_blue

def apply_2a():
    root.sum_blue = root.current_score_2a + root.current_final_score_blue
    score_blue_lb_str.set(root.sum_blue)
    root.current_final_score_blue = root.sum_blue

def apply_3a():
    root.sum_blue = root.current_score_3a + root.current_final_score_blue
    score_blue_lb_str.set(root.sum_blue)
    root.current_final_score_blue = root.sum_blue

def reset_blue():
    # This function puts the score back to 0
    root.current_final_score_blue = 0
    score_blue_lb_str.set(root.current_final_score_blue)

def reset_red():
    root.current_final_score_red = 0
    score_red_lb_str.set(root.current_final_score_red)


def apply_1b():
    root.sum_red = root.current_score_1b + root.current_final_score_red
    score_red_lb_str.set(root.sum_red)
    root.current_final_score_red = root.sum_red

def apply_2b():
    root.sum_red = root.current_score_2b + root.current_final_score_red
    score_red_lb_str.set(root.sum_red)
    root.current_final_score_red = root.sum_red

def apply_3b():
    root.sum_red = root.current_score_3b + root.current_final_score_red
    score_red_lb_str.set(root.sum_red)
    root.current_final_score_red = root.sum_red


def set_score_1a():
    # This function opens a new window and allows the user to input a value to add or subtract from the score. 
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_1a = tk.StringVar(top, root.set_score_1a)

    def ok():
        root.set_score_1a = int(score_1a.get())
        root.current_score_1a = root.set_score_1a
        blue_config_btn_1.config(text=(root.current_score_1a))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_1a)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)

def set_score_2a():
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_2a = tk.StringVar(top, root.set_score_2a)

    def ok():
        root.set_score_2a = int(score_2a.get())
        root.current_score_2a = root.set_score_2a
        blue_config_btn_2.config(text=(root.current_score_2a))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_2a)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)

def set_score_3a():
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_3a = tk.StringVar(top, root.set_score_3a)

    def ok():
        root.set_score_3a = int(score_3a.get())
        root.current_score_3a = root.set_score_3a
        blue_config_btn_3.config(text=(root.current_score_3a))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_3a)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)


def set_score_1b():
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_1b = tk.StringVar(top, root.set_score_1b)

    def ok():
        root.set_score_1b = int(score_1b.get())
        root.current_score_1b = root.set_score_1b
        red_config_btn_1.config(text=(root.current_score_1b))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_1b)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)

def set_score_2b():
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_2b = tk.StringVar(top, root.set_score_2b)

    def ok():
        root.set_score_2b = int(score_2b.get())
        root.current_score_2b = root.set_score_2b
        red_config_btn_2.config(text=(root.current_score_2b))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_2b)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)

def set_score_3b():
    top = tk.Toplevel()
    top.title("Set Score")
    top.geometry = ("200x150")

    score_3b = tk.StringVar(top, root.set_score_3b)

    def ok():
        root.set_score_3b = int(score_3b.get())
        root.current_score_3b = root.set_score_3b
        red_config_btn_3.config(text=(root.current_score_3b))
        top.destroy()
    tk.Label(top,text="Enter Score").grid(row=0,column=0,columnspan=2)

    new_score_ent = tk.Entry(top, textvariable=score_3b)
    new_score_ent.grid(row=1, column=0, columnspan = 2)

    ok_btn = tk.Button(top, text="Ok", command=ok)
    ok_btn.grid(row=2, column=0)

    cancel_btn = tk.Button(top, text = "Cancel", command=top.destroy)
    cancel_btn.grid(row=2, column=1)


# --- Main Program ---
# Creating Tkinter window
root = tk.Tk()
root.title("Scoreboard Program")
root.geometry("1920x1080")
root.resizable = (False,False)

# Defining time and score values for the set_time() and set_score() functions to work

root.time = 330
root.current_time = root.time
root.running = False

root.sum_blue = 0
root.current_final_score_blue = root.sum_blue

root.sum_red = 0
root.current_final_score_red = root.sum_red

root.set_score_1a = 0
root.current_score_1a = root.set_score_1a
root.running = False

root.set_score_2a = 0
root.current_score_2a = root.set_score_2a
root.running = False

root.set_score_3a = 0
root.current_score_3a = root.set_score_3a
root.running = False

root.set_score_1b = 0
root.current_score_1b = root.set_score_1b
root.running = False

root.set_score_2b = 0
root.current_score_2b = root.set_score_2b
root.running = False

root.set_score_3b = 0
root.cuurent_score_3b = root.set_score_3b
root.running = False

root.running = False

# Creating elements to showcase in Tkinter window
# Frames
left_frame = tk.Frame(root)
left_frame.grid(row = 0, column = 0)

middle_frame = tk.Frame(root)
middle_frame.grid(row=0, column=1, sticky="n")

right_frame = tk.Frame(root)
right_frame.grid(row=0, column=2, sticky = "n")

# Top left of screen
save_button_frame = tk.Frame(left_frame)
save_button_frame.config(bg = '#545f66')
save_button_frame.grid(row=0, column=0, sticky="NW")

# Left screen frames
blue_team_frame = tk.Frame(left_frame, padx=50, pady=50, bg = "#00aeef", highlightbackground="black", highlightthickness=5)
blue_team_frame.grid(row=0, column=1)

blue_config_name_frame = tk.Frame(left_frame, padx=50, pady=20)
blue_config_name_frame.grid(row=1, column=1)

blue_config_frame = tk.Frame(left_frame, padx=50, pady=20)
blue_config_frame.grid(row=2, column=1)

# Right screen frames
red_team_frame = tk.Frame(right_frame, padx=50, pady=50, bg="#ba014e", highlightbackground="black", highlightthickness=5)
red_team_frame.grid(row=0, column=0)

red_config_name_frame = tk.Frame(right_frame, padx=50, pady=20)
red_config_name_frame.grid(row=1, column=0)

red_config_frame = tk.Frame(right_frame, padx=50, pady=20)
red_config_frame.grid(row=2, column=0)

# Opening image files for buttons and then resizing them
photo_1 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_play_3923854.png")
photo_1_image = photo_1.subsample(20, 20)

photo_2 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_pause_2935827 (1).png")
photo_2_image = photo_2.subsample(23, 23)

photo_3 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_reset_2283376 (1).png")
photo_3_image = photo_3.subsample(20, 20)

photo_4 = tk.PhotoImage(file = "/Users/hunterbarrett/Desktop/2021/Digital Solutions/Term 2 Work/mock ups gents/icons/noun_Save_9016 (1).png")
photo_4_image = photo_4.subsample(15, 15)

# Placing Tkinter elements into different frames
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

# Top left of the screen
save_btn = tk.Button(save_button_frame, image = photo_4_image, padx=10, pady=10, command=SaveValues)
save_btn.grid(row=0, column=0)

load_btn = tk.Button(save_button_frame, text="Load", font=("Rockwell",12), padx=15, pady=20, command=OpenValues)
load_btn.grid(row=1, column=0)

# Left of the Screen
score_blue_lb_str = tk.StringVar(blue_team_frame, value='0')
score_blue_lb = tk.Label(blue_team_frame, textvariable= score_blue_lb_str, height=1, width=2, font=("Rockwell",300), bg="#00aeef", fg="white")
score_blue_lb.grid(row=0, column=0,sticky = "w")

blue_team_ent_str = tk.StringVar(blue_config_name_frame, value='Enter Team Name')
blue_team_name_ent = tk.Entry(blue_config_name_frame, font=("Rockwell", 20), bg= "#00aeef", fg="white", justify = CENTER, textvariable= blue_team_ent_str)
blue_team_name_ent.grid(row=0, column=2, sticky="n")

blue_config_btn_1 = tk.Button(blue_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command= set_score_1a)
blue_config_btn_1.grid(row=2, column=0)

blue_config_btn_2 = tk.Button(blue_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command= set_score_2a)
blue_config_btn_2.grid(row=2, column=1)

blue_config_btn_3 = tk.Button(blue_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command = set_score_3a)
blue_config_btn_3.grid(row=2, column=2)

blue_config_btn_4 = tk.Button(blue_config_frame, text="Reset Score", font=("Rockwell", 20), padx=10, pady=10, command = reset_blue)
blue_config_btn_4.grid(row=2, column=3)

blue_config_add_btn_1 = tk.Button(blue_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command= apply_1a)
blue_config_add_btn_1.grid(row=3, column=0)

blue_config_add_btn_2 = tk.Button(blue_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command = apply_2a)
blue_config_add_btn_2.grid(row=3, column=1)

blue_config_add_btn_3 = tk.Button(blue_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command = apply_3a)
blue_config_add_btn_3.grid(row=3, column=2)

# Right of the Screen
score_red_lb_str = tk.StringVar(red_team_frame, value='0')
score_red_lb = tk.Label(red_team_frame, textvariable=score_red_lb_str, height=1, width=2, font =("Rockwell",300), bg="#ba014e", fg="white")
score_red_lb.grid(row=0, column=0, sticky="e")

red_team_ent_str = tk.StringVar(red_config_name_frame, value='Enter Team Name')
red_team_name_ent = tk.Entry(red_config_name_frame, text="Enter Name", font=("Rockwell", 20), bg= "#ba014e", fg="white", justify = CENTER, textvariable= red_team_ent_str)
red_team_name_ent.grid(row=0, column=2, sticky="n")

red_config_btn_1 = tk.Button(red_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command = set_score_1b)
red_config_btn_1.grid(row=1, column=0)

red_config_btn_2 = tk.Button(red_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command = set_score_2b)
red_config_btn_2.grid(row=1, column=1)

red_config_btn_3 = tk.Button(red_config_frame, text="0", font=("Rockwell", 20), padx=10, pady=10, command = set_score_3b)
red_config_btn_3.grid(row=1, column=2)

red_config_btn_4 = tk.Button(red_config_frame, text="Reset Score", font=("Rockwell", 20), padx=10, pady=10, command = reset_red)
red_config_btn_4.grid(row=1, column=3)

red_config_add_btn_1 = tk.Button(red_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command = apply_1b)
red_config_add_btn_1.grid(row=2, column=0)

red_config_add_btn_2 = tk.Button(red_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command = apply_2b)
red_config_add_btn_2.grid(row=2, column=1)

red_config_add_btn_3 = tk.Button(red_config_frame, text="Add", font=("Rockwell", 15), padx=5, pady=5, command = apply_3b)
red_config_add_btn_3.grid(row=2, column=2)

# Global variables?

time_lb.after(1000,update())
root.mainloop()