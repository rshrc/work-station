import os

import station_parser

args = station_parser.get_station_parser()

tmux_util = "if [ \"$TMUX\" = \"\" ]; then exec tmux -u; fi"

print("Work Station Ready to be Created!")

if args.gzt:
    print("Installing Git, tmux, Oh-My-Zsh")
    os.system("sudo apt install git")
    os.system("sudo apt install tmux")
    os.system("sudo apt install zsh")
    os.system("sh -c \"$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)")
    os.system("sudo apt-get install fonts-powerline")
    # Adding tmux to the zsh file
    with open("~/.zshrc", "a") as zshfile:
        zshfile.write(tmux_util)

if args.pylib:
    print("Installing required libraries for Machine Learning")
    os.system("sudo pip3 install -r /../machine-learning/machine_learning_req.txt")

if args.dj:
    print("Installing required libraries for Web Dev (Django)")
    os.system("sudo pip3 install -r /../server/web_dev_req.txt")

if args.fend:
    print("Installing requited node.js and it's dependencies")
    os.system("sudo apt install nodejs")
    os.system("sudo apt install npm")
    os.system("sudo apt-get install -y build-essential")
    os.system("npm install -g @angular/cli")
    os.system("sudo npm install -g create-react-app")

if args.android:
    print("Installing Android SDK")
    os.system("./android/install_android_sdk.bash")
