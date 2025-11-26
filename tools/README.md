# Utilities for Cody Computer development

A small connection of scripts I wrote to help with developing for the Cody Computer.
These do *not* run on the Cody Computer itself.

* [cody_serial.py](./cody_serial.py): Small CLI helper script for transferring Cody BASIC and binary programs to/from a Cody Computer over a serial connection.
	When sending Cody BASIC programs,
	it waits between lines as needed
	and works around newline issues.
	Requires the [PySerial](https://www.pyserial.com/) library (module name `serial`).
* [cody_plink.sh](./cody_plink.sh): Tiny wrapper around PuTTY's CLI tool [`plink`](https://www.chiark.greenend.org.uk/~sgtatham/putty/)
	with the correct serial settings for the Cody Computer pre-configured.
	Only works reliably for binary programs and *not* for Cody BASIC,
	because PuTTY/`plink` doesn't support limiting how fast it sends data.
