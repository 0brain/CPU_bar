import tkinter as tk
from tkinter import ttk
import sys


class Application(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.attributes('-alpha', 1)  # 100 percent transparency
        self.wait_visibility()
        self.wm_attributes('-alpha', 1)
        self.attributes('-topmost', True)  # window on top of other windows
        self.overrideredirect(True)  # ban the frame
        self.resizable(False, False)  # ban alter the size of the window
        self.title('CPU bar')

        self.set_ui()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(fill=tk.X)

    def app_exit(self):
        self.destroy()
        sys.exit()


root = Application()
root.mainloop()