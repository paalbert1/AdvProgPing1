# Redo UI to match Homework app UI closely so it is simplistic and easy for user to understand
import signal
import flet as ft
import datetime

def handler(signum, frame):
    print(f"signal {signum} received")

import sys
if sys.platform != "win32":
    signal.signal(signal.SIGINT, handler)


class Extracurricular(ft.Row):
    def __init__(self, extracurricular_name, extracurricular_date, extracurricular_status_change):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.completed = None
        self.extracurricular_name = extracurricular_name
        self.extracurricular_date = extracurricular_date
        self.extracurricular_status_change = extracurricular_status_change
        assert isinstance(self.extracurricular_date, object)

        self.display_Extracurriculars = ft.Checkbox(value=False, label=self.extracurricular_name,
                                                    on_change=self.status_changed)
        self.edit_name = ft.TextField(expand=1)
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

        self.controls.append(self.edit_view)

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

    def extracurricular_status_change(self, extracurricular):
        self.update()
        self.extracurricular_status_change(self)
        #need to add here

    def extracurricular_delete(self, extracurricular):
        self.extracurricular_delete(self)
        #need to add here

class ExtracurricularApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_extracurricular = ft.TextField(hint_text="Enter your extracurricular and its date here",
                                                on_submit=self.add_clicked, expand=True)
        self.extracurriculars = ft.Column()

        # Filter all of the tabs to make it less confusing and keep it simple
        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All extracurriculars"), ft.Tab(text="In the future"), ft.Tab(text="Past events")]
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

    def add_clicked(self, e):
        extracurricular_name = self.new_extracurricular.value
        extracurricular_date = datetime.datetime.now()  # Replace with actual date input if needed
        self.extracurriculars.controls.append(Extracurricular(extracurricular_name, extracurricular_date, extracurricular_status_change= None))
        self.new_extracurricular.value = ""
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for Extracurricular in list(self.extracurriculars.controls):
            if Extracurricular.completed:
                self.extracurricular_delete(Extracurricular)
       
    def extracurricular_delete(self, extracurricular):
        # Remove the extracurricular from the list
        self.extracurriculars.controls.remove(extracurricular)
        self.update()

def main(page: ft.Page):
    app = ExtracurricularApp()
    page.bgcolor = ft.Colors.INDIGO_200
    page.title = "Extracurricular Schedule"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE
    page.add(ExtracurricularApp())

ft.app(main)