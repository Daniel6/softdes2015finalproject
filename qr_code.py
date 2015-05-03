import sys
sys.path.insert(1, './lib/qrcode-5.1')
import qrcode

def generate_QRCode(text):
	#Generate QR code and Display it
	img = qrcode.make(text)
	img.show()

if __name__ == "__main__":
	generate_QRCode("www.google.com")