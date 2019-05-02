# Create a reminder in an specific date/hour of the calendar
import calendar

import datetime

import pytz


dateNow = datetime.date.today()

timeNow = datetime.datetime.now(tz=pytz.utc)

myTimeNow = timeNow.astimezone(pytz.timezone('America/Buenos_Aires'))


def reminder():

    try:
        if dateNow == datetime.date(2019, 2, 27):
            print('It´s', myTimeNow, 'and you have an active reminder!')
        else:
            print('You don´t have any activity programmed for today =)')
    except:
        print('Ups!')


def main():
    reminder()
    print(calendar.calendar(2019))

if __name__ == '__main__':
    main()
