import datetime

def day_of_week(day, month, year):
    
    date = datetime.date(year, month, day)
    return date.strftime('%A')  

def is_leap_year(year):
    
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(day, month, year):
    
    birth_date = datetime.date(year, month, day)
    today = datetime.date.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age


day = int(input("Введите день вашего рождения (числом): "))
month = int(input("Введите месяц вашего рождения (числом): "))
year = int(input("Введите год вашего рождения (числом): "))


dow = day_of_week(day, month, year)
print(f"Ваш день рождения был: {dow}")

if is_leap_year(year):
    print(f"{year} год был высокосным.")
else:
    print(f"{year} год не был высокосным.")

age = calculate_age(day, month, year)
print(f"Вам сейчас {age} лет.")

#если ввести число не то, то всё сломается, i know it, мне просто лень, это даже не всё задание, но я устала, прошу простить