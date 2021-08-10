import requests
import json
from datetime import datetime, timedelta, date


# data ready from 2016-12-02
# start_date = datetime.date(2016, 12, 2)
# end_date = datetime.today()

def daterange(start_date, end_date):
    # The size of each step in days
    day_delta = timedelta(days=1) # <class 'datetime.timedelta'>
    end_date_adjusted = end_date + day_delta # <class 'datetime.date'>
    for n in range(int ((end_date_adjusted - start_date).days)):
        yield start_date + timedelta(n)

start_date = date(2021, 8, 7) # <class 'datetime.date'>
end_date = datetime.today().date() # <class 'datetime.date'>

for single_date in daterange(start_date, end_date):
    # print(single_date.strftime("%Y-%m-%d"))
    # print(type(single_date.strftime("%Y-%m-%d")))

    date = single_date.strftime("%Y-%m-%d")







url = 'https://api.data.gov.sg/v1/environment/rainfall'
param = {'date':date}

r = requests.get(url, params=param)
# print(r.url) - confirmed to be https://api.data.gov.sg/v1/environment/rainfall?date=2017-01-01

if r.status_code == requests.codes.ok:
    print(json.dumps(r.json(), indent=2, sort_keys=True))

else:
    print("got error")

# actual URL: https://api.data.gov.sg/v1/environment/rainfall
# data ready from 2016-12-02