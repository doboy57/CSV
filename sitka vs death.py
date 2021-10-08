import csv
import matplotlib.pyplot as plt
from datetime import datetime

dates_death = []
highs_death = []
lows_death = []
station_death = []
dates_sitka = []
highs_sitka = []
lows_sitka = []
station_sitka = []

open_file_sitka = open("sitka_weather_2018_simple.csv", "r")
csv_file_sitka = csv.reader(open_file_sitka, delimiter=",")
header_row_sitka = next(csv_file_sitka)
TMAX_sitka = header_row_sitka.index("TMAX")
TMIN_sitka = header_row_sitka.index("TMIN")
datesi_sitka = header_row_sitka.index("DATE")
station_s = header_row_sitka.index("NAME")
for row in csv_file_sitka:
    try:
        high_sitka = int(row[TMAX_sitka])
        low_sitka = int(row[TMIN_sitka])
        the_date_sitka = datetime.strptime(row[datesi_sitka], "%Y-%m-%d")
        station_si = str(row[station_s])
    except ValueError:
        print(f"Missing data for {the_date_sitka}")
    else:
        highs_sitka.append(high_sitka)
        lows_sitka.append(low_sitka)
        dates_sitka.append(the_date_sitka)
        station_sitka.append(station_si)

open_file_death = open("death_valley_2018_simple.csv", "r")
csv_file_death = csv.reader(open_file_death, delimiter=",")
header_row_death = next(csv_file_death)
TMAX_death = header_row_death.index("TMAX")
TMIN_death = header_row_death.index("TMIN")
date_death = header_row_death.index("DATE")
station_d = header_row_death.index("NAME")



for row in csv_file_death:
    try:
        high = int(row[TMAX_death])
        low = int(row[TMIN_death])
        the_date = datetime.strptime(row[date_death], "%Y-%m-%d")
                                     
        station = str(row[station_d])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs_death.append(high)
        lows_death.append(low)
        dates_death.append(the_date)
        station_death.append(station)
print(station_death[1])
print(station_sitka[1])

print(TMAX_death)
print(TMIN_death)
print(TMAX_sitka)
print(TMIN_sitka)


plt.subplot(2, 1, 1)
plt.plot(dates_sitka, highs_sitka, c="red")
plt.plot(dates_sitka, lows_sitka, c="blue")
plt.fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor="blue", alpha=0.1)

plt.title(station_sitka[1])

plt.subplot(2, 1, 2)
plt.plot(dates_death, highs_death, c="red")
plt.plot(dates_death, lows_death, c="blue")
plt.fill_between(dates_death, highs_death, lows_death, facecolor="blue", alpha=0.1)


plt.title(station_death[1])

plt.suptitle("Temperature comparison between "+str(station_sitka[1])+ " and "+ str(station_death[1]))
plt.show()
