#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'C:/Users/Teletrabajo/Downloads/all-project-files/chicago.csv',
              'new york city': 'C:/Users/Teletrabajo/Downloads/all-project-files/new_york_city.csv',
              'washington': 'C:/Users/Teletrabajo/Downloads/all-project-files/washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) cities - name of the city to analyze
        (str) month_sel - name of the month to filter by, or "all" to apply no month filter
        (str) day_sel - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    
    cities = input('Please enter one city - Chicago - New York City - Washington : ')
    cities = cities.lower()
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while cities not in CITY_DATA:
        cities = input('City not avalible, please choose between New York, Chicago or Washington')
        cities = cities.lower()


    # TO DO: get user input for month (all, january, february, ... , june)
    
    month_sel = input('Please choose a month -between january and june or option - all - for select all')
    month_sel = month_sel.lower()
    month_list = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    
    while month_sel not in month_list:
        month_sel = input('month not avalible, Please choose a month -between january and june or option - all - for select all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    
    day_sel = input('Please choose a day on week, or select -all-  for select all')
    day_sel = day_sel.lower()
    days = ['all', 'monday','tuesday', 'sunday', 'wednesday', 'thursday', 'friday', 'saturday']
    
    while day_sel not in days:
        day_sel = input('Please choose a day on week, or select -all-  for select all, try again!!')
        
    print('-'*40)
    return cities, month_sel, day_sel


def load_data(cities, month_sel, day_sel):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
     
    df = pd.read_csv(CITY_DATA[cities], sep = ',')
    
    # tranform 'Start time' to date
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])#, format = '%Y%m%d%h%m%s')
                                       
                                     
           
    # Create Columns with month and year
    
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()
    

    #Filtering  df with the month and day choose incluided
    
    
    if  month_sel != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month_sel) + 1
        
    #Filtering by the day
    
    if  day_sel != 'all':
        df = df[df['day'] == day_sel.title()]     
            
    return df


def time_stats(df):
    
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    months_y = ['january', 'february', 'march', 'april', 'may', 'june']
    mode_month = df['month'].mode()[0]
    print('the most common month is: '+ months_y[mode_month-1])
    
      

    # TO DO: display the most common day of week
    
    mode_day = df['day'].mode()
    print('the most common day of week is: {}'.format(mode_day) )
    
    
    # TO DO: display the most common start hour
    
    common_hour = df['Start Time'].dt.hour.mode()
    print('The most common hour is: {} '.format(common_hour))
 
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    common_station_s = df['Start Station'].mode()
    print('The most common start station is: ', common_station_s)


    # TO DO: display most commonly used end station
    
    common_station_f = df['End Station'].mode()
    print('The most common end station is: ', common_station_f)


    # TO DO: display most frequent combination of start station and end station trip
          
    common_combination = df.groupby(['End Station', 'Start Station']).size().nlargest(1)
    print('The most common combination of start station and end station trip is {}'.format(common_combination))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    total_trip_time = df['Trip Duration'].sum()
    total_time_min = total_trip_time // 60
    print('Total travel time was {} minutes'.format(total_time_min))


    # TO DO: display mean travel time
    
    mean_time = df['Trip Duration'].mean()
    mean_time_min = mean_time // 60
    print('Mean of travel is {} minutes.'.format(mean_time_min))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    
       
    subscriber = 0
    dependent = 0
    customer = 0
    
    for i in df['User Type']:
        if i == 'Subscriber':
            subscriber = subscriber + 1
        elif i == 'Dependent':
            dependent = dependent + 1
        else:  customer = customer + 1
    print('count of user is: {} subscribers, {} dependents and {} customers.'.format(subscriber, dependent,customer ))
                
                

    # TO DO: Display counts of gender
    
    Male = 0
    Female = 0
    No_Gender = 0
    
    if 'Gender' not in df.columns.tolist():
        print('Gender count not avalible') 
    else:
        for i in df['Gender']:
            if i == 'Male':
                Male = Male + 1
            elif i == 'Female':
                Female = Female + 1
            else:   No_Gender = No_Gender + 1
    print('count of gender is: {} Males, {} Females and {} no genders'.format(Male,Female,No_Gender))            
                
               
      
    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' not in df.columns.tolist():
        print('Birth Year not avalible')
    else:
        df.fillna(method = 'Ffill', axis = 0)
        earliest_year = df['Birth Year'].min()
        recent_year = df['Birth Year'].max()
        common_year = df['Birth Year'].mode()
        
        print('Earliest year is: {}'.format(earliest_year))
        print('Recent year is {}'.format(recent_year))
        print('Common year is{}'.format(common_year))
              
        
    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        cities, month_sel, day_sel = get_filters()
        df = load_data(cities, month_sel, day_sel)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        
        
        #To prompt the user whether they would like want to see the raw data
        enter = ['yes','no']
        user_input = input('Would you like to see more data? (Enter:Yes/No).\n')
        
        while user_input.lower() not in enter:
            user_input = input('Please Enter Yes or No:\n')
            user_input = user_input.lower()
        n = 0        
        while True :
            if user_input.lower() == 'yes':
        
                print(df.iloc[n : n + 5])
                n += 5
                user_input = input('\nWould you like to see more data? (Type:Yes/No).\n')
                while user_input.lower() not in enter:
                    user_input = input('Please Enter Yes or No:\n')
                    user_input = user_input.lower()
            else:
                break           


if __name__ == "__main__":
	main()


# In[ ]:




