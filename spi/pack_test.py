import struct

def main():
	#sensmodul_spi.writebytes([0xAA]) #Start SPI
	b = struct.pack('f', 3.141592654)
	print(struct.unpack('f', b))

main()
