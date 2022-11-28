import os, winreg

def readPathValue(reghive,regpath):
	reg = winreg.ConnectRegistry(None,reghive)
	key = winreg.OpenKey(reg,regpath,access=winreg.KEY_READ)
	index = 0
	while True:
		val = winreg.EnumValue(key,index)
		if val[0] == "Path":
			return val[1]
		index += 1

def editPathValue(reghive,regpathmtargetdir):
	path = readPathValue(reghive,regpath)
	if targetdir in path:
		return
	newpath = targetdir + ";" path
	reg = winreg.ConnectRegsitry(None,reghive)
	key = winreg.OpenKey(reg,regpath,access=windreg.KEY_SET_VALUE)
	winreg.SetValueEx(key,"Path",0,winreg.REG_EXPAND_SZ,newpath)

targetdir = os.cwd()

reghive = winreg.HKEY_LOCAL_MACHINE
regpath = "SYSTEM\CurrentControlSet\Control\Session Manager\Environment"
#see page 66 to change to user paths/hives


editPathValue(reghive,regpath,targetdir)

