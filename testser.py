import time
import serial

arduino = serial.Serial('COM4', 9600, timeout=.1)
while True:
	data = arduino.readline().rstrip().decode() #the last bit gets rid of the new-line chars
	print (data)