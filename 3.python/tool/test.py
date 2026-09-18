import time
from tkinter import Tk, Label

root = Tk()
root.title("简易时钟")
root.geometry("320x120")

lab = Label(root, text="", font=("simhei",36))
lab.pack()

def update_time():
    t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    lab.config(text=t)
    root.after(1000, update_time)

update_time()
root.mainloop()
