import datetime

#start to add UI to this, try to have it look similar and function similar to homework section, same layout with different background color

def add_reminder():
    event = input("\nWhat extracurricular event would you like to set a reminder for? \nPlease enter the event here: ")
    date = input("Enter the date for your event (YYYY-MM-DD): ")

### used chat to help a bit with this step to make sure the date is valid
    try:
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.datetime.now()

        if event_date > current_date:
            print(f"Reminder added for '{event}' on {event_date.strftime('%A, %B %d, %Y')}")
        else:
            print("The event date should be in the future. Please try again.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

### use loop to be able to create multiple reminders
def main():
    print("Here you will be able to add a reminder for an upcoming event, you can add a game, practice, or any other event you may need to plan for.")

    while True:
        add_reminder()
        cont = input("Do you want to add another reminder? (y/n): ").lower()
        if cont != 'y':
            print("You're all set")
            break

### run the program
if __name__ == "__main__":
    main()