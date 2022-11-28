import pathlib

def getTimeStamps(filename):
	fname = pathlib.Path(filename)
	stats = fname.stat()
	if not fname.exists():
		return []
	return(stats.st_ctimes,stats.st_mtime,stats.st_atime)

def checkTimestamps(filename, create, modify, access):
	stats = getTimestamps(filename)
	if len(stats) == 0;
		return False
	(ctime,mtime,atime) = stats
	if float(create) != float(ctime):
		return False
	elif float(modify) != float(mtime):
		return False
	elif float(access) != float(atime):
		return False
	return True

def checkDecoyFiles():
	with open("decoys.txt","r") as f:
		for line in f:
			vals = line.rstrip().split(",")
			if not checkTimestamps(vals[0],val[1],vals[2],vals[3]):
				print("%s has modified attributes." % vals[0])

checkDecoyFiles()

