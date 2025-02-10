import flet as ft
import datetime

class Extracurriculars(ft.Row):
    def __init__(self, extracurricular_name, extracurricular_date):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.extracurricular_name = None
        self.extracurricular_name = extracurricular_name
        self.extracurricular_date = extracurricular_date
        assert isinstance(self.extracurricular_date, object)
        self.display_Extracurriculars = ft.Checkbox(value=False, label=self.extracurricular_name)
        self.edit_name = ft.TextField(expand=1)
#start to add UI to this, try to have it look similar and function similar to homework section, same layout with different background color

        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [
            self.display_Extracurriculars,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
        ]
        self.edit_view = ft.Row(visible=False, controls=[
            self.edit_name,
            ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color=ft.colors.BLUE, tooltip="Save",
                          on_click=self.save_clicked),
        ])

        def toggle_edit(self, e):
            self.edit_name.value = self.display_Extracurriculars.label
            self.controls[0].visible = False
            self.edit_view.visible = True
            self.update()

        def save_clicked(self, e):
            self.display_Extracurriculars.label = self.edit_name.value
            self.controls[0].visible = True
            self.edit_view.visible = False
            self.update()

        def status_changed(self, e):
            self.completed = self.display_Extracurriculars.value
            self.extracurricular_status_change(self)

        def delete_clicked(self, e):
            self.extracurricular_delete(self)

            class ExtracurricularApp(ft.Column):
                def __init__(self):
                    super().__init__()
                    self.new_extracurricular = ft.TextField(hint_text="Enter your extracurricular and it's date here",
                                                     on_submit=self.add_clicked, expand=True)
                    self.extracurriculars = ft.Column()

                    # Filter all of the tabs to make it less confusing and keep simple
                    self.filter = ft.Tabs(
                        scrollable=False, selected_index=0, on_change=self.tabs_changed,
                        tabs=[ft.Tab(text="All extracurriculars"), ft.Tab(text="In the future"),
                              ft.Tab(text="Already done")]
                    )

                    self.items_left = ft.Text("0 items left")

                    self.controls = [
                        ft.Row([ft.Text(value="Extracurriculars", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                               alignment=ft.MainAxisAlignment.CENTER),
                        ft.Row(controls=[self.new_extracurricular,
                                         ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)]),
                        ft.Column(spacing=25, controls=[
                            self.filter, self.extracurriculars,
                            ft.Row(
                                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                                controls=[self.items_left,
                                          ft.OutlinedButton(text="Clear already done", on_click=self.clear_clicked)]
                            ),
                        ]),
                    ]

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