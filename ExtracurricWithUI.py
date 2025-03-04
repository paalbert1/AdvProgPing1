import flet as ft
import datetime

class Extracurricular(ft.Row):
    def __init__(self, extracurricular_name, extracurricular_date, extracurricular_status_change, extracurricular_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.completed = False
        self.extracurricular_name = extracurricular_name
        self.extracurricular_date = extracurricular_date
        self.extracurricular_status_change = extracurricular_status_change
        self.extracurricular_delete = extracurricular_delete

        self.display_extracurriculars = ft.Checkbox(
            value=False,
            label=f"{self.extracurricular_name} - {self.extracurricular_date.strftime('%Y-%m-%d')}",
            on_change=self.status_changed
        )

        self.edit_name = ft.TextField(expand=1)
        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [self.display_extracurriculars, ft.Row(spacing=0, controls=[self.edit_button, self.delete_button])]

    def toggle_edit(self, e):
        self.edit_name.value = self.display_extracurriculars.label
        self.controls[0].visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_extracurriculars.value
        self.extracurricular_status_change(self)

    def delete_clicked(self, e):
        self.extracurricular_delete(self)

class ExtracurricularApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_extracurricular = ft.TextField(hint_text="Enter Activity Name", expand=True)
        self.extracurricular_date = ft.TextField(hint_text="Event Date (YYYY-MM-DD)", width=150)
        self.extracurriculars = ft.Column()

        # ✅ FIXED: `tabs_changed` method is now properly defined
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

    # ✅ FIXED: `tabs_changed` function is now defined
    def tabs_changed(self, e):
        """Handles tab switching when users change categories."""
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

    def extracurricular_delete(self, extracurricular):
        # Remove the extracurricular from the list
        self.extracurriculars.controls.remove(extracurricular)
        self.update()

    def clear_clicked(self, e):
        for extracurricular in list(self.extracurriculars.controls):
            if extracurricular.completed:
                self.extracurricular_delete(extracurricular)
