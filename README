# Metal Price Web Scraper

## Motivation

This is an example to show how to use BeauitfulSoup to scrape data from a webpage. Of course, websites may change over time so any code that uses web scraping is more subject to rot than usual.

## Dependencies

You must have support for LXML

Ubuntu 20
```
$ sudo apt install python3-lxml
```

## Download the code
```
$ git clone https://github.com/kylebruder/metal_prices.git
cd metal_prices
```

The example page being scraped only goes back a couple of weeks, so the date matching will only work for date ranges that fall with in that period. This is for demonstration purposes only.

## Pull Prices Into a CSV File
```
$ python metals.py
$ cat gold_prices.csv
Date,Opening Price
2021-01-08, 1840.80
2021-01-07, 1913.60
2021-01-06, 1908.60
2021-01-05, 1954.40
2021-01-04, 1946.60
2021-01-01, 1901.60
2020-12-31, 1895.10
2020-12-30, 1893.40
2020-12-29, 1882.90
2020-12-28, 1880.40
2020-12-24, 1883.20
2020-12-23, 1878.10
2020-12-22, 1870.30
2020-12-21, 1882.80
2020-12-18, 1888.90
2020-12-17, 1890.40
2020-12-16, 1859.10
2020-12-15, 1855.30
2020-12-14, 1832.10
2020-12-11, 1843.60
2020-12-10, 1837.40
```

## Running the Price API

### Open a new terminal and run the flask script
```
$ python price_api.py
 * Serving Flask app "price_api" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)
...
```

### Test with curl
```
# Note: change the end date to something recent from the last 2 weeks 
# or the API will return an empty set.
$ curl 'http://localhost:8080/commodity?start_date=2020-05-15&end_date=2021-01-07&commodity_type=silver'
{
    "data": {
        "2021-01-07": 27.261,
        "2021-01-06": 27.042,
        "2021-01-05": 27.64,
        "2021-01-04": 27.364,
        "2021-01-03": 27.008,
        "2021-01-01": 26.525,
        "2020-12-31": 26.412,
        "2020-12-30": 26.573,
        "2020-12-29": 26.217,
        "2020-12-28": 26.539,
        "2020-12-27": 26.295,
        "2020-12-24": 25.908,
        "2020-12-23": 25.921,
        "2020-12-22": 25.535,
        "2020-12-21": 26.379,
        "2020-12-20": 26.015,
        "2020-12-18": 26.033,
        "2020-12-17": 26.181,
        "2020-12-16": 25.052,
        "2020-12-15": 24.644,
        "2020-12-14": 24.047,
        "2020-12-13": 24.073,
        "2020-12-11": 24.092,
        "2020-12-10": 24.094
    },
    "mean": 25.95208333333333,
    "variance": 1.1883564275362322
}
```
