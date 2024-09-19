import tkinter
from tkinter import END

window = tkinter.Tk()
window.title('My First GUI Program')
window.geometry('500x500')

#Label
my_label = tkinter.Label( text='Hello World', font=('Arial', 15))
my_label.pack()


my_label['text']='Hello World'
my_label.config(font=('Arial', 15))

#button
def button_clicked():
    print('button clicked')
    new_text = input.get()
    my_label.config(text=new_text)

button = tkinter.Button(text='Click me', command=button_clicked)
button.pack()


#Input

input = tkinter.Entry()
input.pack()
input.get()

#Text input
text = tkinter.Text(width=30, height=5, font=('Arial', 15))
text.focus() #puts cursor in textbox
text.insert(END, "Example of mumultiline text entry also act as a placeholder")
print(text.get("1.0", END))
text.pack()






window.mainloop()