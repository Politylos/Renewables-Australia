import schedule
import time
import csv
import csv, urllib.request
global cc
cc= 0;
def pull_data(url,file):
    response = urllib.request.urlopen(url)
    lines = [l.decode('utf-8') for l in response.readlines()]
    cr = csv.reader(lines)

    f = open(file, 'a')
    writer = csv.writer(f)
    for row in cr:
        writer.writerow(row)
    f.close()
run = True

def func():
    pull_data('https://services.aremi.data61.io/aemo/v6/csv/renewables','renewable.csv')
    pull_data('https://services.aremi.data61.io/aemo/v6/csv/fossil','Fossil.csv')
    print("pulled")
  
schedule.every(5).minutes.do(func)
func()
while run:
    schedule.run_pending()
    time.sleep(100)
