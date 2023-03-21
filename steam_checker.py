import requests

fname = "imported_accounts.txt"
available = "available_accounts.txt"
api_key = "your_api_key"  # replace with your Steam API key

def file_len(fname):
    with open(fname) as f:
        return sum(1 for _ in f)

def name_check():
    with open(fname, "r") as f, requests.Session() as session:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            url = f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={line}"
            response = session.get(url).json()

            if response["response"]["success"] == 42:  # 42 indicates that the custom URL is available
                print(f"{line} is available.\nexported to text file: {available}")
                with open(available, "a") as available_file:
                    available_file.write(line + "\n")
            else:
                print(f"{line} is unavailable")

def main():
    name_check()

if __name__ == "__main__":
    main()
