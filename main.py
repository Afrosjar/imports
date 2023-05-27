from application.db.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


def main():
    print(datetime.today())
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
