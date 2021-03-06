#this is gud

#https://docs.python.org/3/library/string.html

import pyglet, glooey, random, string

#=====================================

class PatLabel(glooey.Label):
    custom_font_size = 25
    custom_alignment = "center"
    custom_color = "7420BD"
    custom_bold = True

class PatLabel2(PatLabel):
    custom_font_size = 15
    custom_alignment = "center"
    custom_color = "ffffff"
    custom_bold = False

class PatButton(glooey.Button):
    class Label(glooey.Label):
        custom_padding = 10
        custom_color = "ffffff"
    class Base(glooey.images.Background):
        custom_color = "BD2069"
        custom_outline = "D32676"
    class Over(glooey.images.Background):
        custom_color = "D32676"
        custom_outline = "BD2069"
    class Down(glooey.images.Background):
        custom_outline = "000000"
        custom_color = "FFD8EA"

class PatForm(glooey.Form):
    class Label(glooey.EditableLabel):
        custom_color = "000000"
    class Base(glooey.images.Background):
        custom_color = "ffffff"
        custom_outline = "d8abff"

class PatFrame(glooey.Frame):
    class Decoration(glooey.images.Background):
        custom_color = "#ffccff"
        custom_outline = "ffffff"
    class Box(glooey.Bin):
        custom_padding = 5

#=====================================
#               Setting up elements
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)


frame = PatFrame()
rows = glooey.VBox()
frame.add(rows)
mainGui.add(frame)

title = PatLabel("This is the password checker.")
button1 = PatButton("Click to check!")
form1 = PatForm("Enter password here!")
text1 = PatLabel2("")
blank = PatLabel2("")
button2 = PatButton("Improve your Password!")
text2 = PatLabel2("")


#=====================================
#              Adding into rows

rows.add(title)
rows.add(blank)
rows.add(form1)
rows.add(button1)
rows.add(text1)
rows.add(blank)
rows.add(button2)
rows.add(text2)

#=====================================
#        Functions

def buttonDown(widget):
    if form1.text == "1234" or form1.text == "123456" or form1.text == "12345678" or form1.text == "password" or form1.text == "qwerty":
        PatLabel2.custom_color = "000000"
        text1.set_text("can you just actually think of a password?")
    else:
        PatLabel2.custom_color = "000000"
        text1.set_text("Gr8 one!")
    print(form1.text)

def newPass(widget):
    PatLabel2.custom_color = "000000"
    originalLength = len(form1.text)
    new = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for index in range(originalLength))
    text2.set_text(new)
#=====================================
#        Event listener + Run

button1.push_handlers(on_click=buttonDown)
button2.push_handlers(on_click=newPass)
pyglet.app.run()