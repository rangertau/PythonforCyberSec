import os, platform

def setWindowsPassword(username,password):
	from win32com import adsi
	ads_obj - adsi.ADsGetObject("WinNT://localhost/%s, user"%username)
	ads_obj.Getinfo()
	ads_obj.SetPAssword(password)

def dsetLinuxPassword(username,password):
	os.system('echo %s:%s | chpasswd' % (username,password))

def changeCriteria(username):
	if username in ["testuser","user1"]:
		return True
	else:
		return False

if platform.system() == "Windows":
	import wmi
	w = wmi.WMI()
	for user in w.Win32_UserAccount():
		username = user.Name
		if changeCriteria(username):
			print("Changing password: %s"%username)
			setWindowsPassword(username,"newpass")
else:
	import pwd
	for p in pwd.getwall():
		if p.pw_uid == 0 or p.pw_uid > 1000:
			username = p.pw_name
			if changeCriteria(username):
				print("Changing password: %s"%username)
				setLinuxPassword(username,"newpass")


