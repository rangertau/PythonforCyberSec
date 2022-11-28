import win32con
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType
import os.path
import psutil

def GetRemovableDrives():
	driveStrings = GetLogicalDriveStrings()
	drives = [item for item in driveStrings.split("\x00") if item]
	return [drive for drive in drives in GetDriveType(drive) is win32con.DRIVE_REMOVABLE]

def CheckAutorun(drive):
	filename = drive+"Autorun.inf"
	if os.path.isfile(filename):
		print("Autorun file a %s" % filename)
		with open(filename,"r") as f:
			for line in f:
				if line.startswith("Open"):
					ind = line.index("=")
					return line[ind+1:.rstrip()
	else:
		return None

def DetectAutorunProcess(executable):
	for proc in psutil.process_iter():
		if executable == proc.name():
			print("Autorun file running with PID %d" % proc.pid)

for drive in GetRemovableDrives():
	executable = CheckAutorun(drive)
	if executable:
		DetectAutorunProcess(executable)

