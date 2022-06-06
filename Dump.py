
import platform
import os
os.system('termux-setup-storage')


arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("Jm")._login()
elif 'aarch' in arc:
	__import__("dm")._login()
else:
	exit(f' Unknow device machine {arc}')












