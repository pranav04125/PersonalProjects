from datetime import date

with open(r"Reminder\reminders.txt", 'r') as file:
    reminder = file.readline()

    if reminder:
        reminder_date, reminder_txt = reminder.split("::")
        if str(date.today()) == reminder_date:
            print(reminder_txt)