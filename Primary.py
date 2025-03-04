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
        user_name.value = f"Hello, {name_input.value}!"
        page.clean()  # Remove name input UI
        show_main_ui(name_input.value)  # Show the main UI with dropdown menu
        page.update()

    # UI Elements for Name Input
    name_input = ft.TextField(label="Enter your name", text_align=ft.TextAlign.CENTER)
    submit_button = ft.ElevatedButton("Submit", on_click=submit_name)
    user_name = ft.Text(value="Hello!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)

    # Display Name Input UI
    page.add(name_input, submit_button, user_name)

    # STEP 2️⃣: Show Full UI (Dropdown for Homework, Calendar, etc.)
    def show_main_ui(name):
        page.clean()  # Clear the screen
        page.bgcolor = ft.Colors.INDIGO_500

        welcome_text = ft.Text(value=f"Welcome, {name}!", theme_style=ft.TextThemeStyle.HEADLINE_MEDIUM)

        def Todo(e):
            page.window.close()

        def ExtraCuriculars(e):
            page.window.close()

        def calender(e):
            page.window.close()

        pb = ft.PopupMenuButton(
            items=[
                ft.PopupMenuItem(text="Calendar", on_click=calender),
                ft.PopupMenuItem(text="To-Do lists", on_click=Todo),
                ft.PopupMenuItem(text="Manage Extracurriculars", on_click=ExtraCuriculars)
            ]
        )

        # Add UI elements to the page
        page.add(
            ft.Row([welcome_text], alignment=ft.MainAxisAlignment.CENTER),
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
