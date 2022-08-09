# test111

import tkinter as tk
import tkinter.ttk as ttk


class Widget(ttk.Notebook):
    def __init__(self, master=None, **kw):
        super(Widget, self).__init__(master, **kw)
        self.Frame1 = ttk.Frame(self)
        self.Frame1.configure(height=200, width=200)
        self.Frame1.pack(side="top")
        self.add(self.Frame1, text="Tab1")
        self.Frame2 = ttk.Frame(self)
        self.Frame2.configure(height=200, width=200)
        self.Frame2.pack(side="top")
        self.add(self.Frame2, text="Tab2")
        self.Frame3 = ttk.Frame(self)
        self.Frame3.configure(height=200, width=200)
        self.Frame3.pack(side="top")
        self.add(self.Frame3, text="关于作者")
        self.configure(height=200, width=200)
        self.pack(side="top")


if __name__ == "__main__":
    root = tk.Tk()
    widget = Widget(root)
    widget.pack(expand=True, fill="both")
    root.mainloop()
