import flet as ft
import datetime

class ExtracurricularApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_extracurricular = ft.TextField(hint_text="Enter Activity Name", expand=True)
        self.extracurricular_date = ft.TextField(hint_text="Event Date (YYYY-MM-DD)", width=150)
        self.extracurriculars = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All Activities"), ft.Tab(text="Upcoming"), ft.Tab(text="Past Events")]
        )

        self.items_left = ft.Text("0 activities left")

        self.controls = [
            ft.Row([ft.Text(value="Extracurriculars", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[self.new_extracurricular, self.extracurricular_date, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)]),
            self.filter,
            self.extracurriculars,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[self.items_left, ft.OutlinedButton(text="Clear past events", on_click=self.clear_clicked)]
            ),
        ]

    # ✅ FIXED: `add_clicked` function is now properly defined
    def add_clicked(self, e):
        """Adds a new extracurricular event with a date."""
        if self.new_extracurricular.value and self.extracurricular_date.value:
            try:
                event_date = datetime.datetime.strptime(self.extracurricular_date.value, "%Y-%m-%d")
                extracurricular = Extracurricular(
                    self.new_extracurricular.value,
                    event_date,
                    self.extracurricular_status_updated,
                    self.extracurricular_delete
                )
                self.extracurriculars.controls.append(extracurricular)  # ✅ Add new event to UI
                self.new_extracurricular.value = ""  # Clear input field
                self.extracurricular_date.value = ""  # Clear date input field
                try:
                    self.update()  # ✅ Force UI refresh
                except Exception as e:
                    print(f'Error: {e}')
            except ValueError:
                print("Invalid date format. Please enter YYYY-MM-DD.")

    # ✅ FIXED: `tabs_changed` function is now properly included
    def tabs_changed(self, e):
        """Handles tab switching when users change categories."""
        selected_tab = self.filter.selected_index

        if selected_tab == 0:  # "All Activities"
            for item in self.extracurriculars.controls:
                item.visible = True
        elif selected_tab == 1:  # "Upcoming"
            for item in self.extracurriculars.controls:
                if hasattr(item, 'event_date') and item.event_date >= datetime.datetime.now():
                    item.visible = True
                else:
                    item.visible = False
        elif selected_tab == 2:  # "Past Events"
            for item in self.extracurriculars.controls:
                if hasattr(item, 'event_date') and item.event_date < datetime.datetime.now():
                    item.visible = True
                else:
                    item.visible = False

        self.update()  # Refresh UI

