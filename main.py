import csv
from datetime import datetime
import matplotlib.pyplot as plt

overall_records = 0
used_records = 0


def read_and_filter_csv(cv_reader, my_streets_link):
    route_to_home = ['701', '104', '106', '107',
                     '108', '109', '110', '111',
                     '112', '113', '114', '115',
                     '116', '117', '118']
    records_counter = 0
    for row in cv_reader:
        records_counter += 1
        if row[0][6:-3] in route_to_home:
            row[0] = row[0][6:-3]
            row[1] = datetime.strptime(row[1], '%d.%m.%Y %H:%M:%S')
            my_streets_link.append(row)

    global overall_records
    overall_records += records_counter
    return my_streets_link


def read_and_count_by_hours(filename1, filename2):
    with open(filename1) as cv1:
        with open(filename2) as cv2:
            cv_reader1 = csv.reader(cv1, delimiter=';')
            cv_reader2 = csv.reader(cv2, delimiter=';')
            my_route = []
            my_route = read_and_filter_csv(cv_reader1, my_route)
            my_route = read_and_filter_csv(cv_reader2, my_route)
            global used_records
            used_records += len(my_route)

            sorted_by_day = my_route.copy()
            sorted_by_day.sort(key=lambda x: x[1].hour)
            sum_by_hours = []
            k = 0
            for i in range(24):
                current_sum = 0
                while k < len(sorted_by_day) and sorted_by_day[k][1].hour == i:
                    current_sum += float(sorted_by_day[k][2])
                    k += 1
                sum_by_hours.append(current_sum)

            print(f'Records from my route: {len(my_route)} Processed: {filename1} and {filename2} ')
    return sum_by_hours


results = [
    [read_and_count_by_hours('./2018/sausis(1).csv', './2018/sausis(2).csv'), 'january'],
    [read_and_count_by_hours('./2018/vasaris(1).csv', './2018/vasaris(2).csv'), 'february'],
    [read_and_count_by_hours('./2018/kovas(1).csv', './2018/kovas(2).csv'), 'march'],
    [read_and_count_by_hours('./2018/Balandis(1).csv', './2018/balandis(2).csv'), 'april'],
    [read_and_count_by_hours('./2018/geguze(1).csv', './2018/geguze(2).csv'), 'may'],
    [read_and_count_by_hours('./2018/birzelis(1).csv', './2018/birzelis(2).csv'), 'june'],
    [read_and_count_by_hours('./2018/liepa(1).csv', './2018/liepa(2).csv'), 'july'],
    [read_and_count_by_hours('./2018/rugpjutis(1).csv', './2018/rugpjutis(2).csv'), 'august'],
    [read_and_count_by_hours('./2018/rugsejis(1).csv', './2018/rugsejis(2).csv'), 'september'],
    [read_and_count_by_hours('./2018/spalis(1).csv', './2018/spalis(2).csv'), 'october'],
    [read_and_count_by_hours('./2018/lapkritis(1).csv', './2018/lapkritis(2).csv'), 'november'],
    [read_and_count_by_hours('./2018/gruodis(1).csv', './2018/gruodis(2).csv'), 'december']
]

for result in results:
    plt.plot(range(24), result[0], label=result[1])

print(f'used {used_records}/{overall_records}')
ax = plt.subplot(111)
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
plt.xticks(range(24))
plt.ylabel('traffic volume / hour')
plt.xlabel('time')
plt.figure(figsize=(20, 10))
plt.show()
