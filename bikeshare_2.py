import time
import pandas as pd
import numpy as np
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

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
    city = input('Choose what city would you like to analyze [chicago , new york, washington]:').lower()

    while city not in CITY_DATA.keys():
        print('invalid input please try again')
        city = input('Choose what city would you like to analyze [chicago , new york, washington]:').lower()

    # get user input for month (all, january, february, ... , june)
    months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

    month = input('Choose what month would you like to filter by, or "all" to apply no month filter [january , february , march , april , may , june]:').lower()

    while month not in months:
        print('invalid input please try again')
        month = input('Choose what month would you like to filter by, or "all" to apply no month filter [january , february , march , april , may , june]:').lower()

    # get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

    day = input('Choose what day would you like to filter by, or "all" to apply no day filter [monday , tuesday , wednesday , thursday , friday , saturday , sunday ]:').lower()

    while day not in days:
        print('invalid input please try again')
        day = input('Choose what day would you like to filter by, or "all" to apply no day filter [monday , tuesday , wednesday , thursday , friday , saturday , sunday ]:').lower()

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

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.day_name()
    # Filter the data by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
        df = df[df['month'] == month]
    # Filter the data by day of week
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most popular month is {}'.format(df['month'].mode()[0]))

    # display the most common day of week
    print('The most popular day is {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('The most popular hour is {}'.format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most popular start station is {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most popular end station is {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station'] + ' - ' + df['End Station']

    print('The most popular trip is {}'.format(df['Trip'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('the total travel time is {}'.format(df['Trip Duration'].sum().round()))

    # display mean travel time
    print('The average travel time is {}'.format(df['Trip Duration'].mean().round()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('Number of customers based on user type is:\n', df['User Type'].value_counts())

    print('\nCalculate total gender & earliest, most recent, and most common year of birth...\n')

    if city !='washington':
         # Display counts of gender
         print('Number of customers based on gender is:\n', df['Gender'].value_counts())

         # Display earliest, most recent, and most common year of birth
         print('\nThe earliest year of birth is {}'.format(int(df['Birth Year'].min())))

         print('The latest year of birth is {}'.format(int(df['Birth Year'].max())))

         print('The most popular year of birth is {}'.format(int(df['Birth Year'].mode()[0])))
    else:
        print("Washington file haven't gender & birth year coulmns!!")
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)

def print_raw_data(df):
    """Displays 5 rows of raw data on a bikeshare file."""
    index = 0
    
    choice = input("Do you want to show 5 rows in the dataset (yes,no) ? ").lower()

    while choice != 'yes' and choice != 'no':
        print("Invalid input. Please try again.")

        choice = input("Do you want to show 5 rows in the dataset (yes,no) ? ").lower()


    while choice == 'yes':
        end = index + 5

        print(df.iloc[index:end])

        index += 5
        choice = input("Do you want to show first 5 rows in the dataset (yes,no) ?").lower()

        while choice != 'yes' and choice != 'no':
            print("Invalid input. Please try again.")

            choice = input("Do you want to show first 5 rows in the dataset (yes,no) ? ").lower()

    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)
        print_raw_data(df)


        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        while restart not in ['yes','no']:
            print("Invalid input. Please try again.")
            restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart != 'yes':
            break


if __name__ == "__main__":
	main()
