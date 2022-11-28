from scapy.all import *

def printData(x):
	d = chr(x[ICMP].code)
	print (d,ends="",flush = True)

sniff(filter="icmp",prn=printData)


