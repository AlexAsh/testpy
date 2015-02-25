#!/usr/bin/env python
# -*- coding: utf-8 -*-

userList = list(input())
max1 = max2 = userList[0]

for num in userList[1:]:
	if max1 < num:
		max1, max2 = num, max1
	elif num < max1 == max2 or max2 < num < max1:
		max2 = num

print max2 if max1 > max2 else 'NO'	
