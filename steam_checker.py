import requests

fname = "imported_accounts.txt"
available = "available_accounts.txt"

def file_len(fname):
	with open(fname) as f:
		i = 0
		for i, l in enumerate(f):
			pass
	return i + 1

lines = file_len(fname)

def name_check():
	f = open(fname)
	lines = f.readlines()
	
	with open(fname, "r") as f:
		lines = f.readlines()
		for line in lines:
			page = requests.get("http://steamcommunity.com/id/{}".format(line)).text
			if "The specified profile could not be found." in page:
				print("{} is available.\nexported to text file: {}".format(line.strip(), available))
				
				with open(available, "a") as f:
					f.write(line)
				
			else:
				print("{} is unavailable".format(line.strip()))

name_check()
