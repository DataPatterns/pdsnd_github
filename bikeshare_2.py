import time
import pandas as pd
import numpy as np
import datetime
import math

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_NO = {
    'all':0,
    'january':1,'february':2,'march':3,
    'april':4,'may':5,'june':6
}

MONTH_NAMES = {v: k for k, v in MONTH_NO.items()}

DAY_NO = {
    'all': -1,
    'monday' : 0,
    'tuesday' : 1,
    'wednesday' : 2,
    'thursday' : 3,
    'friday' : 4,
    'saturday' : 5,
    'sunday' : 6
}
DAY_NAMES = {v: k for k, v in DAY_NO.items()

def data_cleaning():
    pass}

def data_processing():
    pass

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    flag = 0
    city = input("Enter the name of the city you want to analyze. Valid options: chicago, new york city, washington -> : ")
    while flag == 0:
        if city in CITY_DATA:
            flag=1
        else:
            city = input("You have entered a invalid name \n"
                          "Enter the name of the city you want to analyze. Valid options: chicago, new york city, washington -> : ")


    # get user input for month (all, january, february, ... , june)
    flag = 0

    month = input("Enter the month you want to analyze. Valid options:  january, february, march, april, may , june \n"
                  "if you want to analyze all months, just enter all -> : ")
    while flag == 0:
        if month in MONTH_NO:
            flag = 1
        else:
            month = input("You have entered a invalid month \n"
                         "Enter the month you want to analyze. Valid options:  january, february, march, april, may , june \n"
                          "if you want to analyze all months, just enter all -> :"
                          )

    # get user input for day of week (all, monday, tuesday, ... sunday)
    flag = 0
    valid_day = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    day = input("Enter the day of week you want to analyze. Valid options: monday, tuesday, ... sunday \n"
                "if you want to analyze all days, just enter all -> :")
    while flag == 0:
        if day in DAY_NO:
            flag = 1
        else:
            day = input("You have entered a invalid day \n"
                          "Enter the day of week you want to analyze. Valid options: monday, tuesday, ... sunday \n"
                        "if you want to analyze all days, just enter all -> : ")
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])

    # Convert start and end time to date format
    df["Start Time"] = pd.to_datetime(df["Start Time"])
    df["End Time"] = pd.to_datetime(df["End Time"])


    # select the required month
    if month !="all":
        df = df[(df['Start Time'].dt.month == MONTH_NO[month]) &
                (df['End Time'].dt.month == MONTH_NO[month])]

    # select the required day
    if day != "all":
        df = df[(df['Start Time'].dt.dayofweek == DAY_NO[day]) &
                (df['End Time'].dt.dayofweek == DAY_NO[day])]


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print("the most common month is :" ,MONTH_NAMES[df['Start Time'].dt.month.mode()[0]])

    # display the most common day of week
    print("the most common day is :", DAY_NAMES[df['Start Time'].dt.dayofweek.mode()[0]])

    # display the most common start hour
    print("the most common hour is :", df['Start Time'].dt.hour.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    df["Start_End station"] = df["Start Station"] +"  ---  "+ df["End Station"]
    # display most commonly used start station
    print("the most popular start station is :", df['Start Station'].mode()[0])

    # display most commonly used end station
    print("the most popular end station is :", df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    print("the most popular start and end combination station is :", df["Start_End station"].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    df["travel_time_mins"] =  (df["End Time"] - df["Start Time"]).astype('timedelta64[m]')

    # display total travel time
    print("total travel duration in hours: ", round(df["travel_time_mins"].sum()/60))

    # display mean travel time
    print("mean travel duration in mins: ", round(df["travel_time_mins"].mean(),2))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("Count of user types:")
    print(df['User Type'].value_counts())
    print()

    # Display counts of gender
    print("Count of gender:")
    print(df['Gender'].value_counts())
    print()


    # Display earliest, most recent, and most common year of birth
    print("Earliest year of birth", df["Birth Year"].min())
    print("Recent year of birth", df["Birth Year"].max())
    print("Most common year of birth", df["Birth Year"].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        while True:
            sampledata = input('\nWould you like to see 5 lines of raw data. ? Enter yes or no.\n')
            if sampledata.lower() != 'yes':
                break
            else:
                print(df.head(5))

        try:
            time_stats(df)
            station_stats(df)
            trip_duration_stats(df)
            user_stats(df)
        except Exception as e:
            print("There seems like to be an issue with ",e, "for inputs given")

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
