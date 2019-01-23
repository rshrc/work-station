import os
import sys
import subprocess

print("Work Station Ready to be Created!")

print("Installing Git, TMUX, ZSHRC")
os.system("sudo apt install git")
os.system("sudo apt install tmux")
os.system("sh -c \"$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)")

# Installing most commanly used Python Libraries
print("Installing required libraries for Machine Learning")
os.system("sudo pip3 install -r /../machine-learning/machine_learning_req.txt")

print("Installing required libraries for Web Dev (Django)")
os.system("sudo pip3 install -r /../server/web_dev_req.txt")

print("Installing requited node.js and it's dependencies")
os.system("sudo apt install nodejs")
os.system("sudo apt install npm")
os.system("sudo apt-get install -y build-essential")
os.system("npm install -g @angular/cli")
os.system("sudo npm install -g create-react-app")

print("Installing Android SDK")
os.system("./android/install_android_sdk.bash")



