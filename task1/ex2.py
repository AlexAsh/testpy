#!/usr/bin/env python
# -*- coding: utf-8 -*-

for field in dir(input()):
	if not field.startswith('_'):
		print field

