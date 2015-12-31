import os.path
import sys
from dbr import *

formats = {
	0x3FFL: "OneD",
	0x1L  : "CODE_39",
	0x2L  : "CODE_128",
	0x4L  : "CODE_93",
	0x8L  : "CODABAR",
	0x10L : "ITF",
	0x20L : "EAN_13",
	0x40L : "EAN_8",
	0x80L : "UPC_A",
	0x100L: "UPC_E",
	0x200L: "INDUSTRIAL_25",
	0x2000000L: "PDF417",
	0x8000000L: "DATAMATRIX",
	0x4000000L: "QR_CODE"
}	
	
if __name__ == "__main__":
	license = open('license.txt', 'r')
	license_content = license.readline().strip()
	ret = initLicense(license_content)
	if (ret != 0):
		print "invalid license"
		sys.exit(0)
	
	barcode_image = raw_input("Enter the barcode file: ");
	if not os.path.isfile(barcode_image):
		print "It is not a valid file."
	else:
		
		results = decodeFile(barcode_image);
		print "Total count: " + str(len(results))
		for result in results:
			print "barcode format: " + formats[result[0]]
			print "barcode value: " + result[1] + "\n*************************"