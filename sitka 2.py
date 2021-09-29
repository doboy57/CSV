import csv 
import matplotlib.pyplot as plt
from datetime import datetime
open_file = open("sitka_weather_07-2018_simple.csv", 'r')
csv_file = csv.reader(open_file, delimiter=',')

header_row = next(csv_file)
print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)
mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
print(mydate)
dates = []
highs = []
for row in csv_file:
    highs.append(int(row[5]))
    the_date = datetime.strptime(row[2], '%Y-%m-%d')
    dates.append(the_date)


print(dates)
print(highs)

fig = plt.figure()


plt.title("Daily high temps july 2018",fontsize=16)
plt.xlabel("",fontsize=16)
plt.ylabel("Temperature(f)", fontsize=16)
plt.tick_params(axis="both",which="major" ,labelsize=16)

plt.plot(dates, highs, c="red")

fig.autofmt_xdate()

plt.show()
