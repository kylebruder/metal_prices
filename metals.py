import requests
import datetime
import re
from bs4 import BeautifulSoup

def fetch_prices(url, out_file):
    """
    Fetches recent opening prices of commodities from www.investing.com.

    Sends an HTTP get request to a specified URL, parses the HTML identifying
    the table containing the data, then writes data to a csv file.

    Parameters
    ----------
    arg1 : str
        The URL of the www.investing.com page to parse
    arg2 : str
        The name of the file to which collected data will be written
    """
    # Set the HTTP headers to Ajax request
    urlheader = {
      "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
      "X-Requested-With": "XMLHttpRequest"
    }

    # Get the raw html
    req = requests.get(url, headers=urlheader)
    soup = BeautifulSoup(req.content, "lxml")

    # Select the price table
    table = soup.find('table', id="curr_table")

    # Initialize the price and date lists
    dates = []
    prices = []

    # Select the rows from the table
    rows = table.find_all('tr')[1:-1]

    # Interate over the rows
    for tr in rows:
        tds = tr.find_all('td')
        row = [elem.text for elem in tds]

        # Append the cell data to the respective list
        # Convert date format
        date = datetime.datetime.strptime(row[0], '%b %d, %Y').strftime('%Y-%m-%d')
        dates.append(date)
        # Convert price format
        price = re.sub(',', '', row[1])
        prices.append(price)

    # Open a file and write the data in CSV format
    with open(out_file, 'w') as f:
        # Write header cells to the csv file
        print('Date,Opening Price', file=f)
        for i in range(0, (len(dates) - 1) ):
            print(dates[i] + ", " + prices[i], file=f)

if __name__ == "__main__":
    # Fetch gold prices
    fetch_prices('https://www.investing.com/commodities/gold-historical-data', 'gold_prices.csv')
    # Fetch silver prices
    fetch_prices('https://www.investing.com/commodities/silver-historical-data', 'silver_prices.csv')
    # Fetch bitcoin
    fetch_prices('https://www.investing.com/crypto/bitcoin/btc-usd-historical-data', 'btc_prices.csv')
