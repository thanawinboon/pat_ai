#this is gud
import pyglet, glooey

#=====================================

class PatLable(glooey.lable):
    custom_font_size = 25
    custom_alignment = "center"
    custom_color = "ffffff"
    custom_bold = True

#=====================================

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

title1 = PatLable("This is the password checker.")
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