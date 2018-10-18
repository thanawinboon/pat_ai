print("")

import pyglet, glooey

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

label = glooey.Label("Hello World")
rows.add(label)

form = glooey.Form("Enter password for me to steal: ")
rows.add(form)

button = glooey.Button("This is a scam!")
def buttclicked(wiget):
    print(form.text)
button.push_handlers(on_click=buttclicked)
rows.add(button)

label.set_text("Some new text")

pyglet.app.run()

#helloworld