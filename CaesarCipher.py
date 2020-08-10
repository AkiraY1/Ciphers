from tkinter import *

window = Tk()
window.title('My first GUI')

def hello_function():
    print('Hello, World!')
    display_area.config(text = 'Hello, World!', fg="yellow", bg = "black")

def move_circle(event):
    key = event.keysym
    if key == "Right":
        canvas.move(circle,10,0)
    elif key == "Left":
        canvas.move(circle,-10,0)
    elif key == "Up":
        canvas.move(mychar,0,10)
    elif key == "Down":
        canvas.move(mychar,0,-10)

# def move_object(event):
    # canvas.coords(circle2,event.x,event.y)

greeting = Label(
    text ="Hello Tkinter",
    fg ="#34A2FE",
    bg ="black",
    width =10,
    height = 5
)
greeting.pack()

button1 = Button(window,
    text ="Click me",
    command = hello_function
    )
button1.pack()

button2 = Button(window, text ="Remove", command = button1.destroy)
button2.pack()

display_area = Label(window, text="")
display_area.pack()

label = Label(text="Name")
entry = Entry()

label.pack()
entry.pack()

button3 = Button(window, text ="Enter", command = entry.get())
button3.pack()

canvas = Canvas(window, width=1000,height=1000)
canvas.pack()
circle = canvas.create_oval(200,300,230,330, fill="red")
# circle2 = canvas.create_oval(200,300,230,430, fill="red")

img = PhotoImage(file="Rotating_earth_(large).gif")
mychar = canvas.create_image(500, 100, image=img)


canvas.bind_all('<Key>', move_circle)
# canvas.bind_all('<Button-1>', move_object)
window.mainloop()