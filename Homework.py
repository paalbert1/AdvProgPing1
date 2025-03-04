import flet as ft

class HomeworkApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.total_time = ft.Text(value="Total time: 0 min")
        self.new_homework = ft.TextField(hint_text="Enter Homework Task", expand=True)
        self.new_homework_time = ft.TextField(hint_text="Time (min)", width=100)
        self.homeworks = ft.Column()

        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All Homework"), ft.Tab(text="Needs to be done"), ft.Tab(text="Completed")]
        )

        self.items_left = ft.Text("0 tasks left")

        self.controls = [
            ft.Row([ft.Text(value="Assignments", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[self.new_homework, self.new_homework_time, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)]),
            self.total_time,
            self.filter,
            self.homeworks,
            ft.Row(
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[self.items_left, ft.OutlinedButton(text="Clear completed", on_click=self.clear_clicked)]
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
        for homework in self.homeworks.controls:
            homework.visible = (
                status == "All Homework"
                or (status == "Needs to be done" and not homework.completed)
                or (status == "Completed" and homework.completed)
            )
            if homework.visible:
                count += 1
        self.items_left.value = f"{count} homework task(s) left"
