import flet as ft
import self


class Homework(ft.Column):
    def __init__(self, homework_name, homework_status_change, homework_delete):
        super().__init__()
        self.homework_status_changed = None
        self.completed = False
        self.homework_name = homework_name
        self.homework_status_change = homework_status_change
        self.homework_delete = homework_delete
        self.display_homework = ft.Checkbox
            value=False, label=self.homework_name, on_change=self.homework_status_changed
        )
        self.edit_name = ft.TextField(expand=1)

        self.display_view = ft.Row(
            alignment = ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment = ft.CrossAxisAlignment.CENTER,
            controls = [
                    self.display_homework,
                    ft.Row(
                        spacing=0,
                        controls=[
                             ft.IconButton(
                                icon=ft.icons.CREATE_OUTLINED,
                                tooltip="Edit Homework-Task",
                                on_click=self.edit_clicked,
                             ),
                             ft.IconButton(
                                ft.icons.DELETE_OUTLINE,
                                tooltip="Delete Homework-Task",
                                on_click=self.delete_clicked,
                            ),
                        ],
                    ),
                ],
            )
