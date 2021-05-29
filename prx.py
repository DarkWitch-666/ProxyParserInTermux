import requests
import os
import time
from bs4 import BeautifulSoup as BS
import urllib
import json

proxy_parser = 'https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=1000&country=all&anonymity=elite&ssl=yes'

RED, WHITE, CYAN, GREEN, DEFAULT, CYANCLARO, BOLD = '\033[91m', '\033[46m', '\033[36m', '\033[1;32m',  '\033[0m', '\033[1;36m', '\033[1m'

def get_html(url):
	return requests.get(url).text

def parse_ua(tutilka):
	soup = BS(tutilka, 'html.parser')
	for date in soup.findAll('td'):
		content = date.getText().split('  ')
		for g in content:
			if g == '':
				pass
			elif '\n' in g:
				g = g.replace("\n", "")
			else:
				print(f'{CYAN}[{RED}*{CYAN}] {GREEN}'+g)

print(f'''{BOLD}\033[35m    

██████╗░██████╗░░█████╗░██╗░░██╗██╗░░░██╗
██╔══██╗██╔══██╗██╔══██╗╚██╗██╔╝╚██╗░██╔╝
██████╔╝██████╔╝██║░░██║░╚███╔╝░░╚████╔╝░
██╔═══╝░██╔══██╗██║░░██║░██╔██╗░░░╚██╔╝░░
██║░░░░░██║░░██║╚█████╔╝██╔╝╚██╗░░░██║░░░
╚═╝░░░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░

{RED}PROXY PARSER (IN TERMUX)

{GREEN}[coded by @DarkUserWitch]\n[channel: t.me/termux_hack_xr]
''')
print(f"{RED}1 - proxy parsing\nctrl + c - exit")

while True:
	shell = input(f'{CYAN}[{RED}•~•{CYAN}] Proxy@007: {GREEN}')
	if shell == '1':
		res1 = requests.get(proxy_parser)
		print(f'\n{CYAN}[{RED}-_-{CYAN}] Your proxy:\n\n' + '\n'.join(res1.text.split('\r\n')))
	shell = input(f'{CYAN}[{RED}^_^{CYAN}] Proxy@007: {GREEN}')