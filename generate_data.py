import random 
import pandas as pd
import datetime
# import radar 
import yfinance as yf

# Generate random datetime (parsing dates from str values)
def generate_date():
    radar.random_datetime(start='2000-05-24', stop='2013-05-24')

    # Generate random datetime from datetime.datetime values
    radar.random_datetime(
        start = datetime.datetime(year=2000, month=5, day=24),
        stop = datetime.datetime(year=2013, month=5, day=24)
    )

    # Just render some random datetime. If no range is given, start defaults to 
    # 1970-01-01 and stop defaults to datetime.datetime.now()
    datetime_today = radar.random_datetime()
    date_today = datetime_today.strftime('%d')
    month = datetime_today.strftime('%m')
    year = datetime_today.strftime('%Y')
    return f"{date_today}/{month}/{year}"

    crops = ['milk', 'sugar', 'cocoa', 'coffee', 'cotton']
    prices = [random.randint(1000, 2000) for i in range(10000)]
    region = ['Europe', 'China', 'United States', 'UAE', 'Mexico', 'Canada']
    region_choices = [random.choice(region) for x in range(10000)]
    items = [random.choice(crops) for x in range(10000)]
    transaction_date = [generate_date() for x in range(10000)]
    data = {'crop' : items, 'date' : transaction_date, 'region': region_choices, 'prices': prices}

    data_frame = pd.DataFrame(data)
    data_to_excel = pd.ExcelWriter('Data.xlsx')
    data_frame.to_excel(data_to_excel)
    data_to_excel.save()
    # data_frame.to_excel('data.xlsx')
    print(data_frame)

def get_data():
    pass

def get_data():
    df_yahoo = yf.download('TME',
    start='2010-09-15',
    end='2022-04-11',
    progress=False)
    data_to_excel = pd.ExcelWriter('datasets/Tencent Music.xlsx')
    df_yahoo.to_excel(data_to_excel)
    data_to_excel.save()

def get_financial_data():
    microsoft = yf.Ticker("MSFT")
    google = yf.Ticker("GOOG")
    aapl = yf.Ticker("AAPL")
    amazon = yf.Ticker("AMZN")
    bac = yf.Ticker("BAC")
    jpm = yf.Ticker("JPM")
    credit_suise = yf.Ticker("CS")
    pfizer = yf.Ticker("PFE")
    netflix = yf.Ticker("NFLX")

    instruments = [microsoft, google, aapl, amazon, bac, jpm, credit_suise, pfizer, netflix]

    for stock in instruments:
        stock.cashflow.to_csv(f"datasets/{stock.get_info()['shortName']}_cashflows.csv")
        stock.balance_sheet.to_csv(f"datasets/{stock.get_info()['shortName']}_balancesheet.csv")
        stock.earnings.to_csv(f"datasets/{stock.get_info()['shortName']}_earnings.csv")
        stock.history(period="5y").to_csv(f"datasets/{stock.get_info()['shortName']}_data.csv")
    print("Fetch completed...")


boeing = yf.Ticker("BA")
boeing.cashflow.to_csv(f"datasets/{boeing.get_info()['shortName']}_cashflows.csv")
boeing.balance_sheet.to_csv(f"datasets/{boeing.get_info()['shortName']}_balancesheet.csv")
boeing.earnings.to_csv(f"datasets/{boeing.get_info()['shortName']}_earnings.csv")
boeing.history(period="5y").to_csv(f"datasets/{boeing.get_info()['shortName']}_data.csv")
