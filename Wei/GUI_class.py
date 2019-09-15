import tkinter as tk

on_hit = False


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.creat_widget()

    def creat_widget(self):
        var = tk.StringVar()

        self.entry = tk.Entry(self.master)
        self.entry.pack()

        self.text = tk.Text(self.master,)
        self.text.pack()

        def read_text(self):
            var.set(self.entry.get())

        self.read_text_button = tk.Button(self.master, command=read_text)
        self.read_text_button.pack()


def construct():
    window = tk.Tk()
    window.title("my window")
    window.geometry('500x500')

    var = tk.StringVar()
    lable = tk.Label(window, textvariable=var, bg="red", font=('Arial', 12), width=30, height=2)
    lable.pack(side='bottom')

    def hit_me():
        global on_hit
        if on_hit == False:
            on_hit = True
            var.set('you hit me')
        else:
            on_hit = False
            var.set('')

    def insert_point():
        var = entry.get()
        text.insert('insert', var)

    def insert_end():
        var = entry.get()
        text.insert('end', var)

    button1 = tk.Button(window, text='point', font=('Arial', 12), width=10, height=2, command=insert_point)
    button1.pack()
    button2 = tk.Button(window, text='end', font=('Arial', 12), width=10, height=2, command=insert_end)
    button2.pack()
    entry = tk.Entry(window, show=None)
    entry.pack()

    text = tk.Text(window, height=3)
    text.pack()

    window.mainloop()
