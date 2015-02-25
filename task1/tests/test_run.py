#!/usr/bin/env python
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import os
import json

testFiles = [testFile for testFile in os.listdir('.') if testFile.endswith('.json')]

for testFile in testFiles:
	with open(testFile, 'r') as f:
		testData = json.load(f)
		ex = Popen(testData["ex"], stdin = PIPE, stdout = PIPE)
		output = ex.communicate(testData['input'])[0]
		print '.' if output == testData['output'] else 'F',

