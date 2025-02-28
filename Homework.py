import flet as ft


class Homework(ft.Row):
    def __init__(self, homework_name, homework_time, homework_status_change, homework_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.completed = False
        self.homework_name = homework_name
        self.homework_time = homework_time
        self.homework_status_change = homework_status_change
        self.homework_delete = homework_delete

        self.display_homework = ft.Checkbox(value=False, label=f"{self.homework_name} - {self.homework_time} min",
                                            on_change=self.status_changed)
        self.edit_name = ft.TextField(expand=1)
        self.edit_time = ft.TextField(expand=1, hint_text="Time (min)")

        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [
            self.display_homework,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
        ]

        self.edit_view = ft.Row(visible=False, controls=[
            self.edit_name, self.edit_time,
            ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color=ft.colors.BLUE, tooltip="Save",
                          on_click=self.save_clicked),
        ])

    def toggle_edit(self, e):
        self.edit_name.value = self.homework_name
        self.edit_time.value = self.homework_time
        self.controls[0].visible = False
        self.edit_view.visible = True
        self.update()

    def save_clicked(self, e):
        self.homework_name = self.edit_name.value
        self.homework_time = self.edit_time.value
        self.display_homework.label = f"{self.homework_name} - {self.homework_time} min"
        self.controls[0].visible = True
        self.edit_view.visible = False
        self.update()

    def status_changed(self, e):
        self.completed = self.display_homework.value
        self.homework_status_change(self)

    def delete_clicked(self, e):
        self.homework_delete(self)


class HomeworkApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_homework = ft.TextField(hint_text="Enter your homework assignment", expand=True)
        self.new_homework_time = ft.TextField(hint_text="Time (min)", width=100)
        self.homeworks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All homework"), ft.Tab(text="Needs to be done"), ft.Tab(text="Already finished!")]
        )

        self.items_left = ft.Text("0 items left")

        self.controls = [
            ft.Row([ft.Text(value="Assignments", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[self.new_homework, self.new_homework_time,
                             ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)]),
            ft.Column(spacing=25, controls=[
                self.filter, self.homeworks,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[self.items_left,
                              ft.OutlinedButton(text="Clear already finished", on_click=self.clear_clicked)]
                ),
            ]),
        ]

    def add_clicked(self, e):
        if self.new_homework.value and self.new_homework_time.value:
            homework = Homework(self.new_homework.value, self.new_homework_time.value, self.homework_status_change,
                                self.homework_delete)
            self.homeworks.controls.append(homework)
            self.new_homework.value = ""
            self.new_homework_time.value = ""
            self.new_homework.focus()
            self.update()

    def homework_status_change(self, homework):
        self.update()

    def homework_delete(self, homework):
        self.homeworks.controls.remove(homework)
        self.update()

    def tabs_changed(self, e):
        self.update()

    def clear_clicked(self, e):
        for homework in list(self.homeworks.controls):
            if homework.completed:
                self.homework_delete(homework)

    def before_update(self):
        status = self.filter.tabs[self.filter.selected_index].text
        count = 0
        for homework in self.homeworks.controls:
            homework.visible = (
                    status == "All homework"
                    or (status == "Needs to be done" and not homework.completed)
                    or (status == "Already finished!" and homework.completed)
            )
            if not homework.completed:
                count += 1
        self.items_left.value = f"You have {count} homework assignment(s) left"


class Toodo():
    def main(page: ft.Page):
        page.bgcolor = ft.Colors.GREEN_300
        page.title = "Homework Reminders"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.add(HomeworkApp())

    ft.app(main)
