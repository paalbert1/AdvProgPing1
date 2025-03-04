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

    # ✅ FIXED: `tabs_changed` function is now properly defined
    def tabs_changed(self, e):
        """Handles tab switching when users change categories."""
        self.before_update()
        self.update()

    def before_update(self):
        """Update UI based on the selected tab."""
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for extracurricular in self.extracurriculars.controls:
            extracurricular.visible = (
                status == "All Activities"
                or (status == "Upcoming" and not extracurricular.completed)
                or (status == "Past Events" and extracurricular.completed)
            )
            if extracurricular.visible:
                count += 1
        self.items_left.value = f"{count} event(s) left"
