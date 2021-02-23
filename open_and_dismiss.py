from tkinter import *
from functools import partial  # To prevent unwanted windows


class number1:
    def __init__(self, partner):
        self.button1 = Button(text='Button 1', command=lambda: self.tran())
        self.button1.pack()

    def tran(self):
        number2(self)


class number2:
    def __init__(self, partner):
        self.newwin = Toplevel()
        self.newwin.protocol('WM_DELETE_WINDOW', partial(self.close, partner))

        self.button2 = Button(self.newwin, text='Dismiss', command=partial(self.close, partner))
        self.button2.pack()

        partner.button1.config(state=DISABLED)

    def close(self, partner):
        partner.button1.config(state=NORMAL)
        self.newwin.destroy()
# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Temperature Converter")
    app = number1(root)
    root.mainloop()
