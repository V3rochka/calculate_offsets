# Import Module
from tkinter import *
import pyperclip

# create root window
root = Tk()

# Set geometry(widthxheight)
root.geometry('350x200')
# root.configure(background='blue')



# adding a label to the root window
lbl1 = Label(root, text = "DEBUGGER base")
lbl1.grid()

txt1 = Entry(root, width=10)
txt1.grid(column =1, row =0)

lbl2 = Label(root, text = "IDA base")
lbl2.grid()

txt2 = Entry(root, width=10)
txt2.grid(column =1, row =1)

lbl3 = Label(root, text = "Address to convert")
lbl3.grid()

txt3 = Entry(root, width=10)
txt3.grid(column =1, row =2)


lbl4 = Label(root, text = "Answer")
lbl4.grid()

txt4 = Entry(root, width=10, background="white", foreground="black")
txt4.grid(column =1, row =3)


# function to display user text when 
# button is clicked
def con_ida():
    ida_base =  int(txt2.get(),16)
    x32_base =  int(txt1.get(),16)
    tmp_txt = txt3.get()
    if tmp_txt[:2] == '0x':
        tmp_txt = tmp_txt[2:]
    addr_to_convert = int(f"0x{tmp_txt}",16)
    res = addr_to_convert - x32_base + ida_base
    txt4.delete(0,END)
    txt4.insert(0,hex(res))
    pyperclip.copy(hex(res))

def con_x32():
    ida_base =  int(txt2.get(),16)
    x32_base =  int(txt1.get(),16)
    tmp_txt = txt3.get()
    if tmp_txt[:2] == '0x':
        tmp_txt = tmp_txt[2:]
    addr_to_convert = int(f"0x{tmp_txt}",16)
    res = addr_to_convert + x32_base - ida_base
    txt4.delete(0,END)
    txt4.insert(0,hex(res))
    pyperclip.copy(hex(res))

def set_title():
    title = txt5.get()
    root.title(title)
    txt5.delete(0,END)

if __name__ == '__main__':
    # button widget with red color text inside
    btn = Button(root, text = "Convert To IDA" ,
                fg = "black", command=con_ida)
    # Set Button Grid
    btn.grid(column=0, row=7)

    btn = Button(root, text = "Convert to DBG" ,
                fg = "black", command=con_x32)
    # Set Button Grid
    btn.grid(column=1, row=7)

    #Change title
    btn = Button(root, text = "Set Title" ,
                fg = "black", command=set_title)

    txt5 = Entry(root, width=10)
    txt5.grid(column =0, row =8 ,pady=20)

    # Set Button Grid
    btn.grid(column=1, row=8, pady=20)

    # Execute Tkinter
    root.mainloop()
