import asyncio
from concurrent.futures import ThreadPoolExecutor
import requests

fname = "imported_accounts.txt"
available = "available_accounts.txt"
api_key = "your_api_key"  # replace with your Steam API key

def file_len(fname):
    with open(fname) as f:
        return sum(1 for _ in f)

def name_check(line):
    with requests.Session() as session:
        url = f"http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key={api_key}&vanityurl={line}"
        response = session.get(url).json()

        if response["response"]["success"] == 42:  # 42 indicates that the custom URL is available
            with open(available, "a") as available_file:
                available_file.write(line + "\n")
            return line
        else:
            return None

async def main():
    with open(fname, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    print("checking names...\n")
    with ThreadPoolExecutor() as executor:
        tasks = [loop.run_in_executor(executor, name_check, line) for line in lines]
        results = await asyncio.gather(*tasks)

    available_names = [name for name in results if name]
    print("available names:")
    for name in available_names:
        print(name)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
