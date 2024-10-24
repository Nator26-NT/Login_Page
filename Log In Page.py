from tkinter import *

root = Tk()
root.configure(bg="black")

root.title("NatorBook")
root.geometry("800x800")

Log_in = Label(root, text="LogIn" , width=10 , height=5 , fg="pink" ,bg='black' , font=('Arial', 20))

Log_in.pack()
root_2 = Frame(root)
root_2.pack()
Username = Label(root_2 , text="Username:" , fg="pink" ,bg='black' , font=('Arial', 10))
password = Label(root_2, text="Password:" ,fg="pink" ,bg='black' , font=('Arial', 10))
Textbox_1 = Text(root_2, width=30,height=1)
Textbox_2 = Text(root_2 , width=30, height=1)
button = Button(root, text="Submit", bg="pink" ,fg='black', width=10, height=1)

Username.grid(column=0, row=0)
password.grid(column=0, row=1)
Textbox_1.grid(column=1, row=0)
Textbox_2.grid(column=1, row=1)
button.pack(padx=5, pady=10)






root.mainloop()

