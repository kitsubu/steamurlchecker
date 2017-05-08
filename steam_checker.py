import urllib

fname = "imported_accounts.txt"
available = "available_accounts.txt"

def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

lines = file_len(fname)

def name_check():
    with open(fname, "r") as f:
        lines = f.readlines()
        for line in lines:
            page = urllib.urlopen("http://steamcommunity.com/id/" + line).read()
            if "The specified profile could not be found." in page:
                print(line.strip() + " is available.\nexported to text file: " + available)
                
                with open(available, "a") as f:
                    f.write(line.strip() + "\n")
                
            else:
                print(line.strip() + " is unavailable")

name_check();
