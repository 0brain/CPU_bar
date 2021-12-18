import tkinter as tk
from tkinter import ttk
import sys
from process import CpuBar
from widget_update import Configure_widgets


class Application(tk.Tk, Configure_widgets):
    def __init__(self):
        tk.Tk.__init__(self)
        #self.attributes('-alpha', 1)  # 100 percent transparency
        self.wait_visibility()
        self.attributes('-alpha', 1)
        self.attributes('-topmost', True)  # window on top of other windows
        self.overrideredirect(True)  # ban the frame
        self.resizable(False, False)  # ban alter the size of the window
        self.title('CPU bar')

        self.cpu = CpuBar()
        self.set_ui()
        self.make_bar_cpu_usage()
        self.configure_cpu_bar()

    def set_ui(self):
        exit_but = ttk.Button(self, text='Exit', command=self.app_exit)
        exit_but.pack(fill=tk.X)

        self.bar2 = ttk.LabelFrame(self, text='Manual')
        self.bar2.pack(fill=tk.X)

        self.combo_win = ttk.Combobox(self.bar2,
                                      values=["hide", "don't hide", 'min'],
                                      width=9, state='readonly')

        self.combo_win.current(1)
        self.combo_win.pack(side=tk.LEFT)

        ttk.Button(self.bar2, text='move').pack(side=tk.LEFT)
        ttk.Button(self.bar2, text='>>>').pack(side=tk.LEFT)

        self.bar = ttk.LabelFrame(self, text='Power')
        self.bar.pack(fill=tk.BOTH)

        self.bind_class('Tk', '<Enter>', self.enter_mouse)
        self.bind_class('Tk', '<Leave>', self.leave_mouse)

    def make_bar_cpu_usage(self):
        ttk.Label(self.bar, text=f'physical cores: {self.cpu.cpu_count}, logical cores: {self.cpu.cpu_count_logical}',
                    anchor=tk.CENTER).pack(fill=tk.X)

        self.list_label = []
        self.list_pbar = []

        for i in range(self.cpu.cpu_count_logical):
            self.list_label.append(ttk.Label(self.bar, anchor=tk.CENTER))
            self.list_pbar.append(ttk.Progressbar(self.bar, length=100))
        for i in range(self.cpu.cpu_count_logical):
            self.list_label[i].pack(fill=tk.X)
            self.list_pbar[i].pack(fill=tk.X)

        self.ram_lab = ttk.Label(self.bar, text='', anchor=tk.CENTER)
        self.ram_lab.pack(fill=tk.X)
        self.ram_bar = ttk.Progressbar(self.bar, length=100)
        self.ram_bar.pack(fill=tk.X)

    def enter_mouse(self, event):
        if self.combo_win.current() == 0 or 1:
            self.geometry('')

    def leave_mouse(self, event):
        if self.combo_win.current() == 0:
            self.geometry(f"{self.winfo_width()}x1")

    def app_exit(self):
        self.destroy()
        sys.exit()


if __name__ == '__main__':
    root = Application()
    root.mainloop()