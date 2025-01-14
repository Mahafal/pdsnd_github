import time
import pandas as pd
import numpy as np



CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }


def verification_input(value, answer):

    while True:
        user_input = input(value).lower()
        try:
            if user_input in ['chicago', 'new york city', 'washington'] and answer == 1:
                break
            elif user_input in ['january' , 'february' , 'march' , 'april' , 'may' , 'june' , 'all'] and answer == 2:
                break
            elif user_input in ['sunday' , 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all'] and answer == 3:
                break
            else:
                if answer == 1 or answer == 2 or answer == 3:
                    print('wrong answer')
        except ValueError:
            print('error input')
    return user_input




def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Answer the questions asked')

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Information will be displayed based on choices')

def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    print('Information will be displayed based on choices')

    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = verification_input('which city would you like to display its information?(chicago, new york city, washington) ' , 1)
    # TO DO: get user input for month (all, january, february, ... , june)
    month = verification_input('in which month? *from January to June ', 2)
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = verification_input('in which day? ', 3)
    print('-'*40)

    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable
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
    df['hours'] = df['Start Time'].dt.hour

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
    print('Most Common Month: ', df['month'].mode()[0])
    # TO DO: display the most common day of week
    print('Most Common Day of Week: ' , df['day_of_week'].mode()[0])
    # TO DO: display the most common start hour
    print('Most Common Start Hour: ' , df['hours'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('Most commonly used start station: ', df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print('Most commonly used end station: ', df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print('Most frequent combination of start station and end station trip: ', df.groupby(['Start Station','End Station']).size().idxmax())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total Travel Time: ' , df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Mean Travel Time:' , df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    # TO DO: Display counts of user types
    print('counts of user types: ' , df['User Type'].value_counts())
    # TO DO: Display counts of gender
    # TO DO: Display earliest, most recent, and most common year of birth
    if city == 'chicago' or city == 'new york city':
        print('Gender' , df['Gender'].value_counts())
        print('Earliest year of Birth: ' , df['Birth Year'].min())
        print('Recent year of Birth: ' , df['Birth Year'].max())
        print('Common year of birth: ' , df['Birth Year'].mode()[0])
    else:
        print('Sorry no data about gnder and Birth Year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    #function used to specify view way of the data
def showdata(df):
    row = 0
    T = True
    while T:
        rowdata= input('if you like to see row data enter - yes -: \n').lower()
        if rowdata == 'yes':
            print(df.iloc[row:row + 5])
            row += 5
        elif rowdata == 'no':
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)


        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        showdata(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
            print('yes')



if __name__ == "__main__":
	main()
