from tkinter import *
window=Tk()
window.title("Mile converter Km")
window.config(padx=20,pady=20)

mile_input=Entry(width=10)
mile_input.grid(column=1,row=0)

mile_name=Label(text="Mile",font=("Arial"))
mile_name.grid(column=2,row=0)

is_equal_to=Label(text="is equal to",font=("Arial"))
is_equal_to.grid(column=0,row=1)

km_result=Label(text="0", font=("Arial"))
km_result.grid(column=1, row=1)

km_name=Label(text="Km", font=("Arial"))
km_name.grid(column=2, row=1)


def button_clicked():
    miles=float(mile_input.get())
    km=round(miles*1.609)
    km_result.config(text=f"{km}")



cal_button=Button(text="Calculate",command=button_clicked)
cal_button.grid(column=1,row=2)









window.mainloop()







