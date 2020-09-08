#!/usr/bin/env python3
from tkinter import *
from tkinter.filedialog import *
from os import *
import os
from os.path import isfile, join
import tinify

def clear_placeholder(event):
    e.delete("0", "end")

def submit_command():
    pass

def error_1():
    newWindow = Toplevel(mainWindow)
    newWindow.configure(bg='#0F2027')
    newWindow.title("Error: 001")
    labelExample = Label(newWindow, text = "Ya existe un archivo con ese nombre, usa otro.", bg='#0F2027',fg="White")
    okButton = Button(newWindow,text='OK',command=newWindow.destroy)

    labelExample.grid(row=1, column=1, padx=4)
    okButton.grid(row=2,column=1)

def error_2():
    newWindow = Toplevel(mainWindow)
    newWindow.configure(bg='#0F2027')
    newWindow.title("Error: 002")
    labelExample = Label(newWindow, text = "Por favor, llena todos los campos.", bg='#0F2027',fg="White")
    labelExample.pack()
    labelExample.place(rely=0.5,relx=0.5, anchor="center")
    okButton = Button(newWindow,text='OK',command=newWindow.destroy)

    labelExample.grid(row=1, column=1, padx=4)
    okButton.grid(row=2,column=1)

def optimizeImages():
    tinify.key = '3RtYngxYMyYyWJSwysQLpmSsrwrHw3ty'

    outFolderName = e.get()

    files = []

    if outFolderName and sourceDir:
        try:
            files = [f for f in listdir(sourceDir) if isfile(join(sourceDir, f))]
            os.mkdir(outFolderName)

            for x in files:
                if x.lower().endswith(('.png', '.jpg', '.jpeg')):
                    open_img = tinify.from_file(sourceDir+'/'+x)
                    if outFolderName:
                        open_img.to_file(outFolderName+'/'+x)
                    else:
                        pass
                else:
                    pass
        except FileExistsError:
            error_1()
    else:
        error_2()

sourceDir=""

def fileDialogFolder():
    global sourceDir
    filename = askdirectory(initialdir = "~/",title = "Elije el folder de las imagenes")
    sourceDir=filename


mainWindow = Tk()# Main Window
mainWindow.configure(bg='#0F2027')#Window background
mainWindow.title("Optimizador")#Window title
mainWindow.resizable(0, 0)#Window resize range

#Variables
w = mainWindow.winfo_screenwidth()
h = mainWindow.winfo_screenheight()
x = (400/2)
y = (h/2) - (720/2)
ww = (w/6)

mainWindow.geometry('%dx%d+%d+%d' % (ww, ww, x, y))

# Primera entrada

e = Entry(mainWindow)
placeholder = 'Nombre del archivo de salida.'
e.insert(0, placeholder)
e.pack(padx=20, pady=20)
e.place(rely=0.5, relwidth=0.9, relx=0.5, anchor="center")
e.bind('<FocusIn>', clear_placeholder)
e.bind('<Return>', submit_command)

# Fin de la primera entrada

# Input de archivo
boton1 = Button(mainWindow,text='Elegir archivo de origen',command=fileDialogFolder)
boton1.place(relx=0.5, rely=0.2, anchor="center")
# Fin de el input de archivo

# Boton de 'salir'
boton1 = Button(mainWindow,text='Salir',command=mainWindow.quit)
boton1.place(relx=0.15, rely=0.9, anchor="center")
# Fin del boton 'salir'

# Boton de 'Optimizar'
boton2 = Button(mainWindow,text='Optimizar',command=optimizeImages)
boton2.place(relx=0.77, rely=0.9, anchor="center")
# Fin del boton 'optimizar'


mainWindow.mainloop()
