import os

def generate_QR(text):
	os.system("qr " + text + " > test.png | eog test.png & disown")