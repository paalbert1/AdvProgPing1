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
                self.update()  # ✅ Force UI refresh
            except ValueError:
                print("Invalid date format! Use YYYY-MM-DD.")

    def extracurricular_status_updated(self, extracurricular):
        self.update()
