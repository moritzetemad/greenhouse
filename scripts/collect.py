from datetime import datetime
from pathlib import Path
import json

from camera.capture import capture_image
from sensors.bme280 import read as read_bme280
from sensors.bh1750 import read as read_bh1750

DATA_DIR = Path("data/measurements")

def collect():
	now = datetime.now().isoformat(timespec="seconds")

	#Sensoren lesen
	bme = read_bme280()
	light = read_bh1750()

	#Bild aufnehmen 
	image_path = capture_image()

	record = {
		"timestamp": now,
		**bme,
		**light,
		"image": str(image_path),
	}

	DATA_DIR.mkdir(parents=True, exist_ok=True)
	logfile = DATA_DIR / f"{now[:10]}.json1"

	with open(logfile, "a") as f:
		f.write(json.dumps(record) + "/n")

	print("collected:", record)

if __name__ == "__main__":
	collect()
