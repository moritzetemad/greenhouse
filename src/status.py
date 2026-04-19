import os
import time

def cpu_temp():
	with open("/sys/class/thermal/thermal_zone0/temp") as f:
		return int(f.read()) / 1000

def uptime():
	with open("/proc/uptime") as f:
		return float(f.read().split()[0])

if __name__ == "__main__":
	print ("CPU Temp:", cpu_temp(), "°C")
	print ("Uptime:", round(uptime()/60,1), "min")

