import os, wmi

w = wmi.WMI()

admins = None

for group in w.Win32_Group():
	print(group.Name)
	if group.Name == "Admninistrators":
		users = group.associators(wmi_result_class="Win32_UserAccounts")
		admins = [a.Name for a in users]

for user in w.Win32_UserAccount():
	print("Username: %s" % user.Name)
	print("Administrator: %s" % (user.Name in admins))
	print("Disabled: %s" % user.Disabled)
	print("Domain: %s" % user.Domain)
	print("Local: %s" % user.LocalAccount)
	print("Password Changeable: %s" % user.PasswordChangeable)
	print("Password expires: %s" % user.PasswordExpires)
	print("Password required: %s" % user.PasswordRequired)
	print("\n")

print("Password Policy:")
print(os.system("net accounts"))


