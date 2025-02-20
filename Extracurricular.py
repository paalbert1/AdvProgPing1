import flet as ft
import datetime
from flet.core import page
class Extracurricular(ft.Row):
    def __init__(self, Extracurricular_name, Extracurricular_status_change, Extracurricular_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.extracurricular_name = self.Extracurricular_name
        self.extracurricular_date = self.Extracurricular_date
        assert isinstance(self.extracurricular_date, object)

        self.display_homework = ft.Checkbox(value=False, label=self.Extracurricular_name, on_change=self.Extracurricular_status_change)
        self.edit_name = ft.TextField(expand=1)

        # Buttons for user to click on that call upon ui
        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [
            self.display_Extraxcurricular,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
        ]

        # Edit view controls for user to see
        self.edit_view = ft.Row(visible=False, controls=[
            self.edit_name,
            ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color=ft.colors.BLUE, tooltip="Save",
                          on_click=self.save_clicked),
        ])


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