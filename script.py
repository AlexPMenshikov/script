#!/usr/bin/python
import sys
import os
import subprocess
import time

restart_count = 0
choise = 0

while choise <= 1:
	if subprocess.call('ping -w 5 -c 3 yandex.ru',shell=True) == 0:
		print "Everything OK, restarting: ",restart_count
		time.sleep(10)
	else:
		subprocess.call('/etc/init.d/networking restart',shell=True)
		restart_count += 1
		print "Networking restart: ",restart_count