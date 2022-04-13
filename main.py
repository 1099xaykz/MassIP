import time
import os
import sys
import requests, json

BLACK = '\033[1;30m'
RED = '\033[1;31m'
GREEN = '\033[1;32m'
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
MAGENTA = '\033[1;35m'
CYAN = '\033[1;36m'
WHITE = '\033[1;37m'
RESET = '\033[1;39m'

def banner():
	print(RED + """
███╗   ███╗ █████╗ ███████╗███████╗    ██╗██████╗     ███████╗ ██████╗ █████╗ ███╗   ██╗
████╗ ████║██╔══██╗██╔════╝██╔════╝    ██║██╔══██╗    ██╔════╝██╔════╝██╔══██╗████╗  ██║
██╔████╔██║███████║███████╗███████╗    ██║██████╔╝    ███████╗██║     ███████║██╔██╗ ██║
██║╚██╔╝██║██╔══██║╚════██║╚════██║    ██║██╔═══╝     ╚════██║██║     ██╔══██║██║╚██╗██║
██║ ╚═╝ ██║██║  ██║███████║███████║    ██║██║         ███████║╚██████╗██║  ██║██║ ╚████║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═╝╚═╝         ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═══╝
""")
	print(WHITE + "                 TikTok: @ds.8mqk")
	print()

def main():
	file = input(RED + "Archivo de direcciones IP" + WHITE + " > ")
	archivo = open(file, "r")
	for line in archivo:
		api = "http://ip-api.com/json/"
		try:
				print("----------------------------------------------------------------")
				print()
				data = requests.get(api+line).json()
				print("IP:", data['query'])
				print("ISP:", data['isp'])
				print("Organizacion:", data['org'])
				print("Pais:", data['country'])
				print("Ciudad:", data['city'])
				print("Region:", data['region'])
				print("Longitude:", data['lon'])
				print("Latitude:", data['lat'])
				print("Zona horaria:", data['timezone'])
				print("Codigo postal:", data['zip'])
				print()
				print("----------------------------------------------------------------")
		except requests.exceptions.ConnectionError as e:
			print("No hay conexion a internet")

if __name__ == '__main__':
	main()
