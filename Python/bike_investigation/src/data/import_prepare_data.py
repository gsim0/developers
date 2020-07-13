"""
import_prepare_data.py

Script to import and processd data.

Author: Guillaume Simo, guillaume.simo@hotmail.fr
"""
import os
from typing import Tuple
import zipfile

import pandas as pd

from src.tools import utils

def get_filters() -> Tuple[str, str, str]:
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington).
    #  HINT: Use a while loop to handle invalid inputs
    available_cities = ["chicago", "new york city", "washington"]

    city = input(f"Specify a city among {available_cities}:")
    utils.test_input(var=city, var_str='city', available_var=available_cities)
    city = city.lower().replace(' ', '_')
    print(city)

    # TO DO: get user input for month (all, january, february, ... , june)
    available_months = [
        "january", "february", "march", "april", "may", "june", "july",
        "august", "september", "october", "november", "december"
    ]
    month = input(f"Specify a month among {available_months}:")
    utils.test_input(var=month, var_str='month', available_var=available_months)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    available_days = [
        "monday", "tuesday", "wednesday", "thursday", "friday", "saturday",
        "sunday"
    ]
    day = input(f"Specify a day of week among {available_days}:")
    utils.test_input(var=day, var_str='day', available_var=available_days)

    print('-'*40)
    return city, month, day


def load_data(city: str, month: str, day: str) -> pd.DataFrame:
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    cwd = os.getcwd()
    zip_path = os.path.join(cwd, 'data',
                            'Bike_raw_data.zip')
    zf = zipfile.ZipFile(zip_path)
    df = pd.read_csv(zf.open(f'{city}.csv'))
    return df
