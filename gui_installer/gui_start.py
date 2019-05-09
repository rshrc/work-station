from tkinter import *

from tkinter import messagebox

# from winstaller.utils import Installer
#
# ins = Installer()

# Setting up the GUI

window = Tk()
window.title("Workstation.PY")
window.geometry('720x600')
button_padding_x = (10, 10)
button_padding_y = (10, 10)


def install_python():
    messagebox.showinfo('Success!', 'Python Installed along with required libraries')


def install_django():
    messagebox.showinfo('Success!', 'Django Installed along with django utils')


def install_gzt():
    messagebox.showinfo('Success!', 'Git/tmux/ZSH installed and added to bash!')


def install_fend():
    messagebox.showinfo('Success!', 'Front End Utilities installed')


def install_android():
    messagebox.showinfo('Success!', 'Android SDK installed!')


python_button = Button(window, text='Install Python', command=install_python)
django_button = Button(window, text='Install Django', command=install_django)
gzt_button = Button(window, text='Install Git/TMUX/ZSH', command=install_gzt)
fend_button = Button(window, text='Install Frontend', command=install_fend)
android_button = Button(window, text='Install Android SDK', command=install_android)

python_button.grid(column=2, row=2, padx=button_padding_x, pady=button_padding_y)
django_button.grid(column=3, row=2, padx=button_padding_x, pady=button_padding_y)
gzt_button.grid(column=4, row=2, padx=button_padding_x, pady=button_padding_y)
fend_button.grid(column=5, row=2, padx=button_padding_x, pady=button_padding_y)
android_button.grid(column=6, row=2, padx=button_padding_x, pady=button_padding_y)

window.mainloop()
