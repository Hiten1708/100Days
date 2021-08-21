from tkinter import *

window = Tk()
window.title("Mile to km calculator")
window.minsize(height=100, width=150)

out = Label(text=0, )
out.grid(row=3, column=1)

label = Label(text="is equal to")
label.grid(row=3, column=0)

m_label = Label(text="miles")
m_label.grid(row=2, column=2)

km_label = Label(text="Km")
km_label.grid(row=3, column=2)

ent = Entry(width=10)
ent.grid(row=2, column=1)


def calculator():
    answer = round(int(ent.get())*1.6, 0)
    out.config(text=answer)


but = Button(text="Calculate", command=calculator)
but.grid(row=4, column=1)




window.mainloop()

