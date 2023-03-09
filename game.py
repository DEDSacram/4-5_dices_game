# Python program to create a table
try:
    from tkinter import * 
    from tkinter import messagebox  
    from tkinter.simpledialog import askstring
except ImportError:
    from Tkinter import *
    from Tkinter import messagebox
    from Tkinter.simpledialog import askstring

root = Tk()

height = 5
width = 11


file1 = open('multipliers.txt', 'r')
Lines = file1.readlines()
  
count = 0

nums = []

players = []

results = []

def on_click(group,end,scores):
    # messagebox.showinfo("showinfo", "Information")
    name = askstring('Rozsah', 'Kolik jsi hodil?')
    for i in range(len(group)):
        #player
        result = 0
        for j in range(len(group[i])):
            valuein = group[i][j].get()
            if int(scores[j][0]) < int(name):
                continue
            if valuein == "":
                continue
            result += round(int(valuein)*float(scores[j][1]))
            # print(valuein * float(scores[j][1]))
        set_text(end[i],"{}".format(result))

def set_text(en,text):
    en.delete(0,END)
    en.insert(0,text)
    return

def clean(group,end):
        for i in range(len(group)):
            for j in range(len(group[i])):
                set_text(group[i][j], "")
                set_text(end[i], "")



# Strips the newline character
for line in Lines:
    nums.append(line.strip().split(':'))
    Label(root, text="{} : {}X".format(nums[count][0], nums[count][1])).grid(row=0, column=count+1)
    count += 1



for i in range(height): #Rows
    Label(root, text="Player {}".format(i)).grid(row=i+2, column=0)
    player = []
    for j in range(width): #Columns
        b = Entry(root, text="")
        player.append(b)
        b.grid(row=i+2, column=j+1)
    players.append(player)


Label(root, text="Vysledek").grid(row=0, column=width+1)
for i in range(height):
    cost_var = DoubleVar()
    # state='readonly'
    b = Entry(root,textvariable=cost_var)
    results.append(b)
    b.grid(row=i+2, column=width+1)


# button = Button(root, text='Stop', width=25, command=root.destroy)
# # button.pack()


submitbtn= Button(root, text="Submit", command=lambda: on_click(players,results,nums))
submitbtn.grid(row=0,column=0)

resetbtn= Button(root, text="Reset", command=lambda: clean(players,results))
resetbtn.grid(row=height+2,column=0)

mainloop()