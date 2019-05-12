import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

CITIES = ['chicago', 'new york city', 'washington']

MONTHS = ['january', 'february', 'march', 'april', 'may', 'june']

DAYS = ['sunday', 'monday', 'tuesday', 'wednesday', \
        'thursday', 'friday', 'saturday' ]


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington)


    while True:
        city = input('Enter a city (Chicago, New York City or Washington): ').lower()
        if city in CITIES:
            break

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Enter a month (All, January, February, ... , June): ').lower()
        if month == 'all':
            month == MONTHS
            break
        elif month in MONTHS:
            break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Enter a weekday (All, Monday, Tuesday, ... , Sunday): ').lower()
        if day == 'all':
            day == DAYS
            break
        elif day in DAYS:
            break

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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode().loc[0]
    print('Most Popular Month: ', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode().loc[0]
    print('Most Popular Day: ', popular_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().loc[0]
    print('Most Popular Start Hour: ', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    popular_start = df['Start Station'].mode().loc[0]
    print('Most Popular Start Station: ', popular_start)

    # display most commonly used end station
    popular_end = df['End Station'].mode().loc[0]
    print('Most Popular End Station: ', popular_end)

    # display most frequent combination of start station and end station trip
    most_common_start_end_station = df[['Start Station', 'End Station']].mode().loc[0]
    print("The most commonly used start station and end station : {}, {}"\
            .format(most_common_start_end_station[0], most_common_start_end_station[1]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time


    # display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Most Popular User Types:\n', user_types)


    # Display counts of gender
    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
        print('Counts of gender:\n', gender_counts)


    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        birth_year = df['Birth Year']

        most_common = birth_year.value_counts().idxmax()
        print("The most common birth year: ", most_common)

        most_recent = birth_year.max()
        print("The most recent birth year:", most_recent)

        earliest = birth_year.min()
        print("The most earliest birth year:", earliest)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays 5 rows of raw data from the selected csv file"""

    counter = 0
    response_raw = input('Do you want to see the raw data? Enter \'yes\' or \'no\': ').lower()

    while True:
        while response_raw == 'yes':
            print(df.iloc[counter:counter+5])
            counter += 5
            response_raw = input('Do you want to see more raw data? Enter \'yes\' or \'no\': ').lower()
        if response_raw == 'no':
            break
        else:
            response_raw = input('Please enter \'yes\' or \'no\'').lower()

#    while True:
#       city = input('Enter a city (Chicago, New York or Washington): ').lower()
#       if city in CITIES:
#            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        (time_stats(df))
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
