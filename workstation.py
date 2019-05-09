import station_parser
from winstaller.utils import Installer

args = station_parser.get_station_parser()
installer = Installer()


print("Work Station Ready to be Created!")

if args.gzt:
    installer.gzt_installer()

if args.pylib:
    installer.pylib_installer()

if args.dj:
    installer.dj_installer()

if args.fend:
    installer.fend_installer()

if args.android:
    installer.android_installer()
