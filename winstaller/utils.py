import os


class Installer:

    def __init__(self, package_manager, py_package_manager='pip'):
        self.tmux_util = "if [ \"$TMUX\" = \"\" ]; then exec tmux -u; fi"
        self.package_manager = package_manager
        self.py_package_manager = py_package_manager
        self.install_git = "sudo " + self.package_manager + " install git"
        self.install_tmux = "sudo " + self.package_manager + " install tmux"
        self.install_zsh = "sudo " + self.package_manager + " install zsh"

    def gzt_installer(self):
        print("Installing Git, tmux, Oh-My-Zsh")
        os.system(self.install_git)
        os.system(self.install_tmux)
        os.system(self.install_zsh)
        os.system(
            "sh -c \"$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)")
        os.system("sudo apt-get install fonts-powerline")
        # Adding tmux to the zsh file
        with open("~/.zshrc", "a") as zshfile:
            zshfile.write(self.tmux_util)

    def pylib_installer(self):
        print("Installing required libraries for Machine Learning")
        os.system(
            "sudo " + self.py_package_manager + " install -r machine-learning/machine_learning_req.txt")

    def dj_installer(self):
        print("Installing required libraries for Web Dev (Django)")
        os.system("sudo " + self.py_package_manager + " install -r server/web_dev_req.txt")

    def fend_installer(self):
        print("Installing requited node.js and it's dependencies")
        os.system("sudo " + self.package_manager + " install npm")
        os.system("sudo " + self.package_manager + " install nodejs")
        os.system("sudo " + self.package_manager + " install -y build-essential")
        os.system("npm install -g @angular/cli")
        os.system("sudo npm install -g create-react-app")

    def android_installer(self):
        print("Installing Android SDK")
        os.system("./android/install_android_sdk.bash")

class UbuntuInstaller(Installer):

    def __init__(self):
        super().__init__("apt", py_package_manager="pip3") 

class ArchInstaller(Installer):

    def __init__(self):
        super().__init__("pacman")


