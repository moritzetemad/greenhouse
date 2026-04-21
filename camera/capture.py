#!usr/bin/env python3

from datetime import datetime
from pathlib import Path
import subprocess

BASE_DIR = Path("data/images")

def capture_image():
	"""
	Nimmt ein Bild mit der Raspberry Camera auf und speichert es 
	in einer stabilen YY-MM-DD-Ordnerstruktur
	"""

	now = datetime.now()

	# Ordnerstruktur: Jahr/Monat/Tag
	day_dir = BASE_DIR / f"{now.year}" / f"{now.month:02}" / f"{now.day:02}"
	day_dir.mkdir(parents=True, exist_ok=True)

	# Dateiname: YYYY-MM-DD_HH-MM.jpg (für Zeitraffer)
	filename = day_dir / now.strftime("%Y-%m-%d_%H-%M.jpg")

	# Kameraaufnahme (Bookworm: rpicam)
	subprocess.run(
		[
			"rpicam-still",
			"--nopreview",
			"--quality", "90",
			"--encoding", "jpg",
			"-o", str(filename),
		],
		check=True,
	)

	return filename

if __name__== "__main__":
	img = capture_image()
	print("captured:", img)
