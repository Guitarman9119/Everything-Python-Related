"""
Final Project for Week 4 of "Python Programming Essentials"
Collection of functions to process dates.
"""
#import the datetime module of Python3
import datetime


def days_in_month(year, month):
    """
    Problem 1 - Computing the number of days in a month
    Function receive the following inputs:
      year  - an integer between datetime.MINYEAR and datetime.MAXYEAR
              representing the year
      month - an integer between 1 and 12 representing the month
    Returns:
      The number of days in the input month.
    """
    
    #if statements to test if month is between 1 and 12 
    if month < 12 and month >= 1:
        
        # In this calculation we take the given date plus one month added subtracted by date given to get the difference of days
        # This will give the given days of that month.
        number_of_days = (datetime.date(year, month+1, 1) - datetime.date(year, month, 1)).days
        
        # return the integer value of the total number of days for given date
        return number_of_days
    
    #When month equals to 12 the total number of days will always be 31
    else:
        return (31)


    
def is_valid_date(year, month, day):
    """
    Problem 2 - Computing if a date given is valid
    Inputs:
      year  - an integer representing the year
      month - an integer representing the month
      day   - an integer representing the day

    Returns:
      True if year-month-day is a valid date and
      False otherwise
    """
    
  
    #Check if date is True through conditional statement
    if year <= datetime.MAXYEAR and year >= datetime.MINYEAR and month >= 1 and month<=12 and day <= days_in_month(year, month) and day >= 1:
        return True
    
    #The date was invalid
    else:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Problem 3 - Calculating number of days between two given dates
    Inputs:
      year1  - an integer representing the year of the first date
      month1 - an integer representing the month of the first date
      day1   - an integer representing the day of the first date
      year2  - an integer representing the year of the second date
      month2 - an integer representing the month of the second date
      day2   - an integer representing the day of the second date

    Returns:
      The number of days from the first date to the second date.
      Returns 0 if either date is invalid or the second date is
      before the first date.
    """
    #Set two test conditions
    test_date_one = True
    test_date_two = True
   
    #Test if the two dates given is valid
    if test_date_one == is_valid_date(year1, month1, day1) and test_date_two == is_valid_date(year2, month2, day2):
        
        date_one = datetime.date(year1, month1, day1)
        date_two = datetime.date(year2, month2, day2)
        
     #If test date is before test date one return false
        if date_two < date_one:
            return False
        
     #Calculate the number of days between the two dates
        else:
            number_of_days_between = date_two - date_one
            return (number_of_days_between.days)
        
    #If dates are not valid return False
    else:
        return False



def age_in_days(year, month, day):
    """
    Problem 4 - Calculate age in number of days
    Inputs:
      year  - an integer representing the birthday year
      month - an integer representing the birthday month
      day   - an integer representing the birthday day

    Returns:
      The age of a person with the input birthday as of today.
      Returns 0 if the input date is invalid or if the input
      date is in the future.
    """
    #Set test conditions
    test_date = True
    
    #Test if dates given is valid
    if test_date == is_valid_date(year, month, day):

        date_given =  datetime.date(year, month, day)
        date_today = datetime.date.today()
        
        #Test given is in the Future return False
        if date_given > date_today:
            return False
        #Calculate the number of days from date given to current date
        else:
            
            number_of_days_between = date_today - date_given
            return (number_of_days_between.days)
        
    #Date is not valid return False
    else:
   
        return False



