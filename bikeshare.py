import time
import numpy as np
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def ask_user():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print("")
    print('Explore some USA bikeshare data!')
    print("")
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    the_city_names = ['chicago','new york city','washington']

    while True:
        ask_about_city = "Which city do you like to explore data from it (chicago, new york city, washington)?:  "
        user_selecttion_city = input(ask_about_city)
        print("")
        if user_selecttion_city.lower() in the_city_names:
            city = user_selecttion_city
            break
        else:
            print("This is wrong, select the correct city for these choices (chicago, new york city, washington)")
            print("")


    # get  input from the user for month (all, january, february, ... , june)
    correct_month_choice = ['all' , 'january' , 'february' , 'march' , 'april' , 'may' , 'june']
    while True:
        ask_about_month = input("Which month do you want to chose? (All, January , February , March , April , May or June) :  ")
        print("")
        if ask_about_month.lower() in correct_month_choice:
            month = ask_about_month
            break
        else:
            print("This is wrong, select the correct month (All , January , February , March , April , May or June)")
            print("")


    # get  input from the user for day of week (all, monday, tuesday, ... sunday)
    correct_day = ['all' , 'monday' , 'tuesday' , 'wednesday' , 'thursday', 'friday' , 'saturday' , 'sunday' ]
    while True:
        ask_about_days = input("Which day do you want to chose? (All , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday) :  ")
        print("")
        if ask_about_days.lower() in correct_day:
            day = ask_about_days
            break
        else:
            print("This is wrong, select the correct day (All , Monday , Tuesday , Wednesday , Thursday , Friday , Saturday , Sunday)")
            print("")


    print('-'*40)
    return city , month , day


def loading_datasts(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    city_name = city.lower()
    month = month.lower()
    day = day.lower()

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city_name])

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


def time_status(df):
    """Show and Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Travels Most Frequent Times  ...\n')
    print("")
    start_time = time.time()

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Show and display the most common month
    df['month'] =  df['Start Time'].dt.month
    most_famous_month = df['month'].mode()[0]
    print("The Most common month is: ",most_famous_month)
    print("")

    # Show and display the most common day of week
    df['day_of_week'] =  df['Start Time'].dt.weekday_name
    most_famous_day_of_week = df['day_of_week'].mode()[0]
    print("The Most common day of week is: ",most_famous_day_of_week)
    print("")

    # Show and display the most common start hour
    df['hour'] =  df['Start Time'].dt.hour
    most_famous_hour = df['hour'].mode()[0]
    print("The Most common start hour is: ",most_famous_hour)
    print("")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_status(df):
    """Show and Displays statistics on the most popular stations and trip."""

    print('\nCalculat The Most Popular Stations and Trip...\n')
    print("")
    start_time = time.time()

    # Show and display most commonly used start station
    commonly_used_start_station = df['Start Station'].mode()[0]
    count_of_commonly_used_start_station = df['Start Station'].value_counts()[0]
    print("Commonly used start station: {} with number of counts: {}.".format(commonly_used_start_station,count_of_commonly_used_start_station))
    print("")


    # Show and display most commonly used end station
    commonly_used_end_station = df['End Station'].mode()[0]
    count_of_commonly_used_end_station = df['End Station'].value_counts()[0]
    print("Commonly used end station: {} with number of counts: {}.".format(commonly_used_end_station,count_of_commonly_used_end_station))
    print("")


    # Show and display most frequent combination of start station and end station trip
    Frquent_combination_trip = df[['Start Station', 'End Station']].mode()
    print("The frequent combination of start station and end station trip")
    print(Frquent_combination_trip)
    print("")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_status(df):
    """Show and Displays statistics on the total and average trip duration."""

    print('\nCalculat Trip Duration...\n')
    print("")
    start_time = time.time()

    # Show and display total travel time
    travel_time = df['Trip Duration'].sum()
    print("The total time of travel is: {}.".format(travel_time))
    print("")

    # Show and display mean travel time
    mean_travel_time_duration = df['Trip Duration'].mean()
    print("The duration of the mean travel time is: {}.".format(mean_travel_time_duration))
    print("")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_status(df):
    """Show and Displays statistics on bikeshare users."""

    print('\nCalculat User Stats...\n')
    print("")
    start_time = time.time()

    # Show and Display counts of user types
    if 'User Type' in df.columns:
        count_number_of_user_types = df['User Type'].value_counts()
        print("Count numbers of user types: .....")
        print(count_number_of_user_types)
        print("")

    # Show and Display counts of gender
    if 'Gender' in df.columns:
        count_number_of_gender = df['Gender'].value_counts()
        print("Count numbers of gender: .....")
        print(count_number_of_gender)
        print("")

    # Show and Display earliest, most recent, and most common year of birth


    if 'Birth Year' in df.columns:

        the_earliest_year_of_birth = df['Birth Year'].min()
        print("Earliest year of birth is {}.".format(the_earliest_year_of_birth))
        print("")


        the_most_recent_year_of_birth = df['Birth Year'].max()
        print("Most recent year of birth is {}.".format(the_most_recent_year_of_birth))
        print("")

        the_most_common_year_of_birth = df['Birth Year'].mode()[0]
        count_of_the_most_common_year_of_birth = df['Birth Year'].value_counts().values[0]
        print("Most common year of birth is {} with number of counts {}.".format(the_most_common_year_of_birth,count_of_the_most_common_year_of_birth))



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# The main loop ....

def main():
    while True:
        city,month,day = ask_user()

        df = loading_datasts(city,month,day)


        time_status(df)

        ask_more = input('\nYou want to see more result ? yes or no.\n')
        if ask_more.lower() == 'yes':
        	station_status(df)
        	ask_more = input('\nYou want to see more result ? yes or no.\n')
        	if ask_more.lower() == 'yes':
        		station_status(df)
        		ask_more = input('\nYou want to see more result ? yes or no.\n')
        		if ask_more.lower() == 'yes':
        			trip_duration_status(df)
        			ask_more = input('\nYou want to see more result ? yes or no.\n')
        			if ask_more.lower() == 'yes':
        				user_status(df)
        			elif ask_more.lower() == 'no':
        				break
        			elif ask_more.lower() == 'yes':
        				break


        	elif ask_more.lower() == 'no':
        		break


        elif ask_more.lower() == 'no':
            break

        restart = input('\nWould you like to repeat again??? yes or no.\n')
        if restart.lower() != 'yes':
        	break


if __name__ == "__main__":
	main()
