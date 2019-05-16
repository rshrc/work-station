import station_parser
from winstaller.utils import UbuntuInstaller, ArchInstaller
from gui_installer.gui_start import InstallerGUI

args = station_parser.get_station_parser()

if args.ubuntu:
    installer = UbuntuInstaller()
if args.arch:
    installer = ArchInstaller()

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

if args.gui:
    ins_gui = InstallerGUI()
    ins_gui.define_gui()

