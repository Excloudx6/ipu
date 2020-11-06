import requests as req 
import argparse
import socket
from urllib.parse import urlparse
from termcolor import colored

__author__ = '4N7U'


print("")
print(colored(" 	 _______       ",'green'))
print(colored(" 	(_) ___ \      ",'green'))
print(colored(" 	 _| |_/ /   _  ",'green'))
print(colored(" 	| |  __/ | | | ",'green'))
print(colored(" 	| | |  | |_| | ",'green'))
print(colored(" 	|_\_|   \__,_| ",'green'))
               
print("") 
print(colored(" # Develop by ArMan HoSSa!n     ", 'yellow'))
print(colored(" # Twitter: @0xAntu        ", 'yellow'))
print(colored(" # Get IP address from Domain Name	    ", 'yellow'))               
print("")
parser = argparse.ArgumentParser()
parser.add_argument('-u', help='Target url', dest='url')
parser.add_argument('-f', help='URLs File', dest='url_file')
parser.add_argument('-o', help='Save the results to text file', dest='output_file')
args = parser.parse_args()

url = args.url
url_file = args.url_file
output_file = args.output_file

urls=[]

if url:
	try:
		ip = socket.gethostbyname(url)
		print(" [+]",url + "'s IP Address is ==> ", ip)
		if output_file:
			with open(output_file, 'a') as out:
				out.write(ip+"\n")
	except ConnectionError:
		pass

if url_file:
	file = open(url_file, "r")
	for line in file:
		url = line.strip() 
		try:
			ip = socket.gethostbyname(url)
			print(" [+]",url + "'s IP Address is ==> ", ip)
			if output_file:
				with open(output_file, 'a') as out:
					out.write(ip+"\n")
		except ConnectionError:
			pass


print(" ")
print(colored(" # CopyRight @ 0xAntu", 'yellow'))
print(" ")
