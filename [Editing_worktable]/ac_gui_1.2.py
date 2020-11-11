import tkinter as tk

switch = True
temp = 18
mode = 1
fan = 'OFF'
swing = 'continously'
anti_b = 'OFF'
energy_s = 'OFF'

def visual(on_switch):
    global switch
    
    if on_switch == True:
        label['text'] = f'Temp: {temp}   \nFan: {fan}\nMode: {mode}    \nSwing: {swing}\nAnti Bacteria Mode: {anti_b}    \nEnergy Saving Mode: {energy_s}   '
        switch = False

    else:
        label['text'] = ""
        switch = True


def temp_up(on_switch):
    global temp

    if on_switch == False:
        if temp == 30:
            temp = temp

        else:
            temp += 1
        visual(True)

def temp_down(on_switch):
    global temp
    
    if on_switch == False:
        if temp == 18:
            temp = temp

        else:
            temp -= 1
        visual(True)

def mode_switch(on_switch):
    global mode

    if on_switch == False:
        if mode == 4:
            mode = 1

        else:
            mode += 1
        visual(True)


def fan_up(on_switch):
    global fan
    
    if on_switch == False:
        if fan == 3:
            fan = "Auto"
        
        elif fan == "Auto":
            fan = "OFF"

        elif fan == "OFF":
            fan = 1
            
        else:
            fan += 1
        visual(True)

def fan_down(on_switch):
    global fan
    
    if on_switch == False:
        if fan == "Auto":
            fan = 3

        elif fan == 1:
            fan = "OFF"

        elif fan == "OFF":
            fan = fan

        else:
            fan -= 1
        visual(True)

def ab_switch(on_switch):
    global anti_b

    if on_switch == False:
        if anti_b == "OFF":
            anti_b = "ON"

        else:
            anti_b = "OFF"
        visual(True)


def saving_switch(on_switch):
    global energy_s

    if on_switch == False:
        if energy_s == "OFF":
            energy_s = "ON"

        else:
            energy_s = "OFF"
        visual(True)


def swing_switch(on_switch):
    global swing

    if on_switch == False:

        if  swing == "Up":
            swing  = "Mid"

        elif swing == "Mid":
             swing  = "Down"

        elif swing == "Down":
             swing  = "Continously"

        else:
              swing  = "Up"
        visual(True)
        

root = tk.Tk()


canvas = tk.Canvas(root, height= 500, width=300, bg="#F4F4F2")
canvas.pack()


top_frame = tk.Frame(root, bg='#E8E8E8')
top_frame.place(relx= 0.5, rely=0.05, relwidth=0.8, relheight=0.3, anchor="n")


low_frame = tk.Canvas(root, bg='#F4F4F2')
low_frame.place(relx= 0.5, rely=0.35, relwidth=0.8, relheight=0.7, anchor='n')


on_button = tk.Button(low_frame, text="I O", bg="#C4C4C4", command=lambda: visual(switch))
on_button.place(relx=0.625, rely=0.4,relheight=0.075, relwidth=0.25)


temp_up_button = tk.Button(low_frame, text="Temp Up", bg="#C4C4C4", command=lambda :temp_up(switch))
temp_up_button.place(relx= 0.2, rely = 0.1, relheight= 0.08, relwidth=0.1)


temp_down_button = tk.Button(low_frame, text="Temp Down", bg="#C4C4C4", command=lambda :temp_down(switch))
temp_down_button.place(relx=0.2, rely = 0.2, relheight = 0.08, relwidth=0.1)


mode_button = tk.Button(low_frame, text="MODE", bg="#C4C4C4", command=lambda :mode_switch(switch))
mode_button.place(relx = 0.175, rely = 0.4, relheight=0.075, relwidth=0.25)

fan_up_button = tk.Button(low_frame, text="Fan Up", bg="#C4C4C4", command=lambda :fan_up(switch))
fan_up_button.place(relx= 0.7, rely = 0.1, relheight= 0.08, relwidth=0.1)

fan_down_button = tk.Button(low_frame, text="Fan Down", bg="#C4C4C4", command=lambda :fan_down(switch))
fan_down_button.place(relx=0.7, rely = 0.2, relheight = 0.08, relwidth=0.1)


ab_mode_button = tk.Button(low_frame, text="ANTI-B", bg="#C4C4C4", command=lambda :ab_switch(switch))
ab_mode_button.place(relx=0.175, rely= 0.55, relheight=0.075, relwidth=0.25)


saving_mode_button = tk.Button(low_frame, text="SAVING", bg="#C4C4C4", command= lambda:saving_switch(switch))
saving_mode_button.place(relx=0.625, rely=0.55, relheight=0.075, relwidth=0.25)


swing_button = tk.Button(low_frame, text="SWING", bg="#C4C4C4", command= lambda: swing_switch(switch))
swing_button.place(relx=0.5, rely= 0.7, relheight=0.075, relwidth=0.25, anchor='n')


label = tk.Label(top_frame, bg='#E8E8E8')
label.place(relwidth=1, relheight=1)


root.mainloop()
