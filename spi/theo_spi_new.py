import spidev 					#Fardigt framework for SPI-kommunikation
import time					#Framework for att kunna anvanda sleep
import RPi.GPIO as GPIO				#Framework for att kunma koppla GPIO-pinnarna till events
#import keyboard

sensmodul_spi = spidev.SpiDev()			#Initiera SPI for sensormodulen
sensmodul_spi.open(0, 0)			#Lat sensormodulen styras av CS0 enligt kopplingschemat
sensmodul_spi.max_speed_hz = 100000		#Satt max-overforingsfrekvens till 2000000Hz, fungerar bra vi denna hastighet
    

styrmodul_spi = spidev.SpiDev()			#Initiera SPI for Styrmodulen
styrmodul_spi.open(0, 1)			#Styrmodulen styrs av CS1 enligt kopplingschemat
styrmodul_spi.max_speed_hz = 100000

to_send = [0x01, 0x02, 0x03]			#Godtycklig lista for Bytes att skicka vid olika tester

print('Please wait.. \n .... \n ......... \n')

def gpio_setup():				#Lamplig init for att kunna koppla in t.ex. skjutomkopplaren/led till RPi
    GPIO.setmode(GPIO.BCM)			#Anvander BCM-mode for detta (Istallet for BOARD)
    GPIO.setup(4, GPIO.IN)			#GPIO4 enligt BCM ar motsvarande GPIO7 enligt BOARD. Koppla in Skjutomkopplaren har

#mode = 0b00, 0b01, 0b10, 0b11
def set_mode(module, mode_id):			#Det ar mojligt att valja hur dataovering ska ske med olika moder enligt vilken flank
    module.mode = mode_id			#detta sker enligt klockan. 0b00 ar vanligast. Notera att om en annan mod ska anvandas maste det
						#ocksa andras for modulerna. Se datablad for ATMEGA1284p. 0b00 ar standard.

def write_sensmodul(input):			#Godtycklig write-funktion, anvander ej denna for tillfallet.
    msb = input >> 8
    lsb = input & 0xFF
    sensmodul_spi.xfer([msb, lsb])		#Med xfer sa skiftar man bytes. Andra alternativ ar write och read som endast skriver 
						#och laser
def write_styrmodul(input):			#Godtycklig write-funktion, anvander ej denna for tillfallet.
    msb = input >> 8
    lsb = input & 0xFF
    styrmodul_spi.xfer([msb, lsb])
    
def test_data_sens():				#Testfunktion for sensormodulen (CS0)
	sensmodul_spi.writebytes([0x01])	#Forst skrivs 0xAA over SPI-bussen. Handskakning: Ingen skiftning sker alltsa, inget sparas.
	resp = sensmodul_spi.readbytes(1)	#En ytterligare SPI-overforing sker, nu sparas det som skickas fran slaven. totalt 1B
	if (resp[0] == 0x10):
		print('success')		#Om forvantat varde aterges vid lasning printas "success" annars "fail"
	elif (resp[0] == 0x11):
                                print('success')
	else:
		print('fail ')
		print(resp)
	time.sleep(1)
	sensmodul_spi.writebytes([0x05])	#Testar med att skicka lite olika varden
	resp = sensmodul_spi.readbytes(1)
	if (resp[0] == 0x02):
		print('success')
	else:
		print('fail ')
		print(resp)
	time.sleep(1)
	sensmodul_spi.writebytes([0x0F])
	resp = sensmodul_spi.readbytes(1)
	if (resp[0] == 0x03):
		print('success')
	else:
		print('fail ')
		print(resp)
	time.sleep(1)
				
def test_data_styr():				#Testfunktion for Styrmodulen (CS1)
	styrmodul_spi.writebytes([0xAA])
	resp = styrmodul_spi.readbytes(1)
	if (resp[0] == 0x01):
		print('success')
	else:
		print('fail ')
		print(resp)
	time.sleep(2)
	styrmodul_spi.writebytes([0x05])
	resp = styrmodul_spi.readbytes(1)
	if (resp[0] == 0x02):
		print('success')
	else:
		print('fail ')
		print(resp)
	time.sleep(1)

def main(input_data):				#Generell testfunktion for olika SPI-kommandon
    set_mode(sensmodul_spi, 0b00)		#Satter SPI-mode till 0b00
    set_mode(styrmodul_spi, 0b00)
    try:
	while True:
            print('Please select the use of the program by writing SPITEST or ROBOTTEST or CONTROL')
            inp = raw_input().lower()		#oppnar prompt for anvandaren. Konverterar allt till sma versaler.
            if inp == 'spitest':		#Generellt SPI-test
                while True:
		    print('Please select module to test by writing SENSORMODUL or STYRMODUL')
		    inp = raw_input().lower()
		    if inp == 'sensormodul':
			test_data_sens()
		    elif inp == 'styrmodul':
			test_data_styr()
		    elif inp == 'end':
                        break
		    else:
			print('wrong input')
		    time.sleep(0.5)
	    elif inp == 'robottest':		#Generellt SPI-test for styrmodulen och robotrorelser
		while True:
		    print('Please select robot movement by writing EXTEND or CONSTRICT')
		    inp = raw_input().lower()
		    if inp == 'extend':
			styrmodul_spi.writebytes([0x15])
		    elif inp == 'constrict':
			styrmodul_spi.writebytes([0x10])
		    elif inp == 'end':
                        break
		    else:
			print('wrong input')
		    time.sleep(0.5)
	    elif inp == 'control':		#Specifikt SPI-test for styrmodulen dar anvandaren far manuellt satta servovinklar.
                print('WARNING!! This setting is only for advanced users xD') #Utfor testet med restriktivitet, vinklar omkring 150.
                time.sleep(1)
                print('Are you sure you wish to continue? y n')
                inp = raw_input().lower()
                if inp == 'y':
                    while True:
                        styrmodul_spi.writebytes([0x06])
                        print('please insert an angle for servo 6')
                        inp1 = input()
                        styrmodul_spi.writebytes([inp1])
                        print('please insert an angle for servo 7')
                        styrmodul_spi.writebytes([0x07])
                        inp2 = input()
                        styrmodul_spi.writebytes([inp2])
                        print('please insert an angle for servo 8')
                        styrmodul_spi.writebytes([0x08])
                        inp3 = input()
                        styrmodul_spi.writebytes([inp3])
                        break
                else:
                    break
    except KeyboardInterrupt:			#Avslutar programmet vid ctrl-C i terminalen
        styrmodul_spi.close()			#Stanger SPI-kommunikationen
        sensmodul_spi.close()
        print('\n\n...........interrupted..............!\n\n')
        print('See you soon! ...')

def lol():					#Testfunktion for skjutomkopplaren
	while True:
		time.sleep(1)
		GPIO.wait_for_edge(4, GPIO.RISING)
		print('on')
		GPIO.wait_for_edge(4, GPIO.FALLING)
		print('off')
		        
main(to_send)					#Kor main-testet. Notera att to_send aldrig anvands i denna versionen.





#Kolla sida 167 i atmega databladet for clockfas/polaritet
