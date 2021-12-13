import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1) # 100 percent transparency
        self.attributes('-topmost', True) # window on top of other windows


root = Application()
root.mainloop()