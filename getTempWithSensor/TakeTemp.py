print "----  Get Temperature with sensor ----"
print "autor: Pawel Grygorowicz"
print "ver 1.0"
print "--------------------------------------"

#sensor = ("/sys/bus/w1/devices/28-000004631ea4/w1_slave")

def getTempWithSensor(sensor):

	file  = open(sensor)
	data = file.read()
	file.close()
	secondline = data.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	print "Temperatura: "	
	print temperature


if __name__ == "__main__":
	sensor = "/sys/bus/w1/devices/28-000004631ea4/w1_slave"
	getTempWithSensor(sensor)

