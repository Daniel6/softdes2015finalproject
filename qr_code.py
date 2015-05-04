import os

def generate_QRCode(text):
	"""Generate QR Code from a string"""
	os.system("qr " + text + " > qr_code.png | eog qr_code.png &")

if __name__ == "__main__":
	generate_QRCode("www.google.com")
