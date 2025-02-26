import flet as ft
import datetime

from flet.core import page


class createcalender():
    print("nada")
    def go(page: ft.Page):
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        def handle_change(e):
            page.add(ft.Text(f"Date changed: {e.control.value.strftime('%Y-%m-%d')}"))

        def handle_dismissal(e):
            page.add(ft.Text(f"DatePicker dismissed"))

        page.add(
            ft.ElevatedButton(
                "Pick date",
                icon=ft.Icons.CALENDAR_MONTH,
                on_click=lambda e: page.open(
                    ft.DatePicker(
                        first_date=datetime.datetime.now(),
                        last_date=datetime.datetime(year=2028, month=10, day=1),
                        on_change=handle_change,
                        on_dismiss=handle_dismissal,
                    )
                ),
            )
        )

    grabpass = open("infoPassing.txt", 'r')
    print("opened")
    for line in grabpass:
        content = grabpass.readline()
        print(content + "content")
        if content == "extracuriculars":
            print("keyword found ec")
            close = "false"
        else:
            close = "true"

    if close == "true":
        print("keywod not found")
        ft.app(go)

    from Extracurricular import Extracurricular
    #ft.app(main)
