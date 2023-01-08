import csv


def write(time, value1, value2):
    csvfile = open('.tmp.csv', 'a')
    my_writer = csv.writer(csvfile, delimiter=',')
    # my_writer.writerow((time, value1.split(" ")[0], value2.split(" ")[0]))
    my_writer.writerow((time, value1, value2))