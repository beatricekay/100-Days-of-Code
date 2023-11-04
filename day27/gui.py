from tkinter import *

# initialize new object window from class Tk()
window = Tk()

# give the window a title
window.title("My First GUI Program")

# resize window
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)

# button_clicked() function
def button_clicked():
    print("I got clicked")
    new_text = input.get() # returns the input from the user as a string
    my_label.config(text=new_text)

# add a label to the window
my_label = Label(text="I Am a Label", font=("Arial",24,"bold"))

#.pack() or .place() or .grid() is required for it to appear on screen
# you can only choose one and cannot mix the methods together
# my_label.pack() 
# .pack() will stack all the widgets next to each other in a logical format
# setting side="left" will change the position of the widget

# .place() allows us to precisely place the widget
# my_label.place(x=0, y=0)

# .grid() splits the screen into position rows and columns
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

# adding a button
button = Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

# adding a new button
new_button = Button(text="New Button")
new_button.grid(column=2, row=0)

# entry - takes an input
input = Entry(width=10)
input.grid(column=3, row=2)

# keep window open
window.mainloop()