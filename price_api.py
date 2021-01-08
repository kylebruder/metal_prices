import flask
import csv
import json
import pandas as pd
from flask import request, jsonify
from metals import fetch_prices
app = flask.Flask(__name__)
app.config["DEBUG"] = True


def render_json(commodity, url, csv, start, end):
    """ Read a csv file containing commodity price data and perform
    mean and variance statistics on a specified range of dates

    Keyword arguments:
    commodity   --  currently accepting 'gold' or 'silver'
    url         --  Must be a historical data page from www.investing.com
    csv         --  The name of the csv file in which to store data
    start       --  The start of the date range in iso format
    end         --  The end of the date range in iso format

    Returns:
    json_result --  prices matching the date range including mean and variance
                    statistics in JSON format
    """
    # Scrape data from specified www.investing.com page and save to a local CSV
    fetch_prices(url, csv)
    # Open the saved CSV as a file object
    with open(csv, 'r') as fo:
        # Read the CSV as a pandas dataframe
        df = pd.read_csv(fo)
        # Select the specified date range
        df = df[(df['Date'] > start) & (df['Date'] <= end)]
        # Initialize data dict
        data = {}
        # Add key value pairs from each dataframe row
        for index, row in df.iterrows():
            data[row['Date']] = row['Opening Price']
        # Initialize results dict containing data and statistics
        results = {}
        # Add data to results
        results['data'] = data
        # Add mean to results
        results['mean'] = df['Opening Price'].mean()
        # Add variance to results
        results['variance'] = df['Opening Price'].var()
        # Convert the results dict to JSON format
        json_result = json.dumps(results, indent=4)

        return json_result

@app.route('/commodity', methods=['GET'])
def return_results():
    """
    Returns data and statistics in JSON format based on HTTP GET arguments
    passed to /commodity
    """
    # Assign variables from passed arguments
    start_date = request.args.get("start_date")
    end_date = request.args.get("end_date")
    commodity_type = request.args.get("commodity_type")
    # Use render_json() to get results based on specified commodity type
    if commodity_type == 'gold':
        url = 'https://www.investing.com/commodities/gold-historical-data'
        csv = 'gold_prices.csv'
        result = render_json(commodity_type, url, csv, start_date, end_date)
        return result

    elif commodity_type == 'silver':
        url = 'https://www.investing.com/commodities/silver-historical-data'
        csv = 'silver_prices.csv'
        result = render_json(commodity_type, url, csv, start_date, end_date)
        return result
    else:
        return '''
        Enter args... example:
        commodity?start_date=2019-05-15&end_date=2019-06-07&commodity_type=gold\n
        '''

app.run(port=8080)
