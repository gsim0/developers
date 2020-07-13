"""
main.py

Central point of the project.

Author: Guillaume Simo, guillaume.simo@hotmail.fr
"""
from src.data import import_prepare_data as ipd
from src.models import model


CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'
             }


def main():
    """
    main()
    """
    while True:
        city, month, day = ipd.get_filters()
        df = ipd.load_data(city, month, day)

        model.time_stats(df)
        model.station_stats(df)
        model.trip_duration_stats(df)
        model.user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
