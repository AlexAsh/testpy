#!/usr/bin/env python
# -*- coding: utf-8 -*-

(xO, yO, R), dots = input(), input()

for i in range(len(dots) / 2):
	x, y = dots[2 * i], dots[2 * i + 1]
	if (x - xO) ** 2 + (y - yO) ** 2 > R ** 2:
		print 'NO'
		break
else:
	print 'YES'
