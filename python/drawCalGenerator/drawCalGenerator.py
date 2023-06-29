#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8

# Copyright (C) 2023 Xavier Schoepfer
# GNU GENERAL PUBLIC LICENSE Version 3

from datetime import date, timedelta


# global variables
# reference year
year = 2023
# draw days for the game
isoDrawDay = (1, 3, 6)	# ISO format, Loto® draws : Monday, Wednesday, Saturday
#isoDrawDay = (2, 4)	# ISO format, Euromillions® draws : Tuesday, Friday
# number of days in the months
maxDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]



def main():
	
	# if needed, update the number of days in February
	delta = date(year, 3, 1) - date(year, 2, 1)
	if maxDays[1] != delta.days:
		maxDays[1] = delta.days
	
	# set date to January 1
	myMonth = 1	# ISO format
	myDay = 1	# ISO format
	d = date(year, myMonth, myDay)
	
	# setup the month
	while myMonth <= 12:
		d = d.replace(month = myMonth)
		# setup the day
		while myDay <= maxDays[myMonth - 1]:
			d = d.replace(day = myDay)
			# is this a draw day?
			for myDrawDay in isoDrawDay:
				if myDrawDay == d.isoweekday():
					# print the date in ISO format
					print(d.isoformat())
			# next day
			myDay = myDay + 1
		# next month
		myMonth = myMonth + 1
		# reset on 1st day of the next month
		myDay = 1
		d = d.replace(day = myDay)


	
if __name__ == '__main__':
	main()
