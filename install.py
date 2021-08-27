import os
import time

print("whats is os? [1]Debian [2] Termux")
user_a = int(input("==> "))
if user_a == 1:
	os.system("sudo apt -y update")
	os.system("pip3 install colorama")
	os.system("pip3 install gitpython")
	print("Instalacion completada!!!")
	time.sleep(0.3)
	os.system("python3 CyTools.py")
elif user_a == 2:
	os.system("apt -y update")
	os.system("pip3 install gitpython")
	os.system("pip3 install colorama")
	print("instalacion completada: ")
	os.system("python3 CyTools.py")
else:
	while True:
		print("ERROR-ERROR-ERROR-ERROR-ERROR")

