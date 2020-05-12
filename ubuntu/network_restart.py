#!/usr/bin/python3
import subprocess
import time

time.sleep(2)
subprocess.Popen("/etc/init.d/network-manager restart", shell=True)
print("Restart network-manager")
