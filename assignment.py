import pyglet, glooey

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