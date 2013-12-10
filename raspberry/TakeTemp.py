tfile = open("/sys/bus/w1/devices/28-000004631ea4/w1_slave")
text = t.file.read()
tfile.close()
secondline = text.split("\n")[1]
temperaturedata = secondline.split(" ")[9]
temperature = float(temperaturedata[2:])
temperature = temperature / 1000
print temperature
