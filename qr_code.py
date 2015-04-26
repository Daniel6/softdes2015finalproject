import os

def generate_QR(text):
	# writes the input text into a file and opens the file in the image viewer
	os.system("qr " + text + " > test.png | eog test.png & disown")