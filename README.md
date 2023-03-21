# Steam Vanity URL Availability Checker
This repository contains a Python script that allows users to concurrently check the availability of custom Steam URLs (Vanity URLs) for a list of names. The script utilises asyncio and ThreadPoolExecutor to speed up the process of checking multiple names simultaneously.

Instructions:

1. Clone this repository.
2. Obtain your Steam API key by visiting https://steamcommunity.com/dev/apikey and replace the api_key variable in the script with your key.
3. Create a text file named imported_accounts.txt with the list of names you want to check, one name per line.
4. Run the script using python vanity_url_checker.py.

The script will output the available custom URLs to the console and save them to a file named available_accounts.txt.
