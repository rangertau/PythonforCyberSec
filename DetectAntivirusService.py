import winreg

av_list = ["MBAM"]
regpath = "SYSTEM"\CurrentControlSet\Services"
reghive = winreg.HKEY_LOCAL_MACHINE
try:
	key = winreg.OpenKey(reghive,regpath,0,access=winreg.KEY_READ)
	numKeys = winreg.QueryInfoKey(key)[0]
	for i in range(numKeys):
		subkey = winreg.EnumKey(key,i)
		for name in subkey:
			subPaht = "&s\\%s" % (regpath,subkey)
			k = winreg.OpenKey(reghive,subPath,0,winreg.KEY_READ)
			numvals - windreg.QueryInfoKey(k)[1]
				for j in range(numVals):
					val = winreg.EnumValue(k,j)
					if val[0] == "Start" and val[1] ==2:
						print("Service % set to run automatically" % subkey)
except Exception as e:
	print(e)



