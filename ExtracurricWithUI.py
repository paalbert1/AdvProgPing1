import flet as ft
import datetime

class Extracurricular(ft.Row):
    def __init__(self, extracurricular_name, extracurricular_status_change, extracurricular_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.completed = False
        self.extracurricular_name = extracurricular_name
        self.extracurricular_status_change = extracurricular_status_change
        self.extracurricular_delete = extracurricular_delete

        # ✅ Fix: Ensure the checkbox updates properly
        self.display_extracurriculars = ft.Checkbox(
            value=False,
            label=self.extracurricular_name,
            on_change=self.status_changed
        )
        self.edit_name = ft.TextField(expand=1)
        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [
            self.display_extracurriculars,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
        ]

        self.edit_view = ft.Row(visible=False, controls=[
            self.edit_name,
            ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color=ft.colors.BLUE, tooltip="Save",
                          on_click=self.save_clicked),
        ])

        self.controls.append(self.edit_view)

    def toggle_edit(self, e):
        self.edit_name.value = self.display_extracurriculars.label
        self.controls[0].visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.extracurricular_name = self.edit_name.value
        self.display_extracurriculars.label = self.extracurricular_name
        self.controls[0].visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_extracurriculars.value
        self.extracurricular_status_change(self)

    def delete_clicked(self, e):
        self.extracurricular_delete(self)

class ExtracurricularApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_extracurricular = ft.TextField(hint_text="Enter your event(s) here", expand=True)
        self.extracurriculars = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All extracurriculars"), ft.Tab(text="In the future"), ft.Tab(text="Already finished!")]
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
                              ft.OutlinedButton(text="Clear completed", on_click=self.clear_clicked)]
                ),
            ]),
        ]

    def add_clicked(self, e):
        extracurricular_name = self.new_extracurricular.value
        extracurricular = Extracurricular(
            extracurricular_name=extracurricular_name,
            extracurricular_status_change=self.extracurricular_status_updated,
            extracurricular_delete=self.extracurricular_delete,
        )
        self.extracurriculars.controls.append(extracurricular)
        self.new_extracurricular.value = ""
        self.update()

    def extracurricular_status_updated(self, extracurricular):
        self.update()

    def extracurricular_delete(self, extracurricular):
        self.extracurriculars.controls.remove(extracurricular)
        self.update()

    def clear_clicked(self, e):
        for extracurricular in list(self.extracurriculars.controls):
            if extracurricular.completed:
                self.extracurricular_delete(extracurricular)
