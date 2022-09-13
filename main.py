from datetime import date
from application import salary
from application.db import people as pee
from quickstart import authorization

def get_date():
    cur_date = date.today()
    return cur_date

if __name__ == '__main__':
    print(get_date())
    salary.calculate_salary()
    pee.get_employees()
    authorization()


