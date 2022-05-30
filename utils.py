"""
Created on 2022-05-30
@author: chy
"""


def calculate_threshold_date(original_date, years_to_add):
    new_date = original_date.replace(year=original_date.year + years_to_add)
    return new_date
