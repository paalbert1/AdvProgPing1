import os
import flet as ft
import psycopg2
from ExtracurricWithUI import ExtracurricularApp  # ✅ Correct Import
from Homework import HomeworkApp  # ✅ Correct Import

# ✅ Connect to PostgreSQL database (Heroku provides DATABASE_URL)
DATABASE_URL = os.environ.get("DATABASE_URL")  # Heroku provides this automatically
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# ✅ Create users table if it does not exist
cursor.execute("CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, name TEXT)")
conn.commit()

# ✅ Function to save user to database
def save_user_to_db(name):
    cursor.execute("INSERT INTO users (name) VALUES (%s)", (name,))
    conn.commit()

# ✅ MAIN FLET FUNCTION (NOW CONNECTED TO EXTRACURRICULAR & HOMEWORK)
def mains(page: ft.Page):
    page.title = "Pingree Planner"
    page.bgcolor = ft.Colors.INDIGO_300

    # STEP 1️⃣: Ask for user's name
    def submit_name(e):
        save_user_to_db(name_input.value)  # Save to database
        page.clean()  # Remove name input UI
        show_main_ui(name_input.value)  # Show the main UI with dropdown menu
        page.update()

    # UI Elements for Name Input
    name_input = ft.TextField(label="Enter your name", text_align=ft.TextAlign.CENTER)
    submit_button = ft.ElevatedButton("Submit", on_click=submit_name)

    # Display Name Input UI
    page.add(
        ft.Column(
            [
                ft.Row([ft.Text("Welcome to the Pingree Planner!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([name_input], alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([submit_button], alignment=ft.MainAxisAlignment.CENTER),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

    # STEP 2️⃣: Show Full UI (Dropdown for Homework, Calendar, Extracurriculars)
    def show_main_ui(name):
        page.clean()  # Clear the screen
        page.bgcolor = ft.Colors.BLUE_50

        welcome_text = ft.Text(value=f"Welcome, {name}!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)

        # ✅ Dynamic content area (so menu actions update this instead of closing)
        content_area = ft.Column()

        # ✅ Show Extracurriculars Page
        def show_extracurriculars(e):
            content_area.controls.clear()
            content_area.update()  # ✅ Force UI refresh before adding new content
            try:
                extracurriculars_page = ExtracurricularApp()
                content_area.controls.append(ft.Text("Extracurriculars"))
                content_area.controls.append(extracurriculars_page)  # ✅ Ensure a new instance is created
                page.update()
            except Exception as err:
                content_area.controls.append(ft.Text(f"Error loading Extracurriculars: {err}", color=ft.colors.RED))
                page.update()

        # ✅ Show Homework (To-Do List)
        def show_todo(e):
            content_area.controls.clear()
            content_area.update()  # ✅ Force UI refresh before adding new content
            try:
                homework_page = HomeworkApp()  # ✅ Ensure a new instance is created
                content_area.controls.append(ft.Text("To-Do List"))
                content_area.controls.append(homework_page)
                page.update()
            except Exception as err:
                content_area.controls.append(ft.Text(f"Error loading To-Do List: {err}", color=ft.colors.RED))
                page.update()

        # ✅ Show Calendar (Placeholder)
        def show_calendar(e):
            content_area.controls.clear()
            content_area.controls.append(ft.Text("Calendar Page"))
            page.update()

        # ✅ FIXED: Dropdown menu (wrapped in a visible Row)
        menu = ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.PopupMenuButton(
                    icon_color=ft.colors.WHITE,
                    items=[
                        ft.PopupMenuItem(text="Calendar", on_click=show_calendar),
                        ft.PopupMenuItem(text="To-Do lists", on_click=show_todo),  # ✅ Corrected
                        ft.PopupMenuItem(text="Manage Extracurriculars", on_click=show_extracurriculars)  # ✅ Corrected
                    ]
                )
            ]
        )

        # ✅ Full UI with dropdown menu + content area for navigation
        page.add(
            ft.Column(
                [
                    ft.Row([welcome_text], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([ft.Text("Click the dropdown menu to access features!", theme_style=ft.TextThemeStyle.BODY_LARGE)], alignment=ft.MainAxisAlignment.CENTER),
                    menu,  # ✅ FIXED: Now wrapped in a Row
                    content_area  # ✅ This will update dynamically when menu items are clicked
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            )
        )

# ✅ Ensure Heroku binds to the correct port
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    ft.app(
        target=mains,
        view=ft.WEB_BROWSER,
        host="0.0.0.0",
        port=port
    )
