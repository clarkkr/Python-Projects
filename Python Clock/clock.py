# Importing tkinter for GUI
from tkinter import *
from tkinter.ttk import *

# Importing strftime to retrieve system time
from time import strftime

# Create tkinter window
root = Tk()
root.title('Digital Clock')

# Function to display time on the label

def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)

# Label styling
lbl = Label(root, font = ('calibri', 40, 'bold'),
            background = 'blue',
            foreground = 'white')
    
# Placing the time at the center of the window
lbl.pack(anchor = 'center')
time()

mainloop()