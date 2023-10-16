# Python program to find the first day of given year

# import datetime library
import datetime


def Startingday(year):

	Days = ["Monday", "Tuesday", "Wednesday",
			"Thursday", "Friday", "Saturday", "Sunday"]

	# Creating an object for 1st January of that particular year
	# For that we are passing three argument (1) year (2) month
	# i.e 1 for january (3) date i.e 1 for starting day of
	# that particular year
	a = datetime.datetime(year, 1, 1).weekday()

	# f-String is used for printing Startingday of a particular year
	print(f"Starting day of {year} is {Days[a]}.")


# Driver Code
year = 2010
Startingday(year)
