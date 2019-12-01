def changeBackground(x, y, button, pressed):

    """Changes background image on click"""

    global w, h
    global backgroundImage
    global canvas
    global images
    global image
    global imageLocation

    if pressed:
        print("lad")
        backgroundImage = ImageTk.PhotoImage(Image.open(imageLocation+next(images)))
        canvas.delete(image)
        image = canvas.create_image(w/2, h/2, image = backgroundImage)
