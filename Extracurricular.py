import flet as ft
import datetime
import json
import os
import psycopg2
from ExtracurricWithUI import ExtracurricularApp

# ✅ Connect to PostgreSQL database instead of using JSON files
DATABASE_URL = os.environ.get("DATABASE_URL")  # Provided by Heroku
conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cursor = conn.cursor()

# ✅ Create a table to store extracurricular activities if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS extracurriculars (
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        completed BOOLEAN DEFAULT FALSE
    )
""")
conn.commit()

# ✅ Load extracurriculars from PostgreSQL instead of JSON
def load_extracurriculars():
    cursor.execute("SELECT name, completed FROM extracurriculars")
    return [{"name": row[0], "completed": row[1]} for row in cursor.fetchall()]

# ✅ Save extracurricular to PostgreSQL
def save_extracurricular(name):
    cursor.execute("INSERT INTO extracurriculars (name, completed) VALUES (%s, %s)", (name, False))
    conn.commit()

# ✅ Delete extracurricular from PostgreSQL
def delete_extracurricular(name):
    cursor.execute("DELETE FROM extracurriculars WHERE name = %s", (name,))
    conn.commit()

# ✅ Update extracurricular status in PostgreSQL
def update_extracurricular(name, completed):
    cursor.execute("UPDATE extracurriculars SET completed = %s WHERE name = %s", (completed, name))
    conn.commit()

# ✅ Main Function for Extracurricular UI
def main(page: ft.Page):
    page.bgcolor = ft.Colors.BLUE_300
    page.title = "Your Personal Extracurricular Schedule"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.ADAPTIVE

    # ✅ Load extracurriculars from database
    extracurriculars_data = load_extracurriculars()

    # ✅ Display previously saved extracurriculars
    for extracurricular in extracurriculars_data:
        page.add(ft.Text(extracurricular["name"]))

    # ✅ Add UI Elements
    page.add(ExtracurricularApp())

    def add_reminder(e):
        event = event_input.value
        date = date_input.value

        try:
            event_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            current_date = datetime.datetime.now()
            if event_date > current_date:
                page.add(ft.Text(f"Reminder added for '{event}' on {event_date.strftime('%A, %B %d, %Y')}", color=ft.colors.WHITE))
                save_extracurricular(event)  # ✅ Save to database
            else:
                page.add(ft.Text("The event date should be in the future. Please try again.", color=ft.colors.RED))
        except ValueError:
            page.add(ft.Text("Invalid date format. Please enter YYYY-MM-DD.", color=ft.colors.RED))

    # ✅ Reminder Input Fields
    event_input = ft.TextField(label="Event Name")
    date_input = ft.TextField(label="Event Date (YYYY-MM-DD)")
    add_reminder_button = ft.ElevatedButton("Add Reminder", on_click=add_reminder)

    # ✅ Display UI Elements
    page.add(ft.Column([event_input, date_input, add_reminder_button]))

# ✅ Don't call `ft.app(main)` here! This will be called from `Primary.py`
