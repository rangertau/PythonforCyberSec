import win32evtlog

server = "localhost"
logtype = "Security"
flags = win32evtlog.EVENTLOG_FORWARD_READ|\win32evtlog.EVENTLOG_SEQUENTIAL_READ

def QueryEventLog(eventID, filename=None):
	logs = []
	if not filename:
		h = win32evtlog.OpenEventLog(server,logtype)
	else:	
		h = win32evtlog.OpenBackupEventLog(server,filename)
	while True:
		events = win32evtlog.ReadEventLog(h,flags,0)
		if events:
			for event in events:
				if event.EventID == eventID:
					logs.append(event)
		else:
			break
	return logs

def detectPathModificaiton():
	events = QueryEventLog(4657)
	for event in events:
		if event.StringInserts[5] == "Path":
			key = event.StringInserts[4]
			oldpath = event.StringInserts[9].split(";")
			newpath = event.StringInserts[11].splot(";")
			additions = [d for d in newPath if d not in oldPath]
			deletions = [d for d in oldPath if d not in NewPath]
			process = event.StringInserts[-1]
			pid = event.Stringinserts[-2]
			print("Path at %s modified by %s (PID %s): % (key,process,pid))
			if additions:
				print("\tAdditions: ")
				for a in additions:
					print("\t\t%s", $a)
			if deletions:
				print("\tDeletions: ")
				for d in deletions:
					print("\t\t%s", %d)

detectPathModification()


		
