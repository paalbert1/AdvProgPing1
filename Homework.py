# import flet
import flet as ft
from flet.core import page

# create and initialize class that defines homework name, homework status, and homework delete
class Homework(ft.Row):
    def __init__(self, homework_name, homework_status_change, homework_delete):
        super().__init__(alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.completed = False
        self.homework_name = homework_name
        self.homework_status_change = homework_status_change
        self.homework_delete = homework_delete

        # Display all of the necessary controls for UI
        self.display_homework = ft.Checkbox(value=False, label=self.homework_name, on_change=self.status_changed)
        self.edit_name = ft.TextField(expand=1)

        # Buttons for user to click on that call upon ui
        self.edit_button = ft.IconButton(icon=ft.icons.CREATE_OUTLINED, tooltip="Edit", on_click=self.toggle_edit)
        self.delete_button = ft.IconButton(icon=ft.icons.DELETE_OUTLINE, tooltip="Delete", on_click=self.delete_clicked)

        self.controls = [
            self.display_homework,
            ft.Row(spacing=0, controls=[self.edit_button, self.delete_button]),
        ]

        # Edit view controls for user to see
        self.edit_view = ft.Row(visible=False, controls=[
            self.edit_name,
            ft.IconButton(icon=ft.icons.DONE_OUTLINE_OUTLINED, icon_color=ft.colors.BLUE, tooltip="Save",
                          on_click=self.save_clicked),
        ])

    # define edit function to allow edit access to previous inputs
    def toggle_edit(self, e):
        self.edit_name.value = self.display_homework.label
        self.controls[0].visible = False
        self.edit_view.visible = True
        self.update()

    # define saving function to save after each input/action by user
    def save_clicked(self, e):
        self.display_homework.label = self.edit_name.value
        self.controls[0].visible = True
        self.edit_view.visible = False
        self.update()

    # define status function to display changes made after edits
    def status_changed(self, e):
        self.completed = self.display_homework.value
        self.homework_status_change(self)

    # define delete function to let the user get rid of unwanted assignments
    def delete_clicked(self, e):
        self.homework_delete(self)

# create and initiate a second class for directional pieces mostly some UI displays
class HomeworkApp(ft.Column):
    def __init__(self):
        super().__init__()
        self.new_homework = ft.TextField(hint_text="Enter your homework assignment and it's due date here", on_submit=self.add_clicked, expand=True)
        self.homeworks = ft.Column()

        # Filter all of the tabs to make it less confusing and keep the app simple for easy user interactions
        self.filter = ft.Tabs(
            scrollable=False, selected_index=0, on_change=self.tabs_changed,
            tabs=[ft.Tab(text="All homework"), ft.Tab(text="Needs to be done"), ft.Tab(text="Already finished!")]
        )

        self.items_left = ft.Text("0 items left")

        self.controls = [
            ft.Row([ft.Text(value="Assignments", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[self.new_homework, ft.FloatingActionButton(icon=ft.icons.ADD, on_click=self.add_clicked)]),
            ft.Column(spacing=25, controls=[
                self.filter, self.homeworks,
                ft.Row(
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN, vertical_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[self.items_left, ft.OutlinedButton(text="Clear already finished", on_click=self.clear_clicked)]
                ),
            ]),
        ]

    # define function to allow new homework to be added easily and have it update the previous list of assignments if there is any put in by user already
    def add_clicked(self, e):
        if self.new_homework.value:
            homework = Homework(self.new_homework.value, self.homework_status_change, self.homework_delete)
            self.homeworks.controls.append(homework)
            self.new_homework.value = ""
            self.new_homework.focus()
            self.update()

    # define status change of ongoing assignments to show what needs to be done vs already done
    def homework_status_change(self, homework):
        self.update()

    # define delete function to allow user to delete unwanted assignments
    def homework_delete(self, homework):
        self.homeworks.controls.remove(homework)
        self.update()

    # define tab function to switch between the tabs
    def tabs_changed(self, e):
        self.update()

    # define clear function to get rid of completed assignments if the user wants to
    def clear_clicked(self, e):
        for homework in list(self.homeworks.controls):  # Avoid modifying while iterating
            if homework.completed:
                self.homework_delete(homework)

    # define function and label the status options
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
        self.items_left.value = f"you have {count} homework assignment(s) left"

# define main function to run code and finish UI with background color, title, and alignments if necessary
class Toodo():
    print("blahblah")
    def main(page: ft.Page):
        page.bgcolor = ft.Colors.INDIGO_200
        page.title = "Homework Reminders"
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        page.scroll = ft.ScrollMode.ADAPTIVE
        page.add(HomeworkApp())
    ft.app(main)
