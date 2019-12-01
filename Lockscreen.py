import tkinter
from PIL import ImageTk, Image
import random as r
import os
import sys
import itertools

loc = os.path.abspath(os.path.dirname(sys.argv[0]))
os.chdir(loc)

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
    'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
    'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
    'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
    'light slate gray', 'gray', 'light grey', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
    'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue',  'blue',
    'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
    'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
    'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
    'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
    'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
    'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
    'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
    'indian red', 'saddle brown', 'sandy brown',
    'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
    'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
    'pale violet red', 'maroon', 'medium violet red', 'violet red',
    'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
    'thistle', 'snow2', 'snow3',
    'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
    'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
    'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
    'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
    'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
    'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
    'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
    'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
    'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
    'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
    'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
    'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
    'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
    'cyan4', 'DarkSlateGray1', 'DarkSlateGray2', 'DarkSlateGray3', 'DarkSlateGray4',
    'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
    'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
    'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
    'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
    'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
    'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
    'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
    'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
    'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
    'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
    'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
    'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
    'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
    'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
    'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
    'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
    'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
    'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
    'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
    'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
    'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
    'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
    'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
    'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
    'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
    'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
    'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
    'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

lockscreen = tkinter.Tk()
lockscreen.config(background="black")
lockscreen.attributes("-fullscreen", True)

images = os.listdir(f"lockpicks\\")
r.shuffle(images)
images = itertools.cycle(images)
pic = next(images)

canvas1 = tkinter.Canvas(lockscreen, width=1920, height=1080)
canvas1.grid(row=0, column=0, sticky="NSEW")
bgimage = ImageTk.PhotoImage(Image.open(f"lockpicks\\{pic}"))
image1 = canvas1.create_image(1920 / 2, 1080 / 2, image=bgimage)

# DANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONE #
lockscreen.attributes("-topmost", True)  # This keeps the lockscreen window always on top of all other windows
lockscreen.overrideredirect(True)  # Window cannot be closed by normal means (not even Alt-F4), only through the power of the Task Manager
def on_closing():  # Even if the user somehow manages to get the lockscreen into windowed mode, this disables the close (X) button (on the top right)
    pass
lockscreen.protocol("WM_DELETE_WINDOW", on_closing)
# DANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONEDANGER ZONE #

def changebg():
    global bgimage, image1, canvas1
    bgimage = ImageTk.PhotoImage(Image.open(f"lockpicks\\{next(images)}"))
    canvas1.delete(image1)
    image1 = canvas1.create_image(1920 / 2, 1080 / 2, image=bgimage)


buttons = []
multiplier = 1
number = 50
lol1 = tkinter.Label(lockscreen, text="THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.THE BOARD IS LOCKED; ENTER THE PASSWORD TO UNLOCK.", font=("Times", 20, "bold"), bg="black", fg="red")
lol1.place(x=0, y=0)
lol2 = tkinter.Label(lockscreen, text="12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE 12B WAS HERE ", font=("Times", 20, "bold"), bg="black", fg="red")
lol2.place(x=0, y=1000)

for i in range(479):
    if multiplier > 50:
        multiplier = 1
        number += 100
    lockscreen_buttons = tkinter.Button(lockscreen, text=f"{i}", bg=COLORS[i], fg=COLORS[478-i])
    buttons.append(lockscreen_buttons)
    lockscreen_buttons.place(x=multiplier*1920/51, y=number)
    multiplier += 1

almostchosen_one = r.choice(buttons[3:-1])
almostchosen_one.config(bg="red", fg="black")

chosen_num = r.choice([12, 96, 97])
if chosen_num == 12:  # +12
    buttons[0].config(bg="blue")
elif chosen_num == 96:  # +96
    buttons[0].config(bg="green")
else:  # +97
    buttons[0].config(bg="red")

five = r.choice([5, -5])
chosen_num += five
if five == 5:  # +5
    buttons[-1].config(bg="white", fg="black")
else:  # -5
    buttons[-1].config(bg="black", fg="white")

tenno = r.choice([10, -10])
chosen_num += tenno
if tenno == 10:  # +10
    buttons[1].config(bg="white", fg="black")
else:  # -10
    buttons[1].config(bg="black", fg="white")

chosenone_index = buttons.index(almostchosen_one) + chosen_num
if chosenone_index > 478:  # If it goes past button 478, start reverse indexing with the difference
    chosenone_index = 478 - chosenone_index
if chosenone_index >= 0:
    buttons[2].config(bg="yellow", fg="black")  # Normal indexing
else:
    buttons[2].config(bg="black", fg="yellow")  # Reverse indexing

chosen_one = buttons[chosenone_index]
chosen_one.config(command=lockscreen.destroy)

remaining_butts = buttons
remaining_butts.remove(chosen_one)  # remaining_butts is now a list of all buttons, other than <chosen_one>

for button in remaining_butts:
    button.config(command=changebg)

lockscreen.mainloop()
