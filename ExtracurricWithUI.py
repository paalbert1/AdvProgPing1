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

    def tabs_changed(self, e):
        """Handles tab switching when users change categories."""
        self.update()

    def clear_clicked(self, e):
        """Removes all completed extracurriculars from the list."""
        for extracurricular in list(self.extracurriculars.controls):
            if extracurricular.completed:
                self.extracurricular_delete(extracurricular)
        self.update()

    def add_clicked(self, e):
        try:
            event_date = datetime.datetime.strptime(self.extracurricular_date.value, "%Y-%m-%d")
            extracurricular = Extracurricular(self.new_extracurricular.value, event_date, self.extracurricular_status_updated, self.extracurricular_delete)
            self.extracurriculars.controls.append(extracurricular)
            self.new_extracurricular.value = ""
            self.extracurricular_date.value = ""
            self.update()
        except ValueError:
            print("Invalid date format!")

    def extracurricular_status_updated(self, extracurricular):
        self.update()
