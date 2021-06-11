from datetime import datetime
import random
from datetime import timedelta

min_year=1901
max_year=2021

start = datetime(min_year, 1, 1)
years = max_year - min_year+1
end = timedelta(days=365 * years)

random_date = [(start + (end) * random.random()).strftime("%b, %dth, %Y") for i in range(26)]
print(str(random_date))
print(datetime.now())