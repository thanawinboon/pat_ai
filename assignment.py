#this is gud
import pyglet, glooey

#=====================================

class PatLabel(glooey.Label):
    custom_font_size = 25
    custom_alignment = "center"
    custom_color = "ffffff"
    custom_bold = True
    class Label(glooey.Label):
        custom_padding = 10
    class Base(glooey.images.Background):
        custom_color = "000000"
        custom_outline = "00ffff"
    class Over(glooey.images.Background):
        custom_color = "ffffff"
        custom_outline = "666666"
    class Down(glooey.images.Background):
        custom_outline = "green"
        custom_color = "white"


class PatFrame(glooey.Frame):
    class Decoration(glooey.images.Background):
        custom_color = "003333"
        custom_outline = "ffffff"
    class Box(glooey.Bin):
        custom_padding = 5

#=====================================

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)

frame = PatFrame()
rows = glooey.VBox()
frame.add(rows)
mainGui.add(frame)

title1 = PatLabel("This is the password checker.")
rows.add(title1)

pyglet.app.run()

#=====================================
                # OLD CODE
'''
mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

title1 = glooey.Label("This is the password checker.")
rows.add(title1)

ask = glooey.Label("Please enter a password")
rows.add(ask)
form = glooey.Form("")
rows.add(form)

button = glooey.Button("This is a scam!")
def buttclicked(wiget):
    print(form.text)
button.push_handlers(on_click=buttclicked)
rows.add(button)

pyglet.app.run()

#helloworld
'''