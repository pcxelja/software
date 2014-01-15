import datetime
print "----  Get Temperature with sensor ----"
print "autor: Pawel Grygorowicz"
print "ver 1.2"
print "--------------------------------------"
def getTempWithSensor(sensor, fileTxt):
	file  = open(sensor)
	data = file.read()
	file.close()
	secondline = data.split("\n")[1]
	temperaturedata = secondline.split(" ")[9]
	temperature = float(temperaturedata[2:])
	temperature = temperature / 1000
	print "Temperatura: "
	print temperature
	#return temperature
	fileTxt = open(fileTxt, 'a')
	fileTxt.write(" ")
	fileTxt.write(str(temperature))
	fileTxt.close()

def writeToFile(file, data):
	file = open(file, 'a')
	file.write(data)
	file.write(" ")
	file.close()

date = str(datetime.datetime.now())


if __name__ == "__main__":

	writeToFile(file = "date.txt", data = date)

	w1 = "/sys/bus/w1/devices/28-000004631ea4/w1_slave"
	getTempWithSensor(sensor = w1, fileTxt = "w1.txt")
	#writeToFile(file = "w1.txt", data = temperature)

	w2 = "/sys/bus/w1/devices/28-000004b20553/w1_slave"
	getTempWithSensor(sensor = w2, fileTxt = "w2.txt")
	#writeToFile(file = "w2.txt", data = temperature)

