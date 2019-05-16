import argparse


def get_station_parser():
    station_parser = argparse.ArgumentParser()
    station_parser.add_argument('--gzt', type=bool, default=False, help="Install Git, tmux and Oh-My-Zsh")
    station_parser.add_argument('--pylib', type=bool, default=False, help="Install commonly used Python Libraries")
    station_parser.add_argument('--dj', type=bool, default=False, help="Instal Django and it's common dependencies")
    station_parser.add_argument('--fend', type=bool, default=False, help="Install Node, React and Angular")
    station_parser.add_argument('--android', type=bool, default=False, help="Install Android SDK")
    station_parser.add_argument('--gui', type=bool, default=False, help="Start GUI Installer!")
    station_parser.add_argument('--ubuntu', type=bool, default=True, help="For Ubuntu")
    station_parser.add_argument('--arch', type=bool, default=False, help="For Arch")
    args = station_parser.parse_args()

    return args
