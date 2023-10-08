import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
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
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input("Would you like to see data for Chicago, New York City, or Washington?\n").lower()

        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print("Invalid input. Please enter one of the specified cities (Chicago, New York City, or Washington).")

    # TO DO: get user input for month (all, january, february, ... , june)
    print('\nWhich month would you like to see data from:\n')
    while True:
        month = input("Enter a month between: january, february, march, may, june, or all to see data from all months: ").lower()

        if month in ['january', 'february', 'march', 'may', 'june', 'all']:
            break
        else:
            print("Invalid input. Please enter one of the specified months (january, february, march, may, june, or all).")

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('\nWhich day of week would you like to see data from:\n')
    while True:
        day = input("Enter a day of week between: monday, tuesday, wednesday, thursday, friday, saturday, sunday or all to see data from all days: ").lower()

        if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
            break
        else:
            print("Invalid input. Please enter one of the specified days (monday, tuesday, wednesday, thursday, friday, saturday, sunday, or all).")

    print('-'*50)
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
    # extract month and day of week and hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month']==month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week']==day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print(f"The most common month is: {months[df['month'].value_counts().idxmax()-1].title()}")

    # TO DO: display the most common day of week
    print(f"The most common day of week is: {df['day_of_week'].value_counts().idxmax()}")

    # TO DO: display the most common start hour
    print(f"The most common start hour is: {df['hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(f"The most commonly used start station is: {df['Start Station'].value_counts().idxmax()}")


    # TO DO: display most commonly used end station
    print(f"The most commonly used end station is: {df['End Station'].value_counts().idxmax()}")


    # TO DO: display most frequent combination of start station and end station trip
    most_frequent_combination = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print(f"The most frequent combination of start station and end station trip is: {most_frequent_combination[0]} and {most_frequent_combination[1]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(f"The total travel time is: {df['Trip Duration'].sum()}")


    # TO DO: display mean travel time
    print(f"The total travel time is: {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("\nUser Counts")
    user_types = df['User Type'].value_counts().to_dict()
    for category, count in user_types.items():
        print(f"{category}: {count}")

    # TO DO: Display counts of gender
    if 'Gender' in df:
        print("\nGender Counts")
        gender = df['Gender'].value_counts().to_dict()
        for category, count in gender.items():
            print(f"{category}: {count}")
    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        print(f"\n\nThe earliest year of birth is: {int(df['Birth Year'].min())}")
        print(f"The most recent year of birth is: {int(df['Birth Year'].max())}")
        print(f"The most common year of birth is: {int(df['Birth Year'].value_counts().idxmax())}")
    else:
        print('Birth Year stats cannot be calculated because Birth Year does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
    
def display_raw_data(df):
    """Displays Raw Data"""
    
    start_time = time.time()
    
    start_row = 0
    chunk_size = 10

    while True:
        show_data = input("Would you like to see 10 rows of raw data? Enter yes or no: ").strip().lower()

        if show_data == 'yes':
            end_row = start_row + chunk_size
            print(df.iloc[start_row:end_row])
            start_row = end_row
        elif show_data == 'no':
            print("Thank you.")
            break
        else:
            print("Invalid input. Enter yes or no.\n")    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*50)
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
