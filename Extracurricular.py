import flet as ft
import datetime
import json
import os
from flet.core import page
from ExtracurricWithUI import ExtracurricularApp


#where data will be saved
DATA_FILE = "extracurricular_data.json"

#Load data from the file
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    return {"extracurriculars": [], "reminders": []}

# Save data to the file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

#define class and initialize it
class Extracurricular(ft.Row):
    def __init__(self, Extracurricular_name, on_status_change, on_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)

        self.completed = False
        self.on_status_change = on_status_change
        self.on_delete = on_delete
        self.extracurricular_name = Extracurricular_name

        self.display_extracurricular = ft.Checkbox(
            value=False,
            label=self.extracurricular_name,
            on_change=self.status_changed  # Local handler
        )

    def status_changed(self, e):
        self.completed = self.display_extracurricular.value  # Update based on checkbox value
        self.on_status_change(self)

        # Display extracurricular name checkbox
        self.display_extracurricular = ft.Checkbox(
            value=False,
            label=self.extracurricular_name,
        )

        # Edit and delete buttons
        self.edit_button = ft.IconButton(
            icon=ft.icons.CREATE_OUTLINED,
            tooltip="Edit",
            on_click=self.toggle_edit
        )
        self.delete_button = ft.IconButton(
            icon=ft.icons.DELETE_OUTLINED,
            tooltip="Delete",
            on_click=self.toggle_delete
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

    def toggle_delete(self, e=None):
        if self in self._control_parent.controls:
            self._control_parent.controls.remove(self)
            self._control_parent.update()
        self.on_delete(self)

    def save_clicked(self, e=None):
        new_name = self.edit_name.value
        if new_name:
            self.extracurricular_name = new_name
            self.display_extracurricular.label = new_name
        self.edit_view.visible = False
        self.update()

    def homework_status_change(self, homework):
        self.update()


#date input in correct format
def add_reminder(page):
    event_input = ft.TextField(label="Event Name")
    date_input = ft.TextField(label="Event Date (YYYY-MM-DD)")

    def on_add_reminder_click(e):
        event = event_input.value
        date = date_input.value

        # make sure the date input is correct, can't be in the past
        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            current_date = datetime.datetime.now()
            if event_date > current_date:
                page.add(ft.Text(f"Reminder added for '{event}' on {event_date.strftime('%A, %B %d, %Y')}", color=ft.colors.WHITE))

                # Save the reminder data to file
                data = load_data()
                data["reminders"].append({"event": event, "date": date})
                save_data(data)

            else:
                page.add(ft.Text("The event date should be in the future. Please try again.", color=ft.colors.RED))
        except ValueError:
            page.add(ft.Text("Invalid date format. Please enter the date in YYYY-MM-DD format.", color=ft.colors.RED))

    # create UI elements
    page.add(
        ft.Column(
            [
                ft.Text("Enter Extracurricular Event and Date"),
                event_input,
                date_input,
                ft.ElevatedButton("Add Reminder", on_click=on_add_reminder_click)
            ]
        )
    )


# Allow user to switch between tabs to see progress of event
def tabs_changed(self, e):
    self.update()


# Clear selected events if they are done or no longer needed
def clear_clicked(self, e):
    for extracurricular in list(self.extracurriculars.controls):
        if extracurricular.completed:
            self.extracurricular_delete(extracurricular)


def before_update(self):
    status = self.filter.tabs[self.filter.selected_index].text
    count = 0  # Initialize count variable

    for extracurricular in self.Extracurricular.controls:
        extracurricular.visible = (
                status == "All Extracurriculars"
                or (status == "In the future" and not extracurricular.completed)
                or (status == "Past events" and extracurricular.completed)
        )
        if extracurricular.visible:
            count += 1

    self.items_left.value = f"{count} items left"


# General UI
def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_300
    page.title = "Your Personal Extracurricular Schedule"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # Load previously saved extracurriculars
    data = load_data()
    for extracurricular in data["extracurriculars"]:
        # Assuming the data structure has a list of extracurricular names to recreate them
        page.add(Extracurricular(extracurricular["name"], on_status_change=update_extracurricular, on_delete=delete_extracurricular))

    page.add(ExtracurricularApp())

    add_reminder(page)


def update_extracurricular(extracurricular):
    # Update data when extracurricular status changes
    data = load_data()
    # You can update the list of extracurriculars here if needed
    save_data(data)


def delete_extracurricular(extracurricular):
    # Remove extracurricular from the list and save it
    data = load_data()
    data["extracurriculars"] = [e for e in data["extracurriculars"] if e["name"] != extracurricular.extracurricular_name]
    save_data(data)


ft.app(target=main)
