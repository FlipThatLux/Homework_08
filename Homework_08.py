from datetime import datetime, timedelta

users = [
         {'name': 'Sanders', 'birthday': datetime(year=1969, month=3, day=9)},
         {'name': 'Bluebarella', 'birthday': datetime(year=1985, month=3, day=13)},
         {'name': 'Helga', 'birthday': datetime(year=1970, month=3, day=9)},
         {'name': 'Dinosauria', 'birthday': datetime(year=1905, month=3, day=24)},
         {'name': 'Karen', 'birthday': datetime(year=1960, month=3, day=8)},
         {'name': 'Snitch', 'birthday': datetime(year=2000, month=3, day=22)},
         {'name': 'Jessica', 'birthday': datetime(year=2005, month=3, day=15)},
         {'name': 'Lolo', 'birthday': datetime(year=1995, month=3, day=14)},
         {'name': 'Wendeez', 'birthday': datetime(year=1982, month=3, day=14)},
         {'name': 'Gregor', 'birthday': datetime(year=2000, month=3, day=16)},
         {'name': 'Claudia', 'birthday': datetime(year=1999, month=3, day=13)},
         {'name': 'Policia', 'birthday': datetime(year=2009, month=3, day=17)}
         ]

def get_birthdays_per_week(users):

    this_weeks_birthday_boys = {}

    reference_monday = datetime(year=1900, month=1, day=1)
    reference_sunday = datetime(year=1900, month=1, day=7)
    now = datetime.now()
    weeks_since_reference = (now - reference_monday).days // 7
    current_week_monday = reference_monday + timedelta(weeks=weeks_since_reference)
    current_week_sunday = reference_sunday + timedelta(weeks=weeks_since_reference)
    
    for person in users:

        new_date = person['birthday'].replace(year=now.year)

        if current_week_monday <= new_date <= current_week_sunday:
            day = person['birthday'].strftime('%A')
            if day not in this_weeks_birthday_boys:
                this_weeks_birthday_boys[day] = []
            this_weeks_birthday_boys[day].append(person['name'])

    return this_weeks_birthday_boys

if __name__ == "__main__":

    bday_boys_by_day = get_birthdays_per_week(users)
    for weekday, boys in bday_boys_by_day.items():
        print('{:<9}: {}'.format(weekday, boys))