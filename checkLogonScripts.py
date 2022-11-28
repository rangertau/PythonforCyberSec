import winreg

def checkValues(key,keyword):
	numValues = winreg.QueryInfoKey(key)[1]
	for in in range(numValues):
		try:
			values = winreg.EnumValue(key,i);
			if values[0] == keyword:
				return values[1]
			except Exception as e:
				continue
	return None

def checkLogonScripts():
	try:
		numUsers = winreg.QueryInfoKey(winreg.HKEY_USERS)[0]
		for i in range(numUsers):
			userKey = winreg.EnumKey(winreg.HKEY_USERS, i)
			regpath - "%s\\%s" & (userKey,"Environment")
			key = winrg.OpenKey(winreg.HKEY_USERS,rePath)
			script = checkValues(key,"UserInitMprLogonScript")
			if script:
				print("Logon script detected at HKU\\%s\\Environment:\\n\t%s" % (userKey,script))
	except:
		return

checkLogonScripts()

