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
    city = input("\n Please enter the city chicago, new york city or washington : ").lower()
    while city not in ["chicago", "new york city", "washington"]:
        city = input("\nError please entnr again (Chicago, New york city, Washington) : ").lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("\nPlease enter month from January to June to show data in that month or type all for all months : ").lower()
    while month not in ["all","january","february","march","april","may","june"]:
       month = input("\n not valid month please enter again : ").lower()


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("\nPlease enter the day or enter all for all days : ").lower()
    while day not in ("all","saturday","sunday","monday","tuesday","wednesday","thuresday","friday"):
        day = input("\nError enter again : ")


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

    # TO DO: display the most common month
    print("\nThe most common month is {}".format(df["month"].mode()[0]))

    # TO DO: display the most common day of week
    print("\nThe most common day of the week is {}".format(df["day_of_week"].mode()[0]))

    # TO DO: display the most common start hour
    df["hour"] = df["Start Time"].dt.hour
    print("\nThe most common starting hour is {}".format(df["hour"].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("\nThe most commonly used start station is {}".format(df["Start Station"].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most commonly used end station is {}".format(df["End Station"].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    df["Starting and Ending station"] = df["Start Station"] + " to " + df["End Station"]
    print("The most commonly used start to end station is {}".format(df["Starting and Ending station"].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    df["Total trip Time"] = pd.to_datetime(df["End Time"]) - pd.to_datetime(df["Start Time"])
    """ Changing data type to datetime which is function in pandas
    https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html#pandas.to_datetime """

    # TO DO: display total travel time
    total_travel = df["Total trip Time"].sum()
    print("\nTotal travel time is",total_travel)

    # TO DO: display mean travel time
    mean_travel = df["Total trip Time"].mean()
    print("Mean travel time is",mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    type_of_user = df.groupby("User Type")['User Type'].count()
    print("\nNumber of users for each type user are\n",type_of_user)

    """ https://stackoverflow.com/questions/15705630/get-the-rows-which-have-the-max-value-in-groups-using-groupby """

    # TO DO: Display counts of gender
    if "Gender" not in df:
        print("\nNo gender data avaliable in this city")
    else:
        gender_types = df.groupby("Gender")['Gender'].count()
        print("\nNumber of each gender in this city \n",gender_types)

    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" not in df:
        print("\nNo birth year data avaliable in this city")
    else:
        print("\nThe earliest birth year in this city is {}".format(int(df["Birth Year"].min())))
        print("\nThe earliest age in this city is {}".format(int(2019-df["Birth Year"].min())))
        print("The most recent birth year in this city is {}".format(int(df["Birth Year"].max())))
        print("The most recent age in this city is {}".format(int(2019-df["Birth Year"].max())))
        print("The most common birth year in this city is {}".format(int(df["Birth Year"].mode()[0])))
        print("The most common age in this city is {}".format(int(2019-df["Birth Year"].mode()[0])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    """ Display contents of the data to the display when the user requested """

    start_count = 0
    end_count = 5

    display_row = input("Do you want to see data? Enter yes to display it.\n").lower()
    if display_row == 'yes':
        while end_count < df.shape[0]:
            print(df.iloc[start_count:end_count:])
            start_count = start_count + 5
            end_count = end_count + 5
            display_end = input("Do you wish to continue? Enter no to end displaying more rows.\n").lower()
            if display_end == 'no':
               break

    """ https://www.geeksforgeeks.org/python-pandas-df-size-df-shape-and-df-ndim/ """
    """ also  https://www.shanelynn.ie/summarising-aggregation-and-grouping-data-in-python-pandas/ """

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
