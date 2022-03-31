"""
CTEC 121
date: <ex: mm/dd/yyyy>
<your name>
"""

"""
INSTRUCTIONS:
READ ALL OF THE INSTRUCTIONS BEFORE YOU START WORKING ON THE CODE
0) The code below will not run.
1) The code below contains 7 errors. 
2) Some of the errors are syntactic, others are logic errors
3) Your job is to fix the errors and to place a comment above the line or to 
   the right of the line that 1) describes the error and 2) describes what you
   did to fix the error.
4) Make sure the code runs.
5) Re-read Steps 1 - 4 above :-).
"""


def main():
    # get the day month and year as numbers
    day = integer(input("Enter the day number: "))
    month = int(input("Enter the month number: '))
    year == int(input("Enter the year: "))

    # concatenate the numbers together by converting each variable to a string
    date1 = str(month) "/" + str(day) + "/"+str(year)

    # define a list of the months of the year
    months = ["January"  "February", "March", "April",
              "May", "June", "July", "August",
              "September", "October", "November", "December"]

    # Get the month string 
    monthStr = months[month]

    # concatenate the data together again converting numbers to strings
    date2 = monthStr+" " + str(day) + ", "  str(year)

    # display the date
    print("The date is", date1, "or", date2+".")


main()
