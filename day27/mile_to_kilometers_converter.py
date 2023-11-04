from tkinter import *

# initialize new object window from class Tk()
window = Tk()

# give the window a title
window.title("Mile to Km Converter")

# resize window
# window.minsize(width=500, height=100)
window.config(padx=20, pady=20)

# miles entry
miles_input = Entry(width=10)
miles_input.grid(column=1, row=0)

# miles_label
miles_label = Label(text="Miles", font=("Arial",15))
miles_label.grid(column=2, row=0)

# is_equal_to label
is_equal_label = Label(text="is equal to", font=("Arial",15))
is_equal_label.grid(column=0, row=1)

# km_label
km_label = Label(text=" Km", font=("Arial",15))
km_label.grid(column=2, row=1)

# km_value
km_value_label = Label(text="0",font=("Arial",15))
km_value_label.grid(column=1, row=1)

# function to convert miles to km
def miles_to_km():
    miles_value = float(miles_input.get()) # returns the input from the user as a string
    miles_converted = miles_value * 1.60934
    km_value_label.config(text=miles_converted)
    
# calculate button
calculate_button = Button(text="Calculate", command=miles_to_km)
calculate_button.grid(column=1, row=2)

# keep window open
window.mainloop()