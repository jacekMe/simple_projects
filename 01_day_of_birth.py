import datetime
import calendar

# code only for python 3.10
# def translate_to_polish(day_name):
#     match day_name:
#         case 'Monday':
#             return 'Poniedziałek'
#         case 'Tuesday':
#             return 'Wtorek'
#         case 'Wednesday':
#             return 'Środa'
#         case 'Thursday':
#             return 'Czwartek'
#         case 'Friday':
#             return 'Piątek'
#         case 'Saturday':
#             return 'Sobota'
#         case 'Sunday':
#             return 'Niedziela'

def translate_to_polish_v2(day_name):
    english_to_polish_day_name = {
        'Monday': 'Poniedziałek',
        'Tuesday': 'Wtorek',
        'Wednesday': 'Środa',
        'Thursday': 'Czwartek',
        'Friday': 'Piątek',
        'Saturday': 'Sobota',
        'Sunday': 'Niedziela'
    }

    return english_to_polish_day_name[day_name]
date_of_birth = input("Podaj datę urodzin (dd-mm-yyyy): ")
day, month, year = date_of_birth.split("-")

date_of_birth = datetime.datetime(int(year), int(month), int(day))

day_name = calendar.day_name[date_of_birth.weekday()]
print(day_name)
print(translate_to_polish_v2(day_name))
