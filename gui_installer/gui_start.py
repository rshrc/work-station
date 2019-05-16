from tkinter import *

from tkinter import messagebox

from winstaller.utils import Installer
#
# ins = Installer()

# Setting up the GUI

class InstallerGUI:

    def __init__(self):

        self.window = Tk()
        self.window.title("Workstation.PY")
        self.window.geometry('720x600')
        self.button_padding_x = (10, 10)
        self.button_padding_y = (10, 10)


    def install_python(self):
        messagebox.showinfo('Success!', 'Python Installed along with required libraries')


    def install_django(self):
        messagebox.showinfo('Success!', 'Django Installed along with django utils')


    def install_gzt(self):
        messagebox.showinfo('Success!', 'Git/tmux/ZSH installed and added to bash!')


    def install_fend(self):
        messagebox.showinfo('Success!', 'Front End Utilities installed')


    def install_android(self):
        messagebox.showinfo('Success!', 'Android SDK installed!')

    def define_gui(self):

        python_button = Button(self.window, text='Install Python', command=self.install_python)
        django_button = Button(self.window, text='Install Django', command=self.install_django)
        gzt_button = Button(self.window, text='Install Git/TMUX/ZSH', command=self.install_gzt)
        fend_button = Button(self.window, text='Install Frontend', command=self.install_fend)
        android_button = Button(self.window, text='Install Android SDK', command=self.install_android)

        python_button.grid(column=2, row=2, padx=self.button_padding_x, pady=self.button_padding_y)
        django_button.grid(column=3, row=2, padx=self.button_padding_x, pady=self.button_padding_y)
        gzt_button.grid(column=4, row=2, padx=self.button_padding_x, pady=self.button_padding_y)
        fend_button.grid(column=5, row=2, padx=self.button_padding_x, pady=self.button_padding_y)
        android_button.grid(column=6, row=2, padx=self.button_padding_x, pady=self.button_padding_y)

        self.window.mainloop()
