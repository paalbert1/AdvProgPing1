import flet as ft
import datetime
from flet.core import page

from ExtracurricWithUI import ExtracurricularApp

class Extracurricular(ft.Row):
    def __init__(self, Extracurricular_name, on_status_change, on_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.extracurricular_name = Extracurricular_name

        # Display extracurricular name checkbox
        self.display_extracurricular = ft.Checkbox(
            value=False,
            label=self.extracurricular_name,
            on_change=on_status_change
        )

        # Edit and delete buttons
        self.edit_button = ft.IconButton(
            icon=ft.icons.CREATE_OUTLINED,
            tooltip="Edit",
            on_click=self.toggle_edit
        )
        self.delete_button = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINE,
            tooltip="Delete",
            on_click=on_delete
        )

        # Edit view for renaming extracurricular
        self.edit_name = ft.TextField(expand=1)
        self.edit_view = ft.Row(
            visible=False,
            controls=[
                self.edit_name,
                ft.IconButton(

icon=ft.icons.DONE_OUTLINE_OUTLINED,
                    icon_color=ft.colors.BLUE,
                    tooltip="Save",
                    on_click=self.save_clicked
                ),
            ]
        )

        self.controls = [
            self.display_extracurricular,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
            self.edit_view
        ]

    def toggle_edit(self, e=None):
        self.edit_view.visible = not self.edit_view.visible
        self.update()

    def save_clicked(self, e=None):
        new_name = self.edit_name.value
        if new_name:
            self.extracurricular_name = new_name
            self.display_extracurricular.label = new_name
        self.edit_view.visible = False
        self.update()

def add_reminder():
    event = input("\nWhat extracurricular event would you like to set a reminder for? \nPlease enter the event here: ")
    date = input("Enter the date for your event (YYYY-MM-DD): ")

# used chat to help a bit with this step to make sure the date is valid
    try:
        event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.datetime.now()
        if event_date > current_date:
            print(f"Reminder added for '{event}' on {event_date.strftime('%A, %B %d, %Y')}")
        else:
            print("The event date should be in the future. Please try again.")
    except ValueError:
        print("Invalid date format. Please enter the date in YYYY-MM-DD format.")

# use loop to be able to create multiple reminders
def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_GREY_50
    page.title = "Your Personal Extracurricular Schedule"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.add(ExtracurricularApp())
    while True:
        add_reminder()
        cont = input("Do you want to add another reminder? (y/n): ").lower()
        if cont != 'y':
            print("You're all set")
            break

    ft.app(main)
# run the program
if __name__ == "__main__":
    main()