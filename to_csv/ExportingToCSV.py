import csv


def write(time, download, upload):
    csvfile = open('.tmp.csv', 'a')
    my_writer = csv.writer(csvfile, delimiter=',')
    my_writer.writerow((time, download, upload))
