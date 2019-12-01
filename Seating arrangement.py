import tkinter
import random as r

##_12B = ["Adeeb", "Ali", "Anjelia", "Annnn", "Antoney", "Areeb", "Asheun", "Harshil", "Jadin", "Jo yel", "June ayta",
##        "Matheus", "Ni gil", "Reykhu nath", "Rithe ima", "Rawneth", "Roo jika", "Sah hell", "Sahil", "Saakshi",
##        "Samir", "Samrin", "Shwetha", "Uma"]

bois = ["Adeeb", "Ali", "Antoney", "Areeb", "Asheun", "Harshil", "Jadin", "Jo yel", "Matheus", "Ni gil",
        "Reykhu nath", "Rawneth", "Sah hell", "Sahil", "Samir"]
gurls = ["Anjelia", "Annnn", "June ayta", "Rithe ima", "Roo jika", "Saakshi", "Samrin", "Shwetha", "Uma"]


def generate_arrangement():
    seats = []
    lads = []
    r.shuffle(gurls)
    r.shuffle(bois)
    b1 = []
    b1.extend([bois[0], bois[1], bois[2], bois[3], bois[4]])
    b2 = []
    b2.extend([bois[5], bois[6], bois[7], bois[8], bois[9]])
    b3 = []
    b3.extend([bois[10], bois[11], bois[12], bois[13], bois[14]])
    g1 = []
    g1.extend([gurls[0], gurls[1], gurls[2]])
    g2 = []
    g2.extend([gurls[3], gurls[4], gurls[5]])
    g3 = []
    g3.extend([gurls[6], gurls[7], gurls[8]])
    c1 = b1 + g1
    c2 = b2 + g2
    c3 = b3 + g3
    r.shuffle(c1)
    r.shuffle(c2)
    r.shuffle(c3)
    lads.extend(c1+c2+c3)

    for seat in seats:
        seat.destroy()
        del seat

    c2multiplier = 3
    number = 200
    z = 0
    for lad in lads[:8]:
        if c2multiplier > 4:
            c2multiplier = 3
            number += 150
            z = 0
        seat = tkinter.Button(master, text=f"{lad}", relief="solid", font=("Arial", 20, "bold"), bg="red", cursor="star", width=10)
        seats.append(seat)
        seat.place(x=c2multiplier*1920/7 - z, y=number)
        c2multiplier += 1
        z += 60

    c1multiplier = 1
    number = 200
    z = 0
    for lad in lads[8:16]:
        if c1multiplier > 2:
            c1multiplier = 1
            number += 150
            z = 0
        seat = tkinter.Button(master, text=f"{lad}", relief="solid", font=("Arial", 20, "bold"), bg="red",cursor="star", width=10)
        seats.append(seat)
        seat.place(x=c1multiplier*1920/7 - z, y=number)
        c1multiplier += 1
        z += 60

    c2multiplier = 5
    number = 200
    z = 0
    for lad in lads[16:24]:
        if c2multiplier > 6:
            c2multiplier = 5
            number += 150
            z = 0
        seat = tkinter.Button(master, text=f"{lad}", relief="solid", font=("Arial", 20, "bold"), bg="red", cursor="star", width=10)
        seats.append(seat)
        seat.place(x=c2multiplier*1920/7 - z, y=number)
        c2multiplier += 1
        z += 60

    for seat in seats:
        if seat["text"] == "Samir":
            seat.config(bg="yellow")
        if seat["text"] in gurls:
            seat.config(bg="DeepPink2")


master = tkinter.Tk()
master.config(background="black")
master.attributes("-fullscreen", True)

lol1 = tkinter.Label(master, text="SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | SEATING ARRANGEMENT GENERATOR | ",
                     font=("Times", 20, "bold"), bg="black", fg="red")
lol1.place(x=0, y=0)
lol2 = tkinter.Label(master, text="UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | UMA WANTS TO SOCIALISE | ",
                     font=("Times", 20, "bold"), bg="black", fg="yellow")
lol2.place(x=0, y=1000)

board = tkinter.Label(master, text="____________________|lad board|____________________",
                     font=("Times", 20, "bold"), bg="black", fg="yellow")
##board.place(x=900, y=50)
board.place(x=700, y=50)
door = tkinter.Label(master, text="|_d_o_o_r_l_o_l_|",
                     font=("Times", 20, "bold"), bg="black", fg="yellow")
door.place(x=1600, y=50)

exit_button = tkinter.Button(master, text="EXIT", bg="#000000", fg="#FFFFFF", cursor="X_cursor",
                             activebackground="black", activeforeground="yellow",
                             relief="solid", font=("Arial", 10, "bold"), command=master.destroy)
exit_button.place(x=1870, y=10)

generate_button = tkinter.Button(master, text="GENERATE SEATING ARRANGEMENT", bg="#000000", fg="#FFFFFF", cursor="star",
                             activebackground="black", activeforeground="yellow",
                             relief="solid", font=("Arial", 29, "bold"), command=generate_arrangement)
generate_button.place(x=25, y=920)

master.mainloop()
