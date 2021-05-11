from Caesar import Caesar
from tkinter import *

app = Tk()
app.title("Encrypt Message")

TitleLabel = Label(app, text="Hide Your Messages!",font=('bold',14))
TitleLabel.place(x=270,y=20)

plainLabel = Label(app,text="Your Text?").place(x=10,y=60)
plain = Entry(app, width=70, borderwidth=1)
plain.place(x=90, y=60)
keyCodeLabel= Label(app, text="Key").place(x=10,y=100)
keyCode = Entry(app, width=40, borderwidth=1)
keyCode.place(x=90,y=100)

hasil = Entry(app, width=40, borderwidth=1)
hasil.place(x=90,y=140)

def ProcessEncrypt(text, key):
	chiper = Caesar(text,key)
	return chiper.encrypt()

def ProcessDecrypt(text, key):
	chiper = Caesar(text,key)
	return chiper.decrypt()

def EncryptButton():
	text = plain.get()
	key = int(keyCode.get())
	chiper = ProcessEncrypt(text,key)
	hasil.delete(0,END)
	hasil.insert(0,chiper)

def DecryptButton():
	text = plain.get()
	key = int(keyCode.get())
	chiper = ProcessDecrypt(text,key)
	hasil.delete(0,END)
	hasil.insert(0,chiper)

processButtonEncrypt = Button(app,text="Encrypt",command=EncryptButton)
processButtonEncrypt.place(x=10,y=140)
processButtonDecrypt = Button(app,text="Decrypt",command=DecryptButton)
processButtonDecrypt.place(x=10,y=180)


app.geometry('700x350')
app.mainloop()

