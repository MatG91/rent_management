import csv
from datetime import datetime

# function used by the class Reservation to check if a new reservation overlaps with the old ones


def check_overlap(start_date, end_date):
    with open('reservations.csv', newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            reservation_start = datetime.strptime(
                row['start_date'], '%Y-%m-%d').date()
            reservation_end = datetime.strptime(
                row['end_date'], '%Y-%m-%d').date()
            if (start_date >= reservation_start and start_date <= reservation_end) or (end_date >= reservation_start and end_date <= reservation_end):
                print(
                    f'The property is reserved from {reservation_start} to {reservation_end}, pls book another date\n')
                return False
    return True
