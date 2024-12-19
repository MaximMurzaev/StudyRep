import tkinter
from tkinter import filedialog
from tkinter import messagebox

import os

def file_select():
    filename = filedialog.askopenfilename(initialdir='/', title='Выберите файл', filetypes=(('текстовый файл', 'txt'),
                                                                                            ('Все файлы', '*')))
    text['text'] = text['text'] + ' ' + filename
    os.startfile(filename)

def info():
    messagebox.showinfo('Как пользоваться программой', 'Просто нажимай на выбрать файл и все понятно')

def about():
    messagebox.showinfo('О программе', 'Версия: 1.0. Автор: Нубик')

window = tkinter.Tk()

window.title('Проводник')
window.geometry('450x200')
window.resizable(False, False)
window.configure(bg='orange', borderwidth=3)
text = tkinter.Label(window, text='Файл', height=5, width=65, background='silver')
text.grid(column=1, row=2)
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл', command=file_select)
button_select.grid(column=1, row=3)

main_menu = tkinter.Menu()
main_menu.add_cascade(label='Инфо', command=info)
main_menu.add_cascade(label='О программе', command=about)
window.config(menu=main_menu)

window.mainloop()