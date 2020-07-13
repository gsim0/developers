"""
model.py

Author: Guillaume Simo, guillaume.simo@hotmail.fr
"""
from collections import Counter
import time

import pandas as pd

from src.tools import utils

def time_stats(df: pd.DataFrame):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: Display the most common month
    list_month = [start_time[5:7] for start_time in df['Start Time']]
    month = Counter(list_month).most_common(1)[0][0]
    list_months = [
        "january", "february", "march", "april", "may", "june", "july",
         "august", "september", "october", "november", "december"
    ]
    print(f'most common month: {list_months[int(month)]}')

    # TO DO: Display the most common day of week
    list_day = [utils.weekday_from_date(date) for date in df['Start Time']]
    day = Counter(list_day).most_common(1)[0][0]
    list_days = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
        "sunday"
    ]
    print(f'most common day of week: {list_days[day]}')
    # TO DO: Display the most common start hour
    list_hour = [date[14:16] for date in df['Start Time']]
    hour = Counter(list_hour).most_common(1)[0][0]
    print(f'most common start hour: {hour}')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df: pd.DataFrame):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: Display most commonly used start station
    start_station = Counter(df['Start Station']).most_common(1)[0][0]
    print(f'most commonly used start station: {start_station}')

    # TO DO: Display most commonly used end station
    end_station = Counter(df['End Station']).most_common(1)[0][0]
    print(f'most commonly used end station: {end_station}')

    # TO DO: Display most frequent combination of start station and end station trip
    list_start_end_station = [
        f'{start} to {end}'
        for start, end in zip(df['Start Station'], df['End Station'])
    ]
    start_end_station = Counter(list_start_end_station).most_common(1)[0][0]
    print('most frequent combination of start station'
          f'and end station trip: {start_end_station}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df: pd.DataFrame):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: Display total travel time
    tot_time_in_seconds = sum(df['Trip Duration'])
    tot_time_in_minutes = round(tot_time_in_seconds / 60, 2)
    tot_time_in_hours = round(tot_time_in_minutes / 60, 2)
    tot_time_in_days = round(tot_time_in_hours / 24, 2)
    print(f'total travel time in seconds {tot_time_in_seconds}\n'
          f'= {tot_time_in_minutes} minutes\n= {tot_time_in_hours} hours\n'
          f'= {tot_time_in_days} days')

    # TO DO: Display mean travel time
    mean_time_in_seconds = df['Trip Duration'].mean()
    mean_time_in_minutes = round(mean_time_in_seconds / 60, 2)
    mean_time_in_hours = round(mean_time_in_minutes / 60, 2)
    print(f'mean travel time in seconds {mean_time_in_seconds}\n'
          f'= {mean_time_in_minutes} minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df: pd.DataFrame):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(f"counts of user types: {df['User Type'].nunique()}")

    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        print(f"counts of gender: {df['Gender'].nunique()}")
    else:
        print('Gender column not available')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print(f"Earliest year of birth: {int(df['Birth Year'].min())}")
        print(f"Most recent year of birth: {int(df['Birth Year'].max())}")
        print("Most common year of birth: "
            f"{int(df['Birth Year'].value_counts().index[0])}")
    else:
        print('Birth Year column not available')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
