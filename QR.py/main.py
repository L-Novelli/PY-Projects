from tkinter import *
from tkinter import ttk
import tkinter as tk
import qrcode

root = tk.Tk()
root.geometry("1240x720")
root.configure(background='black')
tk.Wm.wm_title(root, "QR GENERATOR")
    
def Link():
    data = entry1.get() 
    if len(data) == 0:
        status1.configure(text = 'Still waiting for data')  
        return data
    elif data.isdigit:
        status1.configure(text = 'Valid format!')
        return data
    else:
        status1.configure(text = 'Invalid format!')
        return False
    

def Name():
    input = entry2.get()
    if len(input) == 0:
        status2.configure(text = 'Still waiting for input')  
        return input
    elif input.isdigit:
        status2.configure(text = 'Valid format!')
        return input
    else:
        status2.configure(text = 'Invalid format!')
        return False

def Save():
    name = entry2.get()
    img = qrcode.make(Link())
    img.save(f'{name}.png')
    top= Toplevel(root)
    top.geometry("250x250")
    top.title("Message")
    l = Label(top, text= "QR saved", font=('Mistral 18 bold')).place(x=125,y=125)
    
  
mainFrame = ttk.Frame(root, style='Frame.TFrame')
mainFrame.grid(row = 0, column = 0, sticky = 'NEWS')

label0 = ttk.Label(mainFrame, text = "Link for the QR")
label0.grid(row = 0, column = 1, padx = 10, pady = 15,  sticky = 'WE')

label1 = ttk.Entry(mainFrame, text = 'enter the link for the QR: ', font=('Mistral', 18, 'bold'))
label1.grid(row = 1, column = 1, padx = 10, pady = 15,  sticky = 'WE')

entry1 = ttk.Entry(mainFrame)
entry1.grid(row = 1, column = 1, padx = 10, pady = 15, sticky = 'NSEW')

button1 = ttk.Button(mainFrame, text = "ADD", command = Link)
button1.grid(row = 1, column = 2, padx = 5, pady = 15, sticky = 'NSEW')

status1 = ttk.Label(mainFrame, text = "Waiting for input")
status1.grid(row = 1, column = 3, padx = 10, pady = 15, sticky = 'NSEW')
  
label0 = ttk.Label(mainFrame, text = "QR name")
label0.grid(row = 2, column = 1, padx = 10, pady = 15,  sticky = 'WE')

label2 = ttk.Entry(mainFrame, text = 'enter que QR name ', font=('Mistral', 18, 'bold'))
label1.grid(row = 3, column = 1, padx = 10, pady = 15,  sticky = 'WE')

entry2 = ttk.Entry(mainFrame)
entry2.grid(row = 3, column = 1, padx = 10, pady = 15, sticky = 'NSEW')

button2 = ttk.Button(mainFrame, text = "ADD", command = Name)
button2.grid(row = 3, column = 2, padx = 5, pady = 15, sticky = 'NSEW')

status2 = ttk.Label(mainFrame, text = "Waiting for input")
status2.grid(row = 3, column = 3, padx = 10, pady = 15, sticky = 'NSEW')

button3 = ttk.Button(mainFrame, text = "Save", command = lambda:Save())
button3.grid(row = 4, column = 1, padx = 10, pady = 15, sticky = 'NSEW')
  
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight = 1)
mainFrame.columnconfigure(0, weight = 1)
mainFrame.columnconfigure(1, weight = 1)
mainFrame.columnconfigure(2, weight = 1)

root.mainloop()
