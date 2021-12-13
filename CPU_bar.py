import tkinter as tk


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.attributes('-alpha', 1)  # 100 percent transparency
        self.attributes('-topmost', True)  # window on top of other windows
        self.overrideredirect(True)  # ban the frame
        self.resizable(False, False)  # ban alter the size of the window


root = Application()
root.mainloop()