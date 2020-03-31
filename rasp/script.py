
import time
import datetime
import Adafruit_ADS1x15


device = Adafruit_ADS1x15.ADS1115()


num = 0

while True:
    values = [0]*4
    for i in range(4):
        values[i] = device.read_adc(i, gain=8)

 	if values[0] > 3200:
		fo = open("writeTo.txt", "w")
 		fo.write('{}'.format(num))
        	fo.write(' {0:6}'.format(*values))
		ts = time.time()
		st = datetime.datetime.fromtimestamp(ts).strftime('%H:%M:%S')
		fo.write(' {}\n'.format(st))
                print('{}'.format(num))
                print(' {0:6}'.format(*values))
                print(' {}\n'.format(st))
        	num+=1
		fo.close()

time.sleep(0.0001)
