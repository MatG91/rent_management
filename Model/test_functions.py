# This is a test module to run tests of functions.py
from datetime import datetime
from functions import check_overlap

# calling function check_overlap and give them possible args
print(check_overlap(datetime.strptime('2023-03-18', '%Y-%m-%d').date(),
      datetime.strptime('2023-03-30', '%Y-%m-%d').date()))
