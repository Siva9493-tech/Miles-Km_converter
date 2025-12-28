# def add(*args):
#     i=0
#     for n in args:
#         i = i+n
#     print(i)
#
# add(1,3,5,7)


from tkinter import *
window=Tk()
window.title("My first program")
window.minsize(500,300)

my_label=Label(text="i am label",font=("Arial",24))
my_label.grid(column=0,row=0)


def button_clicked():
    new_input=input.get()
    my_label["text"]=new_input

my_button=Button(text="Click me",command=button_clicked)
my_button.grid(column=1,row=1)
my_button_1=Button(text="new_button",command=button_clicked)
my_button_1.grid(column=3,row=0)

input=Entry()
input.grid(column=4,row=3)














window.mainloop()