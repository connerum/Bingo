import time
import random
import tkinter as tk
from tkinter import ttk


# root window
root = tk.Tk()
root.iconbitmap('226609.ico')
root.title('Bingo!')

# get the screen dimension
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# set window dimensions
window_width = int(screen_width * 0.85)
window_height = int(screen_height * 0.80)

# find the center point
center_x = int(screen_width/2 - window_width / 2)
center_y = int(screen_height/2 - window_height / 2)

# set the position of the window to the center of the screen
root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(2, weight=1)
root.columnconfigure(3, weight=1)
root.columnconfigure(4, weight=1)
root.columnconfigure(5, weight=2)

first = ttk.Label(root, text="B", font=('Helvetica', 20, 'bold')).grid(column=0, row=0, sticky=tk.N, padx=1, pady=1)
second = ttk.Label(root, text="I", font=('Helvetica', 20, 'bold')).grid(column=1, row=0, sticky=tk.N, padx=1, pady=1)
third = ttk.Label(root, text="N", font=('Helvetica', 20, 'bold')).grid(column=2, row=0, sticky=tk.N, padx=1, pady=1)
fourth = ttk.Label(root, text="G", font=('Helvetica', 20, 'bold')).grid(column=3, row=0, sticky=tk.N, padx=1, pady=1)
fifth = ttk.Label(root, text="O", font=('Helvetica', 20, 'bold')).grid(column=4, row=0, sticky=tk.N, padx=1, pady=1)
sixth = ttk.Label(root, text="Most Recently Called: ", font=('Helvetica', 20, 'bold')).grid(column=5, row=3, sticky=tk.N, padx=1, pady=1)


chclst = ttk.Frame(root)
chclst2 = ttk.Frame(root)
chclst.grid(column=5, row=4)
chclst2.grid(column=5, row=5)


frst = ttk.Label(chclst, text=" ", font=('Helvetica', 16, 'bold'))
frst.pack(side='left', padx=15, pady=1)
frrow = ttk.Label(chclst2, text=" ", font=('Helvetica', 14))
frrow.pack(side='left', padx=15, pady=1)

def callback():
    choicestr = caller()
    if choicestr == 0:
        ans = input('Would you like to start a new game? (Y or N): ')
        if ans == 'Y':
            for b in B:
                b.config(background='')
            for i in I:
                i.config(background='')
            for n in N:
                n.config(background='')
            for g in G:
                g.config(background='')
            for o in O:
                o.config(background='')
    elif choicestr <= 15:
        print('B' + ' ' + str(choicestr))
        frst.config(text='B')
        frrow.config(text=choicestr)
    elif choicestr <= 30:
        print('I' + ' ' + str(choicestr))
        frst.config(text='I')
        frrow.config(text=choicestr)
    elif choicestr <= 45:
        print('N' + ' ' + str(choicestr))
        frst.config(text='N')
        frrow.config(text=choicestr)
    elif choicestr <= 60:
        print('G' + ' ' + str(choicestr))
        frst.config(text='G')
        frrow.config(text=choicestr)
    elif choicestr <= 75:
        print('O' + ' ' + str(choicestr))
        frst.config(text='O')
        frrow.config(text=choicestr)

nextbtn = ttk.Button(
   root,
   text="Next Ball",
   command=callback
).grid(column=5, row=8, ipadx=10, ipady=10)

# B labels
b1 = ttk.Label(root, text="1", font=('Helvetica', 15))
b1.grid(column=0, row=1, padx=1, pady=8)
b2 = ttk.Label(root, text="2", font=('Helvetica', 15))
b2.grid(column=0, row=2, padx=1, pady=8)
b3 = ttk.Label(root, text="3", font=('Helvetica', 15))
b3.grid(column=0, row=3, padx=1, pady=8)
b4 = ttk.Label(root, text="4", font=('Helvetica', 15))
b4.grid(column=0, row=4, padx=1, pady=8)
b5 = ttk.Label(root, text="5", font=('Helvetica', 15))
b5.grid(column=0, row=5, padx=1, pady=8)
b6 = ttk.Label(root, text="6", font=('Helvetica', 15))
b6.grid(column=0, row=6, padx=1, pady=8)
b7 = ttk.Label(root, text="7", font=('Helvetica', 15))
b7.grid(column=0, row=7, padx=1, pady=8)
b8 = ttk.Label(root, text="8", font=('Helvetica', 15))
b8.grid(column=0, row=8, padx=1, pady=8)
b9 = ttk.Label(root, text="9", font=('Helvetica', 15))
b9.grid(column=0, row=9, padx=1, pady=8)
b10 = ttk.Label(root, text="10", font=('Helvetica', 15))
b10.grid(column=0, row=10, padx=1, pady=8)
b11 = ttk.Label(root, text="11", font=('Helvetica', 15))
b11.grid(column=0, row=11, padx=1, pady=8)
b12 = ttk.Label(root, text="12", font=('Helvetica', 15))
b12.grid(column=0, row=12, padx=1, pady=8)
b13 = ttk.Label(root, text="13", font=('Helvetica', 15))
b13.grid(column=0, row=13, padx=1, pady=8)
b14 = ttk.Label(root, text="14", font=('Helvetica', 15))
b14.grid(column=0, row=14, padx=1, pady=8)
b15 = ttk.Label(root, text="15", font=('Helvetica', 15))
b15.grid(column=0, row=15, padx=1, pady=8)

# I labels
i1 = ttk.Label(root, text="16", font=('Helvetica', 15))
i1.grid(column=1, row=1, padx=1, pady=8)
i2 = ttk.Label(root, text="17", font=('Helvetica', 15))
i2.grid(column=1, row=2, padx=1, pady=8)
i3 = ttk.Label(root, text="18", font=('Helvetica', 15))
i3.grid(column=1, row=3, padx=1, pady=8)
i4 = ttk.Label(root, text="19", font=('Helvetica', 15))
i4.grid(column=1, row=4, padx=1, pady=8)
i5 = ttk.Label(root, text="20", font=('Helvetica', 15))
i5.grid(column=1, row=5, padx=1, pady=8)
i6 = ttk.Label(root, text="21", font=('Helvetica', 15))
i6.grid(column=1, row=6, padx=1, pady=8)
i7 = ttk.Label(root, text="22", font=('Helvetica', 15))
i7.grid(column=1, row=7, padx=1, pady=8)
i8 = ttk.Label(root, text="23", font=('Helvetica', 15))
i8.grid(column=1, row=8, padx=1, pady=8)
i9 = ttk.Label(root, text="24", font=('Helvetica', 15))
i9.grid(column=1, row=9, padx=1, pady=8)
i10 = ttk.Label(root, text="25", font=('Helvetica', 15))
i10.grid(column=1, row=10, padx=1, pady=8)
i11 = ttk.Label(root, text="26", font=('Helvetica', 15))
i11.grid(column=1, row=11, padx=1, pady=8)
i12 = ttk.Label(root, text="27", font=('Helvetica', 15))
i12.grid(column=1, row=12, padx=1, pady=8)
i13 = ttk.Label(root, text="28", font=('Helvetica', 15))
i13.grid(column=1, row=13, padx=1, pady=8)
i14 = ttk.Label(root, text="29", font=('Helvetica', 15))
i14.grid(column=1, row=14, padx=1, pady=8)
i15 = ttk.Label(root, text="30", font=('Helvetica', 15))
i15.grid(column=1, row=15, padx=1, pady=8)

# N labels
n1 = ttk.Label(root, text="31", font=('Helvetica', 15))
n1.grid(column=2, row=1, padx=1, pady=8)
n2 = ttk.Label(root, text="32", font=('Helvetica', 15))
n2.grid(column=2, row=2, padx=1, pady=8)
n3 = ttk.Label(root, text="33", font=('Helvetica', 15))
n3.grid(column=2, row=3, padx=1, pady=8)
n4 = ttk.Label(root, text="34", font=('Helvetica', 15))
n4.grid(column=2, row=4, padx=1, pady=8)
n5 = ttk.Label(root, text="35", font=('Helvetica', 15))
n5.grid(column=2, row=5, padx=1, pady=8)
n6 = ttk.Label(root, text="36", font=('Helvetica', 15))
n6.grid(column=2, row=6, padx=1, pady=8)
n7 = ttk.Label(root, text="37", font=('Helvetica', 15))
n7.grid(column=2, row=7, padx=1, pady=8)
n8 = ttk.Label(root, text="38", font=('Helvetica', 15))
n8.grid(column=2, row=8, padx=1, pady=8)
n9 = ttk.Label(root, text="39", font=('Helvetica', 15))
n9.grid(column=2, row=9, padx=1, pady=8)
n10 = ttk.Label(root, text="40", font=('Helvetica', 15))
n10.grid(column=2, row=10, padx=1, pady=8)
n11 = ttk.Label(root, text="41", font=('Helvetica', 15))
n11.grid(column=2, row=11, padx=1, pady=8)
n12 = ttk.Label(root, text="42", font=('Helvetica', 15))
n12.grid(column=2, row=12, padx=1, pady=8)
n13 = ttk.Label(root, text="43", font=('Helvetica', 15))
n13.grid(column=2, row=13, padx=1, pady=8)
n14 = ttk.Label(root, text="44", font=('Helvetica', 15))
n14.grid(column=2, row=14, padx=1, pady=8)
n15 = ttk.Label(root, text="45", font=('Helvetica', 15))
n15.grid(column=2, row=15, padx=1, pady=8)

# G labels
g1 = ttk.Label(root, text="46", font=('Helvetica', 15))
g1.grid(column=3, row=1, padx=1, pady=8)
g2 = ttk.Label(root, text="47", font=('Helvetica', 15))
g2.grid(column=3, row=2, padx=1, pady=8)
g3 = ttk.Label(root, text="48", font=('Helvetica', 15))
g3.grid(column=3, row=3, padx=1, pady=8)
g4 = ttk.Label(root, text="49", font=('Helvetica', 15))
g4.grid(column=3, row=4, padx=1, pady=8)
g5 = ttk.Label(root, text="50", font=('Helvetica', 15))
g5.grid(column=3, row=5, padx=1, pady=8)
g6 = ttk.Label(root, text="51", font=('Helvetica', 15))
g6.grid(column=3, row=6, padx=1, pady=8)
g7 = ttk.Label(root, text="52", font=('Helvetica', 15))
g7.grid(column=3, row=7, padx=1, pady=8)
g8 = ttk.Label(root, text="53", font=('Helvetica', 15))
g8.grid(column=3, row=8, padx=1, pady=8)
g9 = ttk.Label(root, text="54", font=('Helvetica', 15))
g9.grid(column=3, row=9, padx=1, pady=8)
g10 = ttk.Label(root, text="55", font=('Helvetica', 15))
g10.grid(column=3, row=10, padx=1, pady=8)
g11 = ttk.Label(root, text="56", font=('Helvetica', 15))
g11.grid(column=3, row=11, padx=1, pady=8)
g12 = ttk.Label(root, text="57", font=('Helvetica', 15))
g12.grid(column=3, row=12, padx=1, pady=8)
g13 = ttk.Label(root, text="58", font=('Helvetica', 15))
g13.grid(column=3, row=13, padx=1, pady=8)
g14 = ttk.Label(root, text="59", font=('Helvetica', 15))
g14.grid(column=3, row=14, padx=1, pady=8)
g15 = ttk.Label(root, text="60", font=('Helvetica', 15))
g15.grid(column=3, row=15, padx=1, pady=8)

# O labels
o1 = ttk.Label(root, text="61", font=('Helvetica', 15))
o1.grid(column=4, row=1, padx=1, pady=8)
o2 = ttk.Label(root, text="62", font=('Helvetica', 15))
o2.grid(column=4, row=2, padx=1, pady=8)
o3 = ttk.Label(root, text="63", font=('Helvetica', 15))
o3.grid(column=4, row=3, padx=1, pady=8)
o4 = ttk.Label(root, text="64", font=('Helvetica', 15))
o4.grid(column=4, row=4, padx=1, pady=8)
o5 = ttk.Label(root, text="65", font=('Helvetica', 15))
o5.grid(column=4, row=5, padx=1, pady=8)
o6 = ttk.Label(root, text="66", font=('Helvetica', 15))
o6.grid(column=4, row=6, padx=1, pady=8)
o7 = ttk.Label(root, text="67", font=('Helvetica', 15))
o7.grid(column=4, row=7, padx=1, pady=8)
o8 = ttk.Label(root, text="68", font=('Helvetica', 15))
o8.grid(column=4, row=8, padx=1, pady=8)
o9 = ttk.Label(root, text="69", font=('Helvetica', 15))
o9.grid(column=4, row=9, padx=1, pady=8)
o10 = ttk.Label(root, text="70", font=('Helvetica', 15))
o10.grid(column=4, row=10, padx=1, pady=8)
o11 = ttk.Label(root, text="71", font=('Helvetica', 15))
o11.grid(column=4, row=11, padx=1, pady=8)
o12 = ttk.Label(root, text="72", font=('Helvetica', 15))
o12.grid(column=4, row=12, padx=1, pady=8)
o13 = ttk.Label(root, text="73", font=('Helvetica', 15))
o13.grid(column=4, row=13, padx=1, pady=8)
o14 = ttk.Label(root, text="74", font=('Helvetica', 15))
o14.grid(column=4, row=14, padx=1, pady=8)
o15 = ttk.Label(root, text="75", font=('Helvetica', 15))
o15.grid(column=4, row=15, padx=1, pady=8)

B = [b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15]
I = [i1, i2, i3, i4, i5, i6, i7, i8, i9, i10, i11, i12, i13, i14, i15]
N = [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12, n13, n14, n15]
G = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15]
O = [o1, o2, o3, o4, o5, o6, o7, o8, o9, o10, o11, o12, o13, o14, o15]
total = B + I + N + G + O


def caller():
    lstb = total
    if len(lstb) > 0:
        choice = random.choice(lstb)
        lstb.remove(choice)
        choice.config(background='red')
        choicestr = int(choice["text"])
        return choicestr
    else:
        return 0


root.mainloop()
