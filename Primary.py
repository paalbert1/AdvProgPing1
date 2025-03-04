import os
import flet as ft
import psycopg2

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

# ✅ MAIN FLET FUNCTION (MERGED VERSION)
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

    # STEP 2️⃣: Show Full UI (Dropdown for Homework, Calendar, etc.)
    def show_main_ui(name):
        page.clean()  # Clear the screen
        page.bgcolor = ft.Colors.INDIGO_500

        welcome_text = ft.Text(value=f"Welcome, {name}!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)

        # ✅ Functions for dropdown menu actions
        def Todo(e):
            print("To-Do clicked")
            page.window.close()

        def ExtraCuriculars(e):
            print("Extracurriculars clicked")
            page.window.close()

        def calender(e):
            print("Calendar clicked")
            page.window.close()

        # ✅ Dropdown menu (fully restored)
        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Calendar", on_click=calender),
                ft.PopupMenuItem(text="To-Do lists", on_click=Todo),
                ft.PopupMenuItem(text="Manage Extracurriculars", on_click=ExtraCuriculars)
            ]
        )

        # ✅ Full UI with dropdown menu (fully restored)
        page.add(
            ft.Row([welcome_text], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([ft.Text("Click the dropdown menu to access features!", theme_style=ft.TextThemeStyle.BODY_LARGE)], alignment=ft.MainAxisAlignment.CENTER),
            ft.Row([pb], alignment=ft.MainAxisAlignment.CENTER)
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
