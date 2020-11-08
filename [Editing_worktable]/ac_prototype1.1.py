from os import system

# Program membuat remote ac dengan fiturnya

# Kamus

# Algoritma

switch = True
temp = 18
mode = 1
fan = 2
swing = ''

def clear():
    system("cls")

def visual():

    if switch == True:

        print(f'Temp: {temp}   '  + f'Fan: {fan}')
        print(f'Mode: {mode}    ' + f'Swing: {swing}')

    else:
        print("OFF")


def remote():
    global switch, temp, mode, fan, swing

    clear()
    visual()

    print("""
    List of Instructions:
    1. On
    2. Off
    3. Temp Up
    4. Temp Down
    5. Mode
    6. Fan
    7. Swing On
    8. Swing Off

    """
    )

    remote_input = int(input("Your instructions: "))

    while remote_input not in range(1, 9):
        print("Your instructions is not in the list.")
        remote_input = int(input("Your instrucions: "))

    if remote_input == 1:
        
        switch = True

    elif remote_input == 2:
        
        switch = False

    elif remote_input == 3:
        
        if temp == 30:
            temp = temp

        else:
            temp += 1

    elif remote_input == 4:
        
        if temp == 18:
            temp = temp

        else:
            temp -= 1

    elif remote_input == 5:
        
        if mode == 4:
            mode = 1

        else:
            mode += 1

    elif remote_input == 6:
        
        if fan == 3:
            fan = 1

        else:
            fan += 1

    elif remote_input == 7:
        
        swing = "Auto"

    elif remote_input == 8:
        
        swing = "Off"


switch = True
while switch == True:
    remote()

else:
    visual()
