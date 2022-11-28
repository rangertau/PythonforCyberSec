from libratom.lib.pff import PffArchive

filename = "sample.pst"
archive = PffArchive(filename)

for folder in archive.folders():
	if folder.get_number_of_sub_messages() != 0:
		print("Sender: %s" % message.get_sender_name())
		print("Subject: %s" % message.get_subject())
		print("Message: %s" % message.get_plain_text_body())


