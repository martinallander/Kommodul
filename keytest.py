import time
import keyboard
import spidev

styrmodul_spi = spidev.SpiDev()
styrmodul_spi.open(0, 1)
styrmodul_spi.max_speed_hz = 10000

def main():
    while True:
	response = styrmodul_spi.readbytes(1)
	if response == 0xD0:
		time.sleep(0.01)
        if keyboard.is_pressed('up'):
		styrmodul_spi.writebytes([0x01])
		print("up")
        elif keyboard.is_pressed('down'):
		styrmodul_spi.writebytes([0x02])
		print("down")
	elif keyboard.is_pressed('left'):
		styrmodul_spi.writebytes([0x03])
		print('left')
	elif keyboard.is_pressed('right'):
		styrmodul_spi.writebytes([0x04])
		print('right')
        time.sleep(0.01)

main()

