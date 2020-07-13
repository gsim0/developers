"""
utils.py

Utils (e.g. reusable functions).

Author: Guillaume Simo, guillaume.simo@hotmail.fr
"""
from datetime import datetime
from typing import List


def test_input(var: str, var_str: str, available_var: List[str]):
    """
    Test if the input variables (specify by the users have the correct format
    and values).

    Args:
        (str) var - input variable to test
        (str) var_str - name of the input variable, to be displayed on the error
                        msg
        (list) available_var - possible values the input variable can have
    """
    assert isinstance(var, str) and var.lower() in available_var, \
        f"{var}: {var_str} as to be str among {available_var}!"


def weekday_from_date(date: str) -> int:
    """
    Return the day of the week (int from 0 to 6) of the input date

    Args:
        (str) date - example: 2020-07-12 21:25:45
    Returns:
        (int) weekday - day of the week as integer (0-6: Monday-Sunday)
    """
    return datetime.strptime(date, '%Y-%m-%d %H:%M:%S').weekday()
