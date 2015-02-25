#!/usr/bin/env python
# -*- coding: utf-8 -*-

x1, y1, x2, y2, x3, y3, x4, y4 = input()
print 'YES' if abs((y1 - y2) / (x1 - x2)) == abs((y3 - y4) / (x3 - x4)) else 'NO'
