# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2025 dgelessus
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Step by step conversion of a Mandelbrot set visualization to use only integer arithmetic.

This was the prototype for mandelbrot.bas.
"""

import math

chars = "01#&%*+<^-!;:,'."

def mandelbrot0():
	##for iy in range(-20, 20):
	for iy in range(-35, 35):
		##for ix in range(-60, 20):
		for ix in range(-120, 40):
			c = ix/50 + iy/50*2j
			z = 0
			for v in range(len(chars)):
				z = z**2 + c
				if abs(z) > 10:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot1():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			c = ix/100 + iy/100*1j
			z = 0
			for v in range(len(chars)):
				z = z**2 + c
				if abs(z) > 10:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot2():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			cx = ix/100
			cy = iy/100
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = zx**2 - zy**2 + cx, 2*zx*zy + cy
				if math.sqrt(zx**2 + zy**2) > 10:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot3():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			cx = ix/100
			cy = iy/100
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = zx**2 - zy**2 + cx, 2*zx*zy + cy
				if zx**2 + zy**2 > 100:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot4():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = (zx/100)**2*100 - (zy/100)**2*100 + ix, 2*(zx/100)*(zy/100)*100 + iy
				if (zx/100)**2 + (zy/100)**2 > 100:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot5():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = zx*zx/100 - zy*zy/100 + ix, 2*zx*zy/100 + iy
				if zx*zx + zy*zy > 1000000:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot6():
	for iy in range(-140, 140, 4):
		for ix in range(-240, 80, 2):
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = zx*zx//100 - zy*zy//100 + ix, 2*zx*zy//100 + iy
				if zx*zx + zy*zy > 1000000:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

def mandelbrot7():
	##for iy in range(-140, 140, 4):
	for iy in range(-80, 80, 8):
		##for ix in range(-240, 80, 2):
		for ix in range(-240, 72, 8):
			zx = 0
			zy = 0
			for v in range(len(chars)):
				zx, zy = zx*zx//100 - zy*zy//100 + ix, 2*zx*zy//100 + iy
				if zx*zx/1000 + zy*zy/1000 > 1000:
					print(chars[v % len(chars)], end="")
					break
			else:
				print(" ", end="")
		
		print()

if __name__ == "__main__":
	mandelbrot7()
